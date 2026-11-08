---
name: kawik-studio
description: Build, improve, or review Roblox environments, 3D assets, and Luau features using available Studio and Blender tools. Coordinates bundled Roblox specialist skills and adds a focused asset-quality workflow; also supports a standalone fallback. Invoke as Kawik Studio or Kasha.
---

# Kawik Studio — Kasha

Turn the user's Roblox request into the requested artifact: an actual Studio change when access exists, repository changes when files own the source, or an explicit offline deliverable when neither is available. Do not substitute a plan for an authorized build.

## Integrate without weakening existing skills

For the full bundle, read `roblox-collaboration-mode` first, then only the specialist skills needed for this task. Discover their real paths from the current skill catalog; do not assume a username or hardcoded installation root. This skill is supplementary: it does not override the host's instructions, the user's requested scope, or established domain safeguards. Resolve overlapping guidance by actual environment capabilities and task relevance. A concrete disagreement affecting correctness should be surfaced, not silently combined.

For specialist selection, use [references/routing.md](references/routing.md). Missing specialists in a partial installation do not block ordinary work: the workflows here cover the common core. Do not load the entire installed library or upstream RBSmithy by default.

## Establish the working context

- Inspect the project and connected Studio instances before editing. Identify Studio-owned, file-owned, and hybrid content; avoid overwriting the other source of truth.
- Reuse the user's already confirmed target. Ask only when multiple plausible targets remain or required information is missing.
- Inspect scene bounds, local axes, pivots, material variants, reusable project assets, and relevant scripts. Existing material names and their BaseMaterial take precedence over guessed names.
- Make isolated additions under a named root when a separate map or asset is requested. Scope lighting, spawns, scripts, and shared settings deliberately as well as geometry.
- Use available modeling, mesh-generation, import, and inspection tools according to their live schemas. A text skill cannot add unavailable capabilities, but must not disable tools the environment actually provides.

## Choose the work path

**Environment or 3D asset:** read [references/modeling.md](references/modeling.md). Prefer coherent modular construction, supported geometry, readable silhouettes, and inspectable joins. Choose project reuse, native geometry, Blender, or generated meshes per asset rather than forcing one technique onto the whole scene.

**Live Studio mutation or testing:** read [references/studio.md](references/studio.md). Work in bounded phases and read back the result. An ambiguous timeout requires inspection before retrying.

**Luau or game feature:** read [references/engineering.md](references/engineering.md). Preserve the project's ownership boundaries and established interfaces. Add infrastructure only when the requested behavior needs it.

## Acceptance and communication

Scale evidence to the change. A relocated sign needs placement/readback; a room connection needs avatar clearance and traversal; a purchase or persistence change needs the relevant domain workflow. Use runtime and visual evidence where those are what establishes success. Do not claim multiplayer, mobile, performance, or geometry correctness from static counts alone.

Report the implemented result, meaningful checks, and any remaining limitations in the user's language. Keep routine work concise; reserve full asset briefs, budgets, scored reviews, or release checklists for tasks that need them. Do not add unrelated economy, analytics, localization, release, or multi-agent work to a small edit.

For construction defects, follow the targeted surface/joint references linked from modeling.md. After two failed repairs of one joint, diagnose and rebuild the local module rather than repeating unverified offsets or cuts.
