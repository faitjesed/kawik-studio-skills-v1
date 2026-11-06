# Modeling and environment quality

## Decide before generating

Establish the intended camera distance, player scale, art direction, footprint, repeated-use count, collision needs, and target device context. Infer routine reversible choices from the request and scene. Ask when a missing choice materially changes the asset. A budget is a design constraint tied to the use case, not an arbitrary universal triangle limit.

Inspect reusable project assets first. Search available asset tools for suitable common props before commissioning replacements, following the tool's ownership and price rules. Inspect candidate hierarchy, scripts, packages, dependencies, scale, and appearance before accepting it. Never run imported code merely to discover what it does.

Choose the technique for the shape:

- Native Parts, wedges, cylinders, and shallow CSG for blocky architecture, floors, stairs, frames, trim, and predictable collision.
- Existing or generated meshes for shapes whose silhouette suffers as a pile of boxes: statues, shaped foliage, irregular cliffs, ornament, or hero props.
- Blender when actual mesh editing, controlled topology, reusable custom silhouettes, UV work, or mesh optimization materially helps and the tool/import path exists.
- Modular pieces for repeated buildings and environments. A monolithic map mesh makes local fixes, collision review, and reuse harder.

Generation produces a candidate, not acceptance evidence. Wait for its real completion before dependent placement; verify insertion even after a tool timeout. Keep provenance for externally sourced assets and preserve license notices for adapted material.

## Prototype one representative module

Build and inspect one bay, shop, gate, rock cluster, or room before repeating it. Derive components from named dimensions and anchor transforms. Check the joins and silhouette at player height. Correct the generator when a repeated defect appears; do not multiply a bad prototype and patch each copy independently.

For settlements, place activity approaches and sightlines before decorative density. For combat rooms, preserve a clear navigation core and put most biome identity at the perimeter and ceiling. Different biomes need distinctive forms and prop arrangements, not just new colors. Explicitly floating magic should be distinguishable from accidental unsupported construction.

## Grounding and assembly

Use the actual support surface: a filtered raycast for uneven ground, or a read-back floor top for a known planar foundation. Do not place on a roof or foliage accidentally because the raycast included every descendant.

For a model, inspect `GetBoundingBox()` and the pivot before `PivotTo()`. An upright bounding-box bottom is a useful first pass; it is not reliable proof for a tilted mesh, an irregular trunk, dangling decoration, or a model whose visual bounds differ from its collision. Use dedicated contact points, the trunk/foot/foundation geometry, additional rays, and visual inspection where needed. Record intended rock embed depth rather than treating all intersections as errors.

For a changed platform height, update foundation depth, steps, landings, fixtures, triggers, and arrival points together. Steps must meet the route at both ends, with no unsupported slab hiding a gap. If a no-jump route is intended, verify it with jumping disabled.

Walls must meet foundations and roof supports. Doors and arches need clear body and camera space. Signboards, shelves, lanterns, banners, and weapons require a logical mount or support. Check roof eaves, corners, wall seams, and sign faces from both sides; avoid coincident faces and overlapping labels.

## Blender and import

Work in a named, isolated collection when preserving another scene. Inspect dimensions and axis conventions; test a small representative export before an entire kit. Apply transforms as appropriate for the asset and rig, inspect normals, remove duplicate/loose geometry, and retain intentional open boundaries. Do not treat every non-manifold edge as a defect in every modeling technique.

Use a suitable origin and coherent object names. Share materials and textures where appearance permits; use atlases only when they improve this asset family. Do not decimate uniformly until the silhouette or animation deforms. Review UVs and texel density only when textures require them.

After importing, inspect the real Studio result: scale, pivot, orientation, mesh/texture dependencies, material appearance, anchoring, bounding box, and collision. A successful file export does not prove a successful import. If an asset does not render, inspect the reported loading/permission error before rebuilding it.

Prefer simple collision proxies for decorative or intricate geometry when detailed collision adds no gameplay value. A visible arch's proxy must leave its opening usable; a single box around the whole arch does not. Use LODs or renderer fidelity choices where supported and justified by repeated-use count and measured cost.

## Validate what matters

Combine structural queries, targeted collision/support checks, and visual views. Inspect representative assets close up, joins in motion, player eye level, a third-person view, and an overview. Audit boundary gaps and all meaningful route connections, including returns.

Fix observed defects before declaring the section done. For large scenes, report which sections and paths were actually sampled. A clean bounding-box report cannot establish that every irregular model is grounded. Distinguish observed rendering counts from FPS measurements and device benchmarks.
