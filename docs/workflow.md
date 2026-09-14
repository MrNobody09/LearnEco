# Operating Workflow

## Core principle
Discussion happens in ChatGPT. Approved project truth is persisted in GitHub. Implementation happens in Codex. Review and completion are verified through GitHub and ChatGPT.

## End-to-end flow
1. Discuss and explore in ChatGPT.
2. Reach an explicit decision.
3. Persist the approved outcome in the smallest authoritative repository artifact.
4. Create a GitHub Issue when implementation or other trackable work is needed.
5. Hand Codex a bounded task with clear scope, acceptance criteria, and relevant context.
6. Codex works on a short-lived branch, implements the task, runs applicable tests, and pushes the branch.
7. Open a pull request.
8. Review the diff against the issue, requirements, architecture, and relevant ADRs.
9. If changes are needed, send focused corrections back to Codex; otherwise merge.
10. Close the work item and update project state only when materially required.
11. Sync the local repository back to `main` and clean up completed branches when appropriate.

## Discussion states
Not every discussion becomes project truth.

- Idea: remains in chat unless adopted.
- Agreed decision: must be persisted in the relevant authoritative repository artifact.
- Implementable work: should become a GitHub Issue or another explicit task when tracking is useful.

## Classifying approved outcomes
When a discussion is approved, classify it before creating work:
- Product truth → `docs/product.md`
- Architecture truth → `docs/architecture.md`
- Significant rationale → ADR under `docs/decisions/`
- Important unresolved question → `docs/open-questions.md`
- Project status change → `docs/current-state.md`
- Implementation work → GitHub Issue
- No lasting consequence → leave it in chat

Follow `docs/documentation-rules.md` for ownership and update requirements.

## GitHub Issue role
GitHub Issues represent work, not the authoritative definition of project truth.

A non-trivial implementation Issue should contain enough information for Codex to act safely:
- Goal
- Scope
- Out of scope where useful
- Acceptance criteria
- Relevant repository documents
- Known constraints

Do not duplicate full product or architecture documents inside Issues. Link to the authoritative repository context instead.

## Issue readiness
An implementation Issue is ready for Codex when the goal, scope, acceptance criteria, relevant context, and material constraints are clear enough that Codex does not need to invent product or architecture intent.

If the task is not ready, resolve the missing context before implementation.

## Codex task rule
Codex tasks must be bounded. Prefer instructions such as:

`Implement GitHub Issue #N. Follow AGENTS.md and the linked repository context. Do not make unrelated changes.`

Do not hand Codex broad requests that require it to independently define scope, product behaviour, or architecture.

If Codex discovers a material conflict or missing decision, it must surface the issue instead of silently resolving it.

## Branch and pull-request workflow
For meaningful work:
1. Start from an up-to-date `main`.
2. Create a short-lived branch such as `feature/...`, `fix/...`, `docs/...`, or another clear task-specific name.
3. Make only task-relevant changes.
4. Run applicable tests/checks.
5. Commit with a clear message.
6. Push the branch.
7. Open a pull request to `main`.

Meaningful implementation and documentation changes should not be made directly on `main`.

## Review rule
Before merge, review the pull request against the relevant sources of truth:
- Issue/task acceptance criteria
- Product requirements
- Architecture
- Relevant ADRs
- Applicable tests

ChatGPT should normally perform the repository-level review so the user is not expected to manually inspect source code.

If the implementation does not match the approved context, request a focused correction rather than silently changing project truth to match the code.

## Completion rule
After a successful merge:
- Close the GitHub Issue when applicable.
- Update `docs/current-state.md` only when project status materially changes.
- Update product/architecture/ADR documentation only when approved project truth changed.
- Sync the persistent local repository with `main`.
- Delete completed branches when appropriate.

A merged pull request does not automatically require updates to every project document.

## Work types
| Work type | Example | Issue normally required? | PR normally required? |
| --- | --- | --- | --- |
| Decision/documentation | Choose an auth approach | Not always | Usually |
| Implementation | Add NotebookLM source listing | Yes | Yes |
| Trivial maintenance | Typo or formatting-only fix | No | Optional |

Use judgement rather than creating process overhead for insignificant changes.

## Role boundaries
- ChatGPT decides what should happen and maintains approved project truth.
- GitHub records what is true and what work is tracked.
- Codex changes implementation and tests within approved boundaries.
- Codex may surface technical findings and propose alternatives, but it does not independently redefine product scope, architecture, or acceptance criteria.
