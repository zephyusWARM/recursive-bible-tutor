# Learning State Machine

## State files

When persistent file access exists, keep one learning workspace per topic or course.

Recommended files:

- `TOPIC.md` — target, scope, source set, success criterion.
- `KNOWLEDGE_GRAPH.md` — atomic nodes, prerequisites, status.
- `LEARNER_STATE.md` — stable strengths, fragile areas, current node.
- `MISCONCEPTIONS.md` — incorrect generative rules and repairs.
- `REVIEW_QUEUE.md` — due retrieval items.
- `SESSION_LOG.md` — evidence-focused session summaries.

Use templates from `assets/templates/`.

## Concept states

- `NEW` — identified but untested.
- `LEARNING` — currently being built.
- `FRAGILE` — partially understood or scaffold-dependent.
- `MASTERED` — demonstrated retrieval/application/transfer evidence.
- `REVIEW_DUE` — previously strong but scheduled for delayed retrieval.

Status is evidence-based, not confidence-based.

## Evidence records

For each meaningful learner response, record only what changes the learner model:

- concept;
- prompt type;
- learner response summary;
- evidence type: reconstruction/application/discrimination/transfer;
- scaffolding level;
- result;
- misconception revealed or repaired;
- next action.

Do not turn the log into a verbatim transcript.

## Review scheduling

A simple default without a dedicated scheduler:

- first retrieval: later in the same session or next concept;
- second retrieval: next study session;
- third retrieval: several days later;
- then widen intervals when retrieval is successful.

Failed retrieval shortens the next interval and may move MASTERED to FRAGILE.

## Session restart protocol

On `CONTINUE`:

1. read TOPIC, LEARNER_STATE, KNOWLEDGE_GRAPH, MISCONCEPTIONS, REVIEW_QUEUE;
2. do not reteach mastered material by default;
3. check whether a due review should be interleaved;
4. resume at the smallest unresolved prerequisite or current node.
