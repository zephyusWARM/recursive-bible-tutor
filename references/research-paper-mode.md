# Research / Paper Mode

## Phase 1 — Problem formulation first

Before discussing the method, pin down:

- research question;
- object / population / data-generating unit;
- input and output;
- training-time versus inference-time setting;
- public versus private information when relevant;
- neighboring relation / adjacency when relevant;
- threat model;
- release surface;
- guarantee or objective;
- assumptions;
- baseline and comparison class.

If any of these are ambiguous, label the ambiguity instead of silently choosing one.

## Phase 2 — Claim graph

Separate:

- motivation claim;
- theoretical claim;
- algorithmic claim;
- empirical claim;
- scope/boundary claim.

For each, identify what evidence would be required.

## Phase 3 — Method reconstruction

Teach the method as a dependency chain. Do not follow notation blindly. Translate each object into its role in the system.

## Phase 4 — Proof obligations

For theoretical work, list what must be shown before reading the proof details. This turns the proof into a sequence of questions rather than symbol copying.

## Phase 5 — Experiments

Identify:

- dataset / population;
- split / evaluation protocol;
- metrics;
- baselines;
- ablations;
- hyperparameter dependence;
- whether results actually test the stated claim.

## Phase 6 — Red-team

Ask:

- What would make the main claim false or much weaker?
- Is there leakage between train/test or private/public objects?
- Does the implementation preserve the mathematical assumptions?
- Is the unit of privacy/evaluation the same as the unit in the theorem?
- Are conclusions broader than the evaluated population?
