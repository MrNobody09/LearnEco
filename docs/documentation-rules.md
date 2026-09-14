# Documentation Rules

## Core principle
Update the smallest authoritative artifact that represents the change. Do not duplicate the same truth across multiple files unless there is a clear reason.

## Ownership
- ChatGPT is the primary owner of approved project truth: product scope, requirements, architecture, significant decisions, current project state, and open questions.
- Codex is the primary owner of implementation: source code, tests, and code-adjacent documentation.
- Codex must not silently invent or rewrite product or architecture intent. If implementation conflicts with approved project truth, surface the conflict before proceeding.

## What to update
| Change type | Authoritative artifact | Primary owner | Update required when |
| --- | --- | --- | --- |
| Product scope, requirement, non-goal, acceptance criteria | `docs/product.md` | ChatGPT | Approved product truth changes |
| Architecture, integration, auth, deployment, system design | `docs/architecture.md` | ChatGPT | Approved technical design changes |
| Significant decision and rationale | `docs/decisions/ADR-xxx.md` | ChatGPT | Future maintainers/agents may need to understand why a material decision was made |
| Current phase, completed work, active blocker, next approved step | `docs/current-state.md` | ChatGPT primarily; Codex only when its task clearly changes project state | Project status materially changes |
| Important unresolved question | `docs/open-questions.md` | ChatGPT | A material question remains unresolved; remove it once resolved and update the authoritative artifact |
| Code behaviour | Source code and tests | Codex | Implementation changes |
| Bug, technical debt, experiment, trackable work | GitHub Issue | ChatGPT or Codex | Work needs to be tracked but is not itself project truth |
| Small implementation detail | Code/tests only | Codex | No documentation update unless behaviour, design, or project state changes |

## ADR rule
Create an ADR only when the rationale is likely to matter later. Do not create ADRs for routine implementation details, renames, formatting changes, or reversible low-impact choices.

## Current-state rule
Keep `docs/current-state.md` concise. It should answer:
- What phase are we in?
- What has been completed?
- What is in progress?
- What is blocked?
- What is the next approved step?

It is not a project diary or changelog.

## Changes that normally do not require project-doc updates
- Formatting-only changes
- Typo fixes
- Refactors with no behaviour or architecture change
- Internal variable/function renames
- Temporary debugging
- Local environment setup that does not alter the approved workflow
- Implementation details already represented clearly by code/tests

## Final rules
1. One source of truth per type of information.
2. ChatGPT owns approved project truth; Codex owns implementation.
3. Codex never silently changes product or architecture intent.
4. Update project documentation only when project truth materially changes.
5. Do not add duplicate history or logs for their own sake.
