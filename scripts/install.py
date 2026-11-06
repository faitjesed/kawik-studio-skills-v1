#!/usr/bin/env python3
"""Install this local skill without replacing an existing skill directory."""
import argparse
import os
from pathlib import Path
import shutil


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--destination", type=Path, help="Destination skills directory")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    source = Path(__file__).resolve().parents[1] / "skills" / "kawik-studio"
    codex_home = Path(os.environ.get("CODEX_HOME") or Path.home() / ".codex")
    destination = (args.destination or codex_home / "skills").expanduser().resolve()
    target = destination / source.name
    if not (source / "SKILL.md").is_file():
        parser.exit(1, "Source skill is missing; nothing installed.\n")
    if target.exists() or target.is_symlink():
        parser.exit(1, f"Refusing to replace existing path: {target}\n")
    if args.dry_run:
        print(f"Would copy {source} to {target}; no files changed.")
        return
    destination.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, target)
    print(f"Installed: {target}")


if __name__ == "__main__":
    main()
