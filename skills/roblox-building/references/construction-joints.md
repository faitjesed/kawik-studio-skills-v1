# Construction joints and repeated repairs

Load for arches, stepped seating, annular trim and repeated CSG defects. Use alongside support-and-surfaces.md.

## Diagnose before changing geometry
Identify every object contributing to the visible skin, including obsolete iterations. Distinguish competing faces, actual gaps, exposed slivers, material relief and inaccurate query geometry. Broad overlap checks identify candidates; they do not prove coplanarity. Equally rotated box checks miss angled parts. Inspect the exact location in the user's screenshot.

## Parameterized construction
A passage owns floor, walls, vault, threshold, frame and rear termination. Define clear width, spring height, radius, depth and floor elevation in local coordinates. Changing an opening updates floor coverage and surrounding geometry. Never use a full-height rectangular cut when it would destroy the curved crown.

A stair owns riser height, tread depth, nosing, support and material boundary. An annular strip has width = outer radius - inner radius. Increasing both diameters equally does not increase strip width. Scaling a Union bounding box is not an exact profile edit; regenerate precise profiles. Keep support and cap elevations in one definition, and remove old caps before replacing them.

## CSG and materials
Use Union for pieces that represent one solid. Preserve source solids or a reproducible generator until inspection passes. Remove superseded originals after success. Prefer bounded modules to repeatedly cutting one enormous map Union. Union is not proof of faster rendering, clean textures or usable collision.

Check actual face colors and MaterialVariants after combining materials; do not trust an assumed UsePartColor setting. Keep project-required relief materials. Disabling relief may hide a symptom without proving its cause.

Trim must either form a supported projecting edge or occupy a fitted recess. Identical insert/cutter faces may remain coincident. Choose separation for the scale and camera distance; no universal epsilon fixes every scene. A floating cap is still defective even if flicker disappears.

## Stop repeated patching
After a failed repair inspect the current geometry before retrying. After a second failure at the same joint, preserve a rollback copy and rebuild that local module from named dimensions. Do not continue arbitrary offsets or broad cuts.

Recheck dependencies: opening -> floor/frame; seating -> feet; trim -> support; union -> colors, openings and collision. Preserve user-adjusted transforms and accepted layout. Fixing elevation does not authorize redesigning the arrangement.

## Evidence
Compare the reported close view, a low side view and a changed camera angle. Observe camera movement for flicker: static screenshots cannot prove temporal stability. For a passage, verify clearance and bounded avatar traversal with final position/support. Operation success and part counts do not establish appearance or performance. Report failures and unverified checks explicitly.
