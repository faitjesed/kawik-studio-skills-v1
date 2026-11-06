# Kawik Studio Skills v1 — Kasha

A practical agent skill for building Roblox environments, 3D assets, and Luau features with the Studio and Blender tools available in your environment.

**Repository:** `kawik-studio-skills-v1`  
**Skill identifier:** `kawik-studio`  
**Display name:** Kawik Studio — Kasha

## Overview

Kawik Studio is a standalone skill with a concise shared workflow and focused references for modeling, live Studio work, and engineering. When specialized `roblox-*` skills are installed, it consults the relevant ones. Its core instructions also work without those optional skills.

Existing specialist skills are not bundled or modified by this package. This avoids maintaining competing copies of the same guidance. The package does not install Blender, Studio MCP, Rojo, or other tools; it uses capabilities that are actually connected.

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

The installer copies only `skills/kawik-studio` into the `skills` directory under `CODEX_HOME`, or into `~/.codex/skills` when that variable is unset. It refuses to overwrite an existing destination and leaves other skills untouched. To select another skills directory:

```sh
python3 scripts/install.py --destination /path/to/skills
```

If the skill does not appear in the available skills list after installation, start a new session. Invoke it explicitly with:

```text
Use $kawik-studio. Build a separate medieval blacksmith shop in the connected Roblox Studio scene and verify the result.
```

Automatic selection is allowed but depends on the host environment and task relevance. The explicit identifier `$kawik-studio` is the clearest way to request it.

## Package structure

```text
skills/kawik-studio/
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

Sources and compatibility decisions are documented in [SOURCES.md](SOURCES.md). Independently written files in this package use the [MIT license](LICENSE). External tools, separately installed skills, and assets retain their own licenses.
