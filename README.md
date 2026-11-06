# Kawik Studio Skills v1 — Kasha

A practical agent skill for building Roblox environments, 3D assets, and Luau features with the Studio and Blender tools available in your environment.

**Repository:** `kawik-studio-skills-v1`  
**Skill identifier:** `kawik-studio`  
**Display name:** Kawik Studio — Kasha

## Overview

This is the complete 30-skill bundle: Kawik Studio (Kasha) plus all 29 Roblox specialist skills used by the author. A friend can install the same instruction set from this repository without locating separate roblox-* packages.

Kasha coordinates the relevant specialists; it does not load all 30 skills into every task. Read roblox-collaboration-mode first, then the specialist instructions needed for the requested change. The full inventory is in [skills.json](skills.json).

The original specialist files are included without content changes. Studio MCP, Roblox Studio, Blender, and other tools are separate software connections: the skill bundle does not install or authenticate them. Equal skill files do not guarantee equal tool availability or results on another machine.

## Improvements

- Choose a modeling method for the task: existing project assets, native Parts/CSG, Blender, or mesh generation.
- Inspect one representative module before repeating an entire kit.
- Place assets using real support surfaces and contact geometry; a bounding box alone does not prove that an irregular object is grounded.
- Inspect silhouettes, structural joins, doors, stairs, signs, collisions, and imported geometry.
- Separate visual meshes from simple gameplay collision when appropriate.
- Verify the avatar's final position after navigation instead of relying only on a tool's Success response.
- Account for shared lighting and spawn selection when creating a separate map.
- Match validation and reporting to the size and risk of the change.

The package excludes assumptions that available tools cannot be used, blanket claims of authority over other skills, mandatory long response templates, and automatic expansion into unrelated systems or agent workflows.

## Install in Codex

From this repository's root directory, using Python 3.9 or later:

```sh
python3 scripts/validate.py
python3 scripts/install.py --dry-run
python3 scripts/install.py
```

The installer installs all 30 skills listed in `skills.json` into the `skills` directory under `CODEX_HOME`, or into `~/.codex/skills` when that variable is unset. Identical existing copies are skipped. If any existing copy differs, the installer stops before writing anything; back up or move the conflicting copy first. Unrelated skills are left untouched. Re-running the installer with matching files is safe. To select another skills directory:

```sh
python3 scripts/install.py --destination /path/to/skills
```

If the skill does not appear in the available skills list after installation, start a new session. Invoke it explicitly with:

```text
Use $kawik-studio. Build a separate medieval blacksmith shop in the connected Roblox Studio scene and verify the result.
```

Automatic selection is allowed but depends on the host environment and task relevance. The explicit identifier `$kawik-studio` is the clearest way to request it.

When upgrading from an earlier coordinator-only bundle, back up or move the old `kawik-studio` folder before installing this version if the installer reports a conflict. Do not remove unrelated skills.

## Package structure

```text
skills/
  roblox-*/                 # 29 specialists, each with SKILL.md and references
  kawik-studio/
    SKILL.md
    agents/openai.yaml
    references/
      routing.md
      modeling.md
      studio.md
      engineering.md
scripts/
  install.py
  validate.py
docs/
  acceptance.md
  verification.md
```

## Upload to GitHub manually

Create a repository named `kawik-studio-skills-v1` in your intended personal account. Use **Add file → Upload files** to upload this folder's contents, with `README.md`, `skills`, and `scripts` at the repository root. Extract the ZIP before uploading; uploading only the archive will not expose the skill files as repository contents.

No command in this package creates a GitHub repository, configures a Git remote, pushes changes, or uses work-account credentials.

## Validation and limitations

`scripts/validate.py` checks the package structure, skill identifier, basic metadata, and local document links. These checks do not validate a Roblox game or guarantee agent behavior. See the [behavioral acceptance scenarios](docs/acceptance.md) and [packaging verification record](docs/verification.md).

Sources and compatibility decisions are documented in [SOURCES.md](SOURCES.md). Independently written files in this package use the [MIT license](LICENSE). The MIT notice covers the independently written Kawik additions. Bundled specialist files preserve their supplied provenance and notices; no new license ownership is asserted over those files. External tools and assets retain their own licenses.

## Included specialists

- `roblox-analytics`
- `roblox-animation-vfx`
- `roblox-architecture`
- `roblox-audio`
- `roblox-building`
- `roblox-camera`
- `roblox-cloud`
- `roblox-collaboration-mode`
- `roblox-data`
- `roblox-game-design`
- `roblox-growth-design`
- `roblox-gui`
- `roblox-input`
- `roblox-lighting`
- `roblox-localization`
- `roblox-luau-core`
- `roblox-luau-patterns`
- `roblox-luau-types`
- `roblox-monetization`
- `roblox-networking`
- `roblox-npc-ai`
- `roblox-performance`
- `roblox-physics`
- `roblox-player-psychology`
- `roblox-publish-checklist`
- `roblox-security`
- `roblox-server-data`
- `roblox-studio-mcp`
- `roblox-tooling`
