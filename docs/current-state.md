# Current State

## Phase
Phase 0 — Project Foundation + Tool Integration (complete)

## Completed
- 0A: Information model agreed.
- 0B: GitHub foundation created and bootstrapped.
- 0C: ChatGPT can read from and write to the repository through a branch and pull-request workflow.
- 0D: Persistent local LearnEco workspace established and Codex verified end-to-end against the real repository.
  - Local repository path: `C:\Projects\LearnEco`
  - Local Git can communicate with `origin` at `MrNobody09/LearnEco`.
  - Codex opened the real local repository, read `AGENTS.md` and `docs/current-state.md`, created a controlled test branch, committed one test file, and pushed it to GitHub.
  - ChatGPT independently verified the pushed commit from GitHub.
- 0E: Persistent Codex context model finalized.
  - `AGENTS.md` now defines required startup reads, the repository context map, conditional-reading behaviour, conflict/precedence rules, local workspace expectations, and change/workflow rules.
  - Fresh Codex sessions are expected to recover project context from the repository rather than from chat history or prior session memory.
- 0F: Documentation/update rules finalized.
  - `docs/documentation-rules.md` defines which artifact is authoritative for each change type, ownership between ChatGPT and Codex, ADR/current-state rules, and when documentation updates are unnecessary.
  - `AGENTS.md` points Codex to these rules when work may materially change project truth or status.
- 0G: Discussion → decision → task → implementation workflow finalized.
  - `docs/workflow.md` defines how discussions become approved repository truth, when GitHub Issues are created, issue readiness, bounded Codex tasks, branch/PR workflow, review, and completion/cleanup.
  - `AGENTS.md` points Codex to the workflow for tracked implementation work and project workflow changes.
- 0H: End-to-end operating-model test completed successfully.
  - GitHub Issue #6 defined a bounded repository health-check task with clear scope, acceptance criteria, relevant context, and constraints.
  - Codex implemented the task from the persistent local repository on a short-lived branch, added tests, ran checks, pushed the branch, and opened PR #7.
  - ChatGPT independently reviewed PR #7 against Issue #6 and the repository rules before merging it.
  - PR #7 merged successfully and automatically closed Issue #6.
  - The test proved the agreed ChatGPT → GitHub → Codex → GitHub → ChatGPT workflow without relying on prior Codex chat memory.
- GitHub repository created as `MrNobody09/LearnEco`.
- Repository is public.
- Default branch is `main`.

## In progress
- None.

## Not started
- Phase 1: Define LearnEco product scope.

## Current constraints
- Repository is public; secrets, authentication material, private learning content, cookies, tokens, and session files must never be committed.
- GitHub is the project system of record for approved requirements, decisions, architecture, status, code, and implementation work.
- Chat is for exploration and discussion; finalized project truth must be persisted in the repository.
- Codex must operate from the persistent local repository at `C:\Projects\LearnEco`; GitHub API access alone is not equivalent to a valid local development workspace.
- Codex must use repository documentation as authoritative context and surface material conflicts instead of resolving them by guesswork.
- Documentation updates must follow `docs/documentation-rules.md`, using the smallest authoritative artifact and avoiding duplicate project truth.
- Tracked work and implementation flow must follow `docs/workflow.md`, with bounded tasks, short-lived branches, pull-request review, and explicit completion.

## Next approved step
Begin Phase 1 by defining LearnEco product scope before creating product requirements, architecture, or implementation work.
