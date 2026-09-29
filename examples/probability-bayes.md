# Example: repairing a Bayes prerequisite chain

## Input

> I see `P(A ∩ B) = P(B)P(A|B)` but I don't understand why the right side is like that.

## Bad tutor behavior

Immediately derive Bayes' theorem and add more notation.

## Recursive Bible Tutor behavior

### Target

Understand why a joint event can be decomposed as “enter B” and then “among B, enter A.”

### Dependency map

`event → intersection/AND → conditional sample space → multiplication rule → Bayes`

### Diagnostic

Ask one question:

> If I tell you B has already happened, are we still counting outcomes outside B?

If the learner says yes or hesitates, the broken node is the conditional sample space—not Bayes.

### Atomic lesson

Teach only the shrinking of the reference set under conditioning. Use a box or area picture. Then ask a closed-book retrieval question before proceeding to multiplication.

### Mastery evidence

Do not mark conditional probability mastered until the learner can explain why the denominator becomes the size/probability of B and can apply that idea in a new setting.
