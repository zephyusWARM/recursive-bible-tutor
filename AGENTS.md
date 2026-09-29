# Agent Instructions

When modifying this repository:

- Keep `SKILL.md` focused enough to load as the skill entrypoint.
- Put detailed domain-specific teaching protocols under `references/` and link them from `SKILL.md`.
- Preserve the core invariant: mastery is evidence-based, not confidence-based.
- Prefer tests/evals that detect passive-explanation failure modes.
- Do not add a teaching rule merely because it sounds pedagogically sophisticated; tie it to a concrete failure mode.
- Keep scripts dependency-free unless a dependency clearly earns its complexity.
