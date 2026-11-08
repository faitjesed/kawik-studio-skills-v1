# Support and surface validation

Use for ground placement, assembly joins, floating objects, and flickering surfaces. Scope checks to the changed geometry and its dependents; intentional floating scenery, cantilevers, buried foundations, and moving objects need their intended support behavior, not forced ground contact.

## Establish support before placement

1. Read current dimensions, transforms, pivot, and intended support geometry from the scene. For a known horizontal floor, its top is center Y plus half its height; this shortcut does not apply to tilted floors or terrain.
2. Select actual support surfaces explicitly. Use a raycast include filter restricted to the intended floor/terrain/foundation, excluding foliage, roofs, the placed model, and helper geometry. Confirm the hit instance and queryability; no hit is UNVERIFIED, not permission to assume Y=0.
3. Define contact points on the geometry that bears weight: trunk base, each table foot, each fence post, foundation corners. Use local points transformed by the current CFrame, or dedicated Attachments. An upright bounding-box bottom is only an initial placement estimate; mesh padding, decoration, and rotations can invalidate it.
4. Place using the measured support and the pivot-to-contact offset. PivotTo places the pivot, not the base. For terrain, sample all meaningful supports; choose longer posts, stepped sections, a foundation, or deliberate terrain preparation when one rigid vertical shift cannot fit them all. Do not silently flatten terrain or tilt the whole assembly to hide gaps.
5. Read back after placement. Record signed contact gap, allowed gap, intended embed depth, and the surface actually hit. Choose tolerances for the asset scale; do not hide visible gaps behind an oversized global tolerance.

Examples: tree = trunk base rather than foliage bounds; fence = every post rather than one ray at the group center; crate = its bottom supports rather than its lid; wall-mounted sign = bracket-to-wall connection rather than ground contact. A support chain must reach a valid foundation or intended attachment, not another accidentally floating object.

## Contact-check example

Illustrative Luau for static geometry and vertical ground contact; configure explicit contact entries from the inspected scene. This reads geometry only. It does not automatically repair models, discover every required contact, or validate wall mounts. A missing entry list must not report PASS.

```luau
local contacts = {
    -- One entry per required contact; never leave this empty for acceptance.
    -- { label = "Fence/Post01", part = post, localPoint = Vector3.new(0, -post.Size.Y/2, 0),
    --   support = ground, embed = 0, tolerance = 0.02, above = 5, below = 10 },
}
local failures, unverified = 0, 0
if #contacts == 0 then
    warn("UNVERIFIED: no support contacts configured")
    return
end
for _, c in ipairs(contacts) do
    if not c.part or not c.part:IsDescendantOf(workspace)
        or not c.support or not c.support:IsDescendantOf(workspace)
        or c.part == c.support or c.support:IsDescendantOf(c.part) then
        unverified += 1
        warn(c.label, "UNVERIFIED: invalid contact/support")
        continue
    end
    local point = c.part.CFrame:PointToWorldSpace(c.localPoint)
    local params = RaycastParams.new()
    params.FilterType = Enum.RaycastFilterType.Include
    params.FilterDescendantsInstances = { c.support }
    local hit = workspace:Raycast(point + Vector3.new(0, c.above, 0),
        Vector3.new(0, -(c.above + c.below), 0), params)
    if not hit then
        unverified += 1
        warn(c.label, "UNVERIFIED: no intended support hit")
        continue
    end
    local gap = point.Y - hit.Position.Y -- positive = air; negative = penetration
    local errorFromTarget = gap + c.embed -- embed is a nonnegative intended depth
    local ok = math.abs(errorFromTarget) <= c.tolerance
    if not ok then failures += 1 end
    print(c.label, ok and "CONTACT OK" or "FAIL", "gap", gap,
        "embed", c.embed, "tolerance", c.tolerance, "surface", hit.Instance:GetFullName())
end
print("Contact failures", failures, "unverified", unverified)
```

Use world-up rays only when vertical support is the intended test. Start above the support top and cast far enough to cover the expected gap/embed range; a ray starting inside a solid is not a reliable surface measurement. For sloped surfaces, also inspect seating across the footprint; for wall mounts use an appropriate direction and signed distance along it. Rendered mesh shape and collision/query shape may differ, so verify visually. CONTACT OK establishes only the configured sampled contact, not full asset acceptance.

## Prevent and repair z-fighting

Inspect overlapping top panels, trim, corners, wall/floor seams, and cloned parts. Coincident or nearly coincident visible faces can compete in depth rendering. A static screenshot suggests a candidate; move the camera to observe flicker. If there are no competing faces, investigate mesh topology, normals, UVs, and appearance before assuming a texture problem.

Repair in this order as appropriate:
- Remove accidental duplicate geometry.
- Correct panel extents and joins so only the intended exterior skin remains visible. Intersecting volumes with hidden internal faces can be valid; do not flag every overlap as an error.
- Give overlays intentional thickness and a visible separation suited to scale and camera distance. A tiny arbitrary offset is not a universal cure, especially at distant views.
- Use Union/CSG when the parts should form one solid. Preserve the source until success is verified, then remove the superseded originals. Inspect resulting silhouette, materials/UVs, collision, and openings. Grouping into a Model does not remove internal or duplicate faces; CanCollide does not fix rendering.

The cutter epsilon used for boolean operations is not a universal spacing tolerance for decorative surfaces. Do not Union an entire map to hide bad joins. Broad-phase overlap reports identify candidates; they do not prove coplanarity or absence of flicker.

## Recheck and accept

- Validate a representative module before repeating it; repair the generator and regenerate affected copies if the defect repeats.
- After changing floor elevation, dimensions, scale, or rotation, recompute contact points and dependent posts, foundations, steps, fixtures, and arrival points.
- Inspect supports from player eye level and a low side view; inspect joins close up and with a moving camera at intended viewing distances. Use an overview for layout, not as sole contact evidence.
- Report checked scope, failed/unverified contacts, intended exceptions, and visual coverage. Fix observed defects before acceptance. If Studio or visual capture is unavailable, distinguish document/code review from observed scene correctness.

## Stepped crowds and CSG supports
A ray may hit a neighboring cap, higher terrace or approximate CSG collision instead of the visible tread. Record its hit and compare with the intended tread definition. Search near the expected elevation rather than casting through the entire structure. Check both feet and their footprint. If supports differ in height, relocate onto a wide tread rather than lifting the character to the highest hit.

Invalidate cached support heights after scaling, cuts or unions. Analytical heights are valid only while actual geometry matches their source definition. Neither a ray nor a formula alone proves visible grounding. Inspect feet from player height.

For crowds, use irregular groups, empty seats and minimum spacing. Repeated angle/row cycles create visible diagonal lines even with jitter. Orient from the actual face axis, not an arbitrary model pivot, and preserve intended poses.
