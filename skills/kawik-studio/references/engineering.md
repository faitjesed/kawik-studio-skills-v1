# Luau and feature implementation

## Source and ownership

Inspect existing code and interfaces before creating an alternative system. Determine whether Studio, repository files, or a hybrid workflow owns each edit. Do not introduce Rojo, packages, an ECS, or a service framework simply because a template uses them.

Give each behavior a clear owner. The server decides authoritative progression, inventory, damage, rewards, purchases, and saves; the client handles presentation, input, camera, and suitable prediction. Shared modules contain contracts and non-secret configuration, not authoritative client-controlled state.

Use the smallest maintainable module shape. Separate code when it has distinct ownership, lifecycle, authority, persistence, or independent testing needs. Avoid giant unrelated scripts as well as gratuitous one-function services and initialization ceremonies.

## Implementation

Follow project conventions and use strict types where they clarify interfaces without creating an unrelated migration. Handle Luau's actual semantics: one-based sequences, nil gaps, only false/nil being falsy, explicit cleanup, and scheduled work with a clear lifetime.

For remotes, define the accepted inputs, server-side validation, ownership/distance/state checks, and abuse controls. Never trust client-reported eligibility, prices, damage, balances, or reward amounts. Persistence and purchase changes should use the installed domain skills when available and current official documentation where API behavior is uncertain.

Preserve failure semantics. A failed operation is not the same as a successful empty result. Bound waiting/retrying according to the actual operation and its idempotency. Disconnect connections and destroy temporary instances when their owner ends.

## Verification

Match checks to the behavior: pure-logic tests for nontrivial rules; Studio runtime tests for engine behavior; multiple clients for actual replication and concurrency claims. Keep an existing test framework when suitable. Verify current tool/library status before adding dependencies rather than installing one by recognition alone.

Run the changed path, including meaningful failure/recovery cases. A small reversible visual adjustment does not require a new test framework. A single-player test does not establish multiplayer economy correctness. Report limitations plainly.

Do not expand a narrow task into monetization, analytics, localization, live operations, release automation, or a general hardening project. Apply those workflows when requested or needed to make the requested feature correct. Keep the final response centered on the result and useful evidence.
