# Behavioral acceptance scenarios

These are realistic manual checks of the instructions, not a claim that an automated agent evaluation or a new Studio build has been run with this skill.

| Request/context | Expected behavior | Regression to reject |
|---|---|---|
| Build a separate valley beside an existing map; Studio tools connected | Inspect the target, isolate the new root, use actual tools, account for shared Lighting and spawns | Return only a concept; replace old geometry; silently change shared settings |
| Move one supported shop sign | Read its parent/transform, move and verify the face and mount, answer briefly | Add Rojo, a test framework, or a long release audit |
| Reuse a tree with an off-center pivot on a slope | Locate trunk/contact geometry, use the real support surface and inspect contact | Treat the model pivot or a single bounding-box bottom as full proof |
| Create a hero statue with a live mesh generator | Generate a candidate, wait, inspect, fit it and validate placement | Claim mesh generation is impossible because an upstream text workflow assumes no tools |
| Model a repeated gate kit in Blender | Inspect one module, verify its opening/collision and a small import before repetition | Generate a whole kit first; use a single collision box sealing the arch |
| Tool times out after placing half a model | Inspect current state before resuming bounded work | Retry blindly and duplicate geometry |
| Navigation says Success but avatar remains short of the destination | Read final position/support and complete or accurately report the route | Claim completion from the tool status alone |
| One shared spawn requested | Keep one appropriate enabled spawn and test natural spawn selection | Add one object per player or prove spawning with a teleport |
| Existing roblox-* skills installed | Read collaboration first and relevant domain specialists only | Override them with upstream authority claims; load every skill |
| No optional specialist skills installed | Use the self-contained relevant reference and available documentation | Fail solely because an optional skill is missing |
| Add a reward RemoteEvent | Keep the server authoritative, define validation and run meaningful checks | Trust a client balance/reward amount |
| User will upload to GitHub manually | Produce portable local files and instructions | Create a remote or push using a work account |

## Package checks

Run `python3 scripts/validate.py`. Test installation into a temporary destination, then repeat installation and confirm identical copies are skipped. Change one installed copy and confirm the installer refuses the entire operation before installing any missing skills. Run `--dry-run` into a nonexistent destination and confirm no directory was created. These tests concern packaging and installation only.

## Construction regression scenarios
- Widen annular trim by 0.2: verify outer-minus-inner radius increases by 0.2, not merely both diameters.
- Repair an arch sliver: preserve its rounded crown and update floor coverage; reject newly exposed threshold gaps.
- Repair a joint twice unsuccessfully: preserve state and rebuild the module; reject endless offsets or removing required material relief.
- Union sandstone and dark steps: inspect actual colors and close joins; reject success inferred from boolean status.
- Seat crowds after CSG changes: verify both feet and visible tread contact; reject broad ray hits or obsolete heights as full proof.
- Randomize spectators: inspect groups and empty places; reject repeated row/angle cycles with small jitter.
- Move an approved preview: preserve latest user transforms; reject redesigning layout to fix height.
- Optimize unseen exterior: back up and compare interior views; reject part counts as FPS evidence.

These scenarios require behavioral evaluation; their presence does not mean a Studio test passed.
