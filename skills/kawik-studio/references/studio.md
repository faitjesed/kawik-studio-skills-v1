# Live Studio workflow

1. Discover the bridge and target instance using its available tools. Read its mode and available Edit/Client/Server contexts. Reacquire references on each stateless execution call.
2. Inspect the intended root and dependencies. Use the current hierarchy and geometry rather than relying on remembered coordinates. Establish a named root and an undo/removal boundary for a new build.
3. Mutate one logical phase at a time. Respect the bridge's current batching constraints. Construct bounded subtrees and yield between batches; avoid a single huge final parenting operation that defeats incremental construction.
4. Read back the specific result: names, properties, count/bounds, exceptions, or full authored script as relevant. After a timeout or disconnect, rediscover and inspect before retrying. Stop dependent mutations after a real error.
5. For visual or traversal changes, capture deliberate viewpoints and run the relevant route in the actual installed scene. A pathfinding result is useful evidence but does not establish that an avatar reached the endpoint. Read its final position and supporting surface after movement completes.
6. Test gameplay in a running VM. Confirm the intended context before inspecting runtime state. Temporary test teleports, open gates, speeds, and camera settings should remain in the play session or be explicitly restored.
7. Stop only a play session started for this work; preserve a pre-existing user session unless the task requires changing it and authorization covers that change. Leave the edit scene in the intended final state.

Use the bridge's supported script-editing tools, or the appropriate ScriptEditorService path when available, so an open editor is not silently overwritten. Group reversible edits with supported undo recording when possible. Do not invent APIs or ignore failures because the requested result seems plausible.

## Shared-state changes

A separate Model does not isolate Lighting, terrain, Teams, global scripts, or spawn selection. Identify these separately. Prefer localized runtime behavior or an explicit reversible preview for per-map atmosphere. If a global edit is required, preserve the prior values for every property changed and clearly state its scope.

For spawn selection, inspect every enabled SpawnLocation and relevant RespawnLocation/team behavior. Use the smallest spawn configuration that meets the user request; player capacity does not by itself require one spawn object per player. Check natural spawning in a fresh play session, not a teleport presented as a spawn test.

## Reporting

Record factual evidence proportionate to the work: root/target, changed behavior, actual checks, and what remains unverified. Counts, a clean console, or one successful route do not establish complete performance or release readiness. Publishing, uploading, and changing external settings follow the host's authorization rules and the user's actual scope.
