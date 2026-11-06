#!/usr/bin/env python3
"""Validate this package's concrete metadata and local document links."""
from pathlib import Path
import re
import sys


def main():
    root = Path(__file__).resolve().parents[1]
    skill = root / "skills" / "kawik-studio"
    errors = []
    required = ["SKILL.md", "agents/openai.yaml", "references/routing.md",
                "references/modeling.md", "references/studio.md", "references/engineering.md"]
    for name in required:
        if not (skill / name).is_file():
            errors.append(f"Missing skill file: {name}")
    entry = skill / "SKILL.md"
    if entry.is_file():
        text = entry.read_text(encoding="utf-8")
        front = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
        if not front:
            errors.append("SKILL.md needs YAML frontmatter")
        else:
            if not re.search(r"^name: kawik-studio$", front[1], re.M):
                errors.append("Skill name must match kawik-studio")
            if not re.search(r"^description: .+", front[1], re.M):
                errors.append("Missing discovery description")
    for doc in root.rglob("*.md"):
        text = doc.read_text(encoding="utf-8")
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
            if "://" in target or target.startswith("#"):
                continue
            path = (doc.parent / target.split("#", 1)[0]).resolve()
            if not path.is_relative_to(root):
                errors.append(f"Non-portable link in {doc.relative_to(root)}: {target}")
            elif not path.exists():
                errors.append(f"Broken link in {doc.relative_to(root)}: {target}")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("Validated: skill metadata, required files and local Markdown links.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
