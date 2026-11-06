#!/usr/bin/env python3
"""Install the complete local skill bundle without replacing conflicting copies."""
import argparse
import json
import os
from pathlib import Path
import shutil


def files(root):
    return {str(p.relative_to(root)): p.read_bytes() for p in root.rglob('*') if p.is_file()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--destination', type=Path, help='Destination skills directory')
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    names = json.loads((root / 'skills.json').read_text())['skills']
    codex_home = Path(os.environ.get('CODEX_HOME') or Path.home() / '.codex')
    destination = (args.destination or codex_home / 'skills').expanduser().resolve()
    pending = []
    for name in names:
        if not isinstance(name, str) or Path(name).name != name or name in ('.', '..'):
            parser.exit(1, 'Invalid skill name; nothing installed.\n')
        source, target = root / 'skills' / name, destination / name
        if not (source / 'SKILL.md').is_file():
            parser.exit(1, f'Missing skill: {name}; nothing installed.\n')
        if target.is_symlink():
            parser.exit(1, f'Refusing symlink destination: {target}; nothing installed.\n')
        if target.exists():
            if not target.is_dir() or files(source) != files(target):
                parser.exit(1, f'Conflicting existing skill: {target}; nothing installed. Back up or move that copy before retrying.\n')
            print(f'Already identical: {name}')
        else:
            pending.append((source, target))
    if args.dry_run:
        print(f'Would install {len(pending)} skills; no files changed.')
        return
    destination.mkdir(parents=True, exist_ok=True)
    created = []
    try:
        for source, target in pending:
            # Claim the directory before copying so a concurrent existing path is never overwritten.
            target.mkdir()
            created.append(target)
            shutil.copytree(source, target, dirs_exist_ok=True)
            print(f'Installed: {target.name}')
    except Exception:
        for target in reversed(created):
            shutil.rmtree(target)
        raise
    print(f'Complete: {len(names)} skills available ({len(pending)} newly installed).')


if __name__ == '__main__':
    main()
