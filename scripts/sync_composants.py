#!/usr/bin/env python3
"""Recopie le docs/ de chaque repo listé dans composants.txt vers documentation/composants/<repo>/.

Usage : python3 scripts/sync_composants.py --sources <dossier des clones>

<dossier des clones>/<repo>/docs/ est la source de chaque repo. Le script :
- ignore les fichiers et dossiers dont le nom commence par « _ » ou « . » ;
- ajoute en tête de chaque page un bandeau « à modifier dans le repo d'origine » ;
- réécrit vers GitHub les liens qui sortent de docs/ (../schemas/x.json…) ;
- génère un README.md pour chaque dossier qui n'en a pas ;
- régénère la section « ## Composants » de documentation/SUMMARY.md.

Stdlib uniquement : lançable tel quel en local comme en CI.
"""

import argparse
import posixpath
import re
import shutil
import sys
from pathlib import Path

ORG = "jabfy-corp"
BRANCH = "main"
# Dossier synchronisé avec l'espace GitBook (voir gitbook-docs.yaml).
SITE_DIR = "documentation"
SECTION = "## Composants"
LINK = re.compile(r"(\]\()([^)\s]+)((?:\s+\"[^\"]*\")?\))")
SCHEME = re.compile(r"^[a-z][a-z0-9+.-]*:", re.IGNORECASE)
FENCE = re.compile(r"^\s*(```|~~~)")


def read_repos(path):
    repos = []
    for line in path.read_text(encoding="utf-8").splitlines():
        name = line.split("#", 1)[0].strip()
        if name:
            repos.append(name)
    return repos


def is_published(rel_parts):
    return not any(part.startswith(("_", ".")) for part in rel_parts)


def github_url(repo, path):
    return f"https://github.com/{ORG}/{repo}/blob/{BRANCH}/{path}"


def rewrite_links(text, repo, rel):
    """Réécrit vers GitHub les liens relatifs qui pointent hors du docs/ publié."""
    base = posixpath.join("docs", posixpath.dirname(rel))

    def fix(match):
        target = match.group(2)
        if SCHEME.match(target) or target.startswith(("#", "/")):
            return match.group(0)
        path, sep, anchor = target.partition("#")
        resolved = posixpath.normpath(posixpath.join(base, path))
        if resolved.startswith("../") or resolved == "..":
            return match.group(0)
        parts = resolved.split("/")
        if parts[0] == "docs" and len(parts) > 1 and is_published(parts[1:]):
            return match.group(0)
        return match.group(1) + github_url(repo, resolved) + sep + anchor + match.group(3)

    out, in_fence = [], False
    for line in text.splitlines(keepends=True):
        if FENCE.match(line):
            in_fence = not in_fence
        out.append(line if in_fence else LINK.sub(fix, line))
    return "".join(out)


def add_banner(text, repo, rel):
    """Place le bandeau après le front matter et le titre H1 éventuels."""
    banner = (
        f"> ⚠️ Page recopiée automatiquement depuis "
        f"[{repo}/docs/{rel}]({github_url(repo, 'docs/' + rel)}). "
        "Toute modification faite ici sera écrasée : modifiez le repo d'origine.\n\n"
    )
    head = ""
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            head, text = text[: end + 5], text[end + 5 :]
    stripped = text.lstrip("\n")
    if stripped.startswith("# "):
        lead = text[: len(text) - len(stripped)]
        title, _, rest = stripped.partition("\n")
        body = rest.lstrip("\n")
        return f"{head}{lead}{title}\n\n{banner}{body}"
    return head + banner + text


def page_title(path):
    if path.is_file():
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.startswith("# "):
                return line[2:].strip()
    name = path.parent.name if path.name == "README.md" else path.stem
    return name.replace("-", " ").replace("_", " ").capitalize()


def link_text(title):
    return title.replace("[", "\\[").replace("]", "\\]")


def copy_docs(repo, src, dest):
    for path in sorted(src.rglob("*")):
        rel = path.relative_to(src)
        if path.is_symlink() or not path.is_file() or not is_published(rel.parts):
            continue
        out = dest / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        if path.suffix.lower() == ".md":
            text = path.read_text(encoding="utf-8")
            text = add_banner(rewrite_links(text, repo, rel.as_posix()), repo, rel.as_posix())
            out.write_text(text, encoding="utf-8")
        else:
            shutil.copy2(path, out)


def ensure_readmes(repo, dest):
    for folder in [dest, *sorted(p for p in dest.rglob("*") if p.is_dir())]:
        readme = folder / "README.md"
        if readme.exists():
            continue
        name = repo if folder == dest else folder.name
        lines = [f"# {name}", "", f"> Index généré automatiquement depuis le docs/ de {repo}.", ""]
        lines += [f"* [{link_text(page_title(p))}]({p.name})" for p in sorted(folder.glob("*.md"))]
        lines += [f"* [{s.name}]({s.name}/README.md)" for s in sorted(folder.iterdir()) if s.is_dir()]
        readme.write_text("\n".join(lines) + "\n", encoding="utf-8")


def summary_lines(folder, depth, root):
    indent = "  " * depth
    lines = []
    for page in sorted(folder.glob("*.md")):
        if page.name != "README.md":
            lines.append(f"{indent}* [{link_text(page_title(page))}]({page.relative_to(root).as_posix()})")
    for sub in sorted(p for p in folder.iterdir() if p.is_dir()):
        readme = sub / "README.md"
        lines.append(f"{indent}* [{link_text(page_title(readme))}]({readme.relative_to(root).as_posix()})")
        lines += summary_lines(sub, depth + 1, root)
    return lines


def update_summary(summary, entries):
    lines = summary.read_text(encoding="utf-8").splitlines()
    try:
        start = lines.index(SECTION)
    except ValueError:
        sys.exit(f"{summary} : section « {SECTION} » introuvable")
    end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")), len(lines))
    tail = [""] + lines[end:] if end < len(lines) else []
    summary.write_text("\n".join(lines[: start + 1] + [""] + entries + tail) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--sources", required=True, type=Path, help="dossier contenant un clone par repo")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent,
                        help="racine du repo jabfy-docs (par défaut : parent de scripts/)")
    args = parser.parse_args()

    root = args.root.resolve()
    site = root / SITE_DIR
    composants = site / "composants"
    repos = read_repos(root / "composants.txt")

    # Vérifier toutes les sources avant d'effacer quoi que ce soit :
    # un clone raté ne doit pas faire disparaître la doc déjà publiée.
    missing = [r for r in repos if not (args.sources / r).is_dir()]
    if missing:
        sys.exit(f"Sources absentes dans {args.sources} : {', '.join(missing)}")

    entries = ["* [À propos de cette section](composants/README.md)"]
    synced = set()
    for repo in repos:
        dest = composants / repo
        if dest.exists():
            shutil.rmtree(dest)
        src = args.sources / repo / "docs"
        if not src.is_dir():
            print(f"{repo} : pas de dossier docs/, ignoré")
            continue
        copy_docs(repo, src, dest)
        if not dest.exists():
            print(f"{repo} : rien à publier dans docs/, ignoré")
            continue
        ensure_readmes(repo, dest)
        entries.append(f"* [{repo}](composants/{repo}/README.md)")
        entries += summary_lines(dest, 1, site)
        synced.add(repo)
        print(f"{repo} : synchronisé")

    for stale in composants.iterdir():
        if stale.is_dir() and stale.name not in synced:
            shutil.rmtree(stale)
            print(f"{stale.name} : retiré (plus listé ou plus de docs/)")

    update_summary(site / "SUMMARY.md", entries)


if __name__ == "__main__":
    main()
