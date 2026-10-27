"""Banc d'essai jabfy-bus : débit de télémétrie et latence d'une commande.

Usage : PYTHONPATH=../jabfy-bus python3 benchmarks/bench_bus.py
"""

import gc
import os
import statistics
import tempfile
import time
import tracemalloc

from jabfy_bus.audit.log import AuditLog
from jabfy_bus.core.bus import UniversalJsonBus
from jabfy_bus.core.message import Entity, Value, new_message
from jabfy_bus.core.registry import EntityRegistry
from jabfy_bus.core.types import MessageType, RiskLevel, TrustLevel
from jabfy_bus.execution.executor import ExecutionLayer
from jabfy_bus.verification.engine import VerificationEngine
from jabfy_bus.verification.policies import Policy


def telemetry_message(i):
    return new_message(
        MessageType.TELEMETRY,
        adapter="bench",
        protocol="mqtt",
        entity=Entity(id=f"sensor.t{i % 50}", domain="sensor", entity_class="temperature"),
        value=Value(raw=200 + i % 5, normalized=20.0 + i % 5 / 10, unit="°C"),
        trust_level=TrustLevel.LOCAL_GATEWAY,
    )


def telemetry_throughput(n, repeats=5):
    built, published = [], []
    for _ in range(repeats):
        bus = UniversalJsonBus(history_size=500)
        EntityRegistry().attach(bus)
        bus.subscribe("*", lambda m: None, name="consumer")
        t0 = time.perf_counter()
        messages = [telemetry_message(i) for i in range(n)]
        t1 = time.perf_counter()
        for m in messages:
            bus.publish(m)
        t2 = time.perf_counter()
        built.append(n / (t2 - t0))
        published.append(n / (t2 - t1))
    return statistics.median(built), statistics.median(published)


def command_latencies(n, audit_path):
    bus = UniversalJsonBus()
    audit = AuditLog(audit_path)
    engine = VerificationEngine(
        bus,
        policies=[Policy(name="lights", effect="allow", max_risk=RiskLevel.MEDIUM,
                         domains={"light"}, min_trust=TrustLevel.INTERNAL)],
        audit=audit,
    )
    engine.attach()
    executor = ExecutionLayer(bus, audit=audit, approval_validator=engine.consume_approval)
    executor.register_transport("mqtt", lambda target, payload: None)
    executor.attach()
    latencies = []
    for _ in range(n):
        request = new_message(
            MessageType.COMMAND_REQUESTED,
            adapter="bench",
            protocol="internal",
            entity=Entity(id="light.salon", domain="light"),
            command={"action": "turn_on", "target": "zigbee2mqtt/salon_lamp",
                     "protocol": "mqtt", "params": {}},
            trust_level=TrustLevel.INTERNAL,
        )
        t0 = time.perf_counter()
        bus.publish(request)
        latencies.append((time.perf_counter() - t0) * 1e6)
    assert executor.executed == n, (executor.executed, executor.failed)
    assert audit.verify()
    latencies.sort()
    return statistics.median(latencies), latencies[int(0.95 * len(latencies)) - 1]


def dedup_memory(n):
    """Mémoire encore allouée après n messages : l'ensemble de déduplication n'est jamais purgé."""
    bus = UniversalJsonBus(history_size=500)
    gc.collect()
    tracemalloc.start()
    for i in range(n):
        bus.publish(telemetry_message(i))
    gc.collect()
    current, _ = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return len(bus._published_ids), current / n


if __name__ == "__main__":
    built, published = telemetry_throughput(20_000)
    print(f"telemetry: build+publish {built:,.0f} msg/s | publish only {published:,.0f} msg/s")

    med, p95 = command_latencies(2_000, None)
    print(f"command (audit in memory): median {med:.0f} us | p95 {p95:.0f} us | {1e6 / med:,.0f} cmd/s")

    with tempfile.TemporaryDirectory(dir=os.path.expanduser("~")) as tmp:
        med, p95 = command_latencies(500, os.path.join(tmp, "audit.jsonl"))
    print(f"command (audit on disk + fsync): median {med:.0f} us | p95 {p95:.0f} us | {1e6 / med:,.0f} cmd/s")

    ids, per_msg = dedup_memory(100_000)
    print(f"dedup: {ids:,} ids kept after 100,000 messages, ~{per_msg:.0f} bytes still allocated per message")
