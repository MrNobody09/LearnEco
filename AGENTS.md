# LearnEco Agent Instructions

This repository is the system of record for the LearnEco project.

## Before making changes
1. Read `docs/current-state.md`.
2. Read the relevant project/specification/architecture documents if they exist.
3. Read applicable ADRs under `docs/decisions/` if they exist.
4. Do not treat chat history as the source of truth when repository documentation exists.

## Change rules
- Do not implement behavior that conflicts with an approved requirement or decision.
- If implementation requires changing an approved decision, surface the conflict before proceeding.
- Never commit credentials, cookies, tokens, session files, private source material, or other secrets.
- Keep documentation synchronized when a change materially alters project state or an approved decision.
- Run applicable tests before considering implementation complete.

## Repository workflow
- Use short-lived branches for meaningful changes.
- Prefer pull requests for meaningful documentation, architecture, and implementation changes.
- Use GitHub Issues for trackable work, bugs, experiments, and technical debt—not as a duplicate of project documentation.
