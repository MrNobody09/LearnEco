# LearnEco Agent Instructions

This repository is the system of record for the LearnEco project.

## Workspace
- Operate from the persistent local repository at `C:\Projects\LearnEco` when using Codex locally.
- GitHub API access alone is not equivalent to a valid local development workspace.

## Required startup context
Before making changes:
1. Read `docs/current-state.md`.
2. Read the task prompt or issue.
3. Read only the relevant product, specification, architecture, ADR, source-code, and test files needed for that task.
4. Read `docs/documentation-rules.md` when a task may materially change project truth or status.
5. Do not treat Codex chat history, ChatGPT chat history, or prior session memory as authoritative when repository documentation exists.

## Repository context map
- Current project state: `docs/current-state.md`
- Documentation ownership/update rules: `docs/documentation-rules.md`
- Product requirements and scope: `docs/product.md` when it exists
- Architecture and integration design: `docs/architecture.md` when it exists
- Significant approved decisions and rationale: `docs/decisions/`
- Unresolved project questions: `docs/open-questions.md`
- Implementation truth: source code and tests

Use this map to retrieve context on demand. Do not preload unrelated documentation simply because it exists.

## Conflict and precedence rules
- Approved requirements and ADRs define intended behaviour.
- Architecture documents define the approved technical design.
- `docs/current-state.md` describes the current implementation/project status.
- Source code and tests provide evidence of what is actually implemented.
- GitHub issues/tasks define the current unit of work, not project truth by themselves.
- Chat history is exploratory unless its outcome has been persisted in the repository.
- If these sources disagree materially, do not guess or silently choose one. Surface the conflict before implementation.

## Change rules
- Follow `docs/documentation-rules.md` for documentation ownership and update requirements.
- ChatGPT is the primary owner of approved project truth; Codex is the primary owner of implementation.
- Codex must not silently change product or architecture intent.
- Do not implement behaviour that conflicts with an approved requirement or decision.
- If implementation requires changing an approved decision, surface the conflict before proceeding.
- Never commit credentials, cookies, tokens, session files, private source material, `.env`, or other secrets.
- Make only changes required for the active task; avoid unrelated refactors or cleanup unless explicitly requested.
- Update the smallest authoritative artifact when project truth materially changes; do not duplicate the same truth across multiple files without a clear reason.
- Run applicable tests before considering implementation complete.

## Repository workflow
- Use short-lived branches for meaningful changes.
- Prefer pull requests for meaningful documentation, architecture, and implementation changes.
- Use GitHub Issues for trackable work, bugs, experiments, and technical debt—not as a duplicate of project documentation.
- A fresh Codex session should be able to recover the required project context from the repository without a long context prompt.
