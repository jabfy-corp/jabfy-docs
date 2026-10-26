#!/usr/bin/env python3
"""Recopie le docs/ de chaque repo listé dans composants.txt vers documentation/composants/<repo>/.

Usage : python3 scripts/sync_composants.py --sources <dossier des clones>

<dossier des clones>/<repo>/docs/ est la source de chaque repo. Le script :
- ignore les fichiers et dossiers dont le nom commence par « _ » ou « . » ;
- ajoute en tête de chaque page un bandeau « à modifier dans le repo d'origine » ;
- réécrit vers GitHub les liens qui sortent de docs/ (../schemas/x.json…) ;
- génère un README.md pour chaque dossier qui n'en a pas ;
- régénère la section « ## Composants » de documentation/SUMMARY.md.

Un dossier généré contient un fichier témoin (.synchro). Un dossier sans témoin a
été écrit à la main dans jabfy-docs : il n'est jamais modifié ni supprimé, et
apparaît quand même dans le sommaire. Un repo dont le clone a échoué garde sa
doc déjà publiée.

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
MARKER = ".synchro"
GENERATED_NOTE = "Index généré automatiquement"
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


def is_generated(folder):
    return (folder / MARKER).is_file()


def subfolders(folder):
    return sorted(p for p in folder.iterdir() if p.is_dir() and is_published((p.name,)))


def ordered_pages(folder):
    """Pages du dossier dans l'ordre où son README les cite, puis les autres par nom."""
    pages = {p.name: p for p in folder.glob("*.md") if p.name != "README.md"}
    order = []
    readme = folder / "README.md"
    if readme.is_file():
        for match in LINK.finditer(readme.read_text(encoding="utf-8")):
            name = match.group(2).partition("#")[0]
            if name in pages and name not in order:
                order.append(name)
    order += sorted(set(pages) - set(order))
    return [pages[name] for name in order]


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
    (dest / MARKER).write_text(
        f"Dossier généré par scripts/sync_composants.py depuis {repo}/docs/ : ne pas modifier ici.\n",
        encoding="utf-8",
    )


def ensure_readmes(top):
    """Crée l'index des dossiers sans README.md et tient à jour les index déjà générés."""
    folders = [top] + [p for p in sorted(top.rglob("*"))
                       if p.is_dir() and is_published(p.relative_to(top).parts)]
    for folder in folders:
        readme = folder / "README.md"
        if readme.exists() and GENERATED_NOTE not in readme.read_text(encoding="utf-8"):
            continue
        lines = [f"# {folder.name}", "", f"> {GENERATED_NOTE}.", ""]
        lines += [f"* [{link_text(page_title(p))}]({p.name})" for p in ordered_pages(folder)]
        lines += [f"* [{s.name}]({s.name}/README.md)" for s in subfolders(folder)]
        readme.write_text("\n".join(lines) + "\n", encoding="utf-8")


def summary_lines(folder, depth, root):
    indent = "  " * depth
    lines = []
    for page in ordered_pages(folder):
        lines.append(f"{indent}* [{link_text(page_title(page))}]({page.relative_to(root).as_posix()})")
    for sub in subfolders(folder):
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


def sync_repo(repo, src, dest):
    if dest.exists() and not is_generated(dest):
        if src.is_dir():
            print(f"::warning::{repo} : composants/{repo}/ est écrit à la main, "
                  "le docs/ du repo n'est pas recopié")
        return
    if dest.exists():
        shutil.rmtree(dest)
    if not src.is_dir():
        print(f"{repo} : pas de dossier docs/, ignoré")
        return
    copy_docs(repo, src, dest)
    print(f"{repo} : synchronisé")


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

    for repo in repos:
        if (args.sources / repo).is_dir():
            sync_repo(repo, args.sources / repo / "docs", composants / repo)
        else:
            # Clone raté (repo privé sans token…) : on garde la doc déjà publiée.
            print(f"::warning::{repo} : source absente, doc déjà publiée conservée")

    for folder in subfolders(composants):
        if is_generated(folder) and folder.name not in repos:
            shutil.rmtree(folder)
            print(f"{folder.name} : retiré (plus listé dans composants.txt)")

    listed = [composants / r for r in repos if (composants / r).is_dir()]
    others = [f for f in subfolders(composants) if f.name not in repos]
    entries = ["* [À propos de cette section](composants/README.md)"]
    for folder in listed + others:
        ensure_readmes(folder)
        entries.append(f"* [{folder.name}](composants/{folder.name}/README.md)")
        entries += summary_lines(folder, 1, site)
    update_summary(site / "SUMMARY.md", entries)


if __name__ == "__main__":
    main()
