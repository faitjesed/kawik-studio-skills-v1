# Sources and integration decisions

Prepared 2026-11-06. This package contains independently written instructions; it does not vendor the upstream RBSmithy package. The full bundle now includes the user's 29 existing roblox-* skills, copied without content changes.

## Reviewed sources

- Existing local Roblox skills: collaboration mode, building, Studio MCP, Luau core/patterns, architecture, tooling and lighting. They are now bundled specialists; their ownership, security, source-of-truth and evidence workflows are preserved rather than replaced with duplicate implementations.
- [RBSmithy Free](https://github.com/gogolumo/rbsmithy-roblox-claude-skill), especially its [main skill](https://github.com/gogolumo/rbsmithy-roblox-claude-skill/blob/main/skills/rbsmithy/SKILL.md), [3D Asset Forge Director](https://github.com/gogolumo/rbsmithy-roblox-claude-skill/blob/main/skills/rbsmithy/reference/3D_ASSET_FORGE_DIRECTOR.md), [Blender pipeline](https://github.com/gogolumo/rbsmithy-roblox-claude-skill/blob/main/skills/rbsmithy/reference/BLENDER_PRODUCTION_PIPELINE.md), [MeshPart import](https://github.com/gogolumo/rbsmithy-roblox-claude-skill/blob/main/skills/rbsmithy/reference/ROBLOX_MESHPART_IMPORT_PIPELINE.md) and [skill interoperability](https://github.com/gogolumo/rbsmithy-roblox-claude-skill/blob/main/skills/rbsmithy/reference/THIRD_PARTY_3D_SKILL_INTEROP.md). Upstream identifies its Free edition as MIT-licensed. No paid Pro content was accessed or included. Remote pages were reviewed on this date; this package does not track their future changes automatically.
- The locally available Codex `skill-creator` instructions for focused routing, progressive disclosure, realistic validation, and preserving user scope.

## Selection

The useful modeling ideas are integrated as a compact original workflow: choose a suitable construction method, inspect a prototype before repetition, prepare meshes deliberately for import, use fitting collision, and verify the actual engine result.

The following upstream framing is deliberately not adopted: blanket authority over other Roblox skills; the assumption that only text and placeholder meshes are available; mandatory long answer templates for every task; unrelated production requirements for minor edits. Access, actual tool schemas, established project conventions, and the user's scope remain authoritative under the host's instruction hierarchy.

No RBSmithy scripts, blueprints, asset files or code templates are redistributed. The bundled roblox-* files preserve their original text, source citations and provenance; this package does not assert new authorship over them. If future revisions copy substantial upstream material, retain its original copyright and license notices with those files rather than attributing it solely to this package.
