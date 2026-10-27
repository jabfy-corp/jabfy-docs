"""Banc d'essai du raisonnement : latence, JSON valide et bonne action.

Reprend le prompt système, le format de message et le parseur de jabfy-core
(main a3b9aa7). Appelle Ollama en local : http://127.0.0.1:11434/api/chat.
Usage : python3 benchmarks/bench_llm.py (Ollama démarré, modèles llama3.2 et ministral-3 téléchargés)
"""

import json
import re
import statistics
import time
import urllib.request

DEVICES = (
    "hallway_light", "hallway_window", "living_room_light", "living_room_window",
    "living_room_tv", "kitchen_light", "kitchen_window", "bedroom_light",
    "bedroom_window", "bathroom_light", "bathroom_window", "garage_light",
    "garage_door", "house_lock", "climatisation", "heater", "alarm",
)

SYSTEM_PROMPT = f"""You are a Smart Home automation controller.
You receive the current device states and a situation.
Return ONLY one raw JSON object, without markdown or explanation.

Required format:
{{"action_chain":"<one sentence describing the proposal>","changes":{{"<device_id>":true}}}}

Available device IDs: {", ".join(DEVICES)}

Rules:
- Only propose changes for available device IDs.
- Values in "changes" must be JSON booleans.
- Only include devices whose state needs to change.
- If nothing needs to change, return an empty "changes" object.
- You propose actions only. A deterministic verifier decides whether they are safe.
"""

SCHEMA = {
    "type": "object",
    "properties": {
        "action_chain": {"type": "string"},
        "changes": {
            "type": "object",
            "properties": {d: {"type": "boolean"} for d in DEVICES},
            "additionalProperties": False,
        },
    },
    "required": ["action_chain", "changes"],
}

# (consigne, état courant, changements attendus)
CASES = [
    ("Allume la lumière de la cuisine.", {}, {"kitchen_light": True}),
    ("Éteins la télé du salon.", {"living_room_tv": True}, {"living_room_tv": False}),
    ("Ferme la porte du garage.", {"garage_door": True}, {"garage_door": False}),
    ("J'ai froid.", {"heater": False}, {"heater": True}),
    ("Je vais me coucher, éteins tout dans le salon.",
     {"living_room_light": True, "living_room_tv": True},
     {"living_room_light": False, "living_room_tv": False}),
    ("Ouvre la fenêtre de la chambre.", {"bedroom_window": False}, {"bedroom_window": True}),
    ("Je pars de la maison.", {"house_lock": False, "alarm": False, "hallway_light": True},
     {"house_lock": True, "alarm": True}),
    ("Allume la lumière de la salle de bain et celle du couloir.", {},
     {"bathroom_light": True, "hallway_light": True}),
    ("Quelle heure est-il ?", {"kitchen_light": True}, {}),
    ("Il fait trop chaud ici.", {"climatisation": False}, {"climatisation": True}),
]


def user_message(prompt, state):
    if not state:
        context = "Current device state: all devices are off."
    else:
        context = "Current device state:\n" + "\n".join(
            f"  {d}: {'ON' if v else 'OFF'}" for d, v in state.items())
    return f"{context}\n\nSituation: {prompt}"


def parse(content):
    """Même logique que app/core/action_parser.py de jabfy-core."""
    cleaned = re.sub(r"^```(?:json)?\s*", "", content.strip(), flags=re.IGNORECASE)
    cleaned = re.sub(r"\s*```$", "", cleaned).strip()
    decoder = json.JSONDecoder()
    for i, ch in enumerate(cleaned):
        if ch != "{":
            continue
        try:
            payload, _ = decoder.raw_decode(cleaned[i:])
        except json.JSONDecodeError:
            continue
        if isinstance(payload, dict) and isinstance(payload.get("changes", {}), dict):
            return payload.get("changes", {})
    return None


def verified(changes):
    """Même règle que app/core/verification.py : appareils connus, booléens."""
    return all(d in DEVICES and type(v) is bool for d, v in changes.items())


def chat(model, message, schema, cpu_only):
    body = {
        "model": model,
        "stream": False,
        "messages": [{"role": "system", "content": SYSTEM_PROMPT},
                     {"role": "user", "content": message}],
        "options": {"temperature": 0.2, "seed": 42, **({"num_gpu": 0} if cpu_only else {})},
    }
    if schema:
        body["format"] = SCHEMA
    req = urllib.request.Request("http://127.0.0.1:11434/api/chat",
                                 data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json"})
    t0 = time.perf_counter()
    with urllib.request.urlopen(req, timeout=300) as r:
        data = json.load(r)
    return time.perf_counter() - t0, data


def run(model, schema, cpu_only=False):
    chat(model, "warm-up", schema, cpu_only)  # charge le modèle en mémoire
    lat, valid, correct, extra, tps = [], 0, 0, 0, []
    for prompt, state, expected in CASES:
        seconds, data = chat(model, user_message(prompt, state), schema, cpu_only)
        lat.append(seconds)
        if data.get("eval_duration"):
            tps.append(data["eval_count"] / (data["eval_duration"] / 1e9))
        changes = parse(data["message"]["content"])
        if changes is None or not verified(changes):
            continue
        valid += 1
        # Bonne action : tous les changements attendus, sans changement contraire.
        # Un changement en plus, cohérent avec l'état (ex. éteindre une lumière en partant), est compté à part.
        effective = {d: v for d, v in changes.items() if state.get(d, False) != v}
        if all(effective.get(d) == v for d, v in expected.items()) and \
                (expected or not effective):
            correct += 1
            if set(effective) - set(expected):
                extra += 1
    lat.sort()
    label = f"{model}{' (CPU)' if cpu_only else ''} | {'schema' if schema else 'prompt only'}"
    print(f"{label}: median {statistics.median(lat):.2f} s | max {lat[-1]:.2f} s | "
          f"{statistics.median(tps):.0f} tok/s | JSON valid {valid}/{len(CASES)} | "
          f"correct {correct}/{len(CASES)} (of which {extra} with extra changes)", flush=True)


if __name__ == "__main__":
    for model in ("llama3.2", "ministral-3"):
        for schema in (False, True):
            run(model, schema)
    run("llama3.2", False, cpu_only=True)
