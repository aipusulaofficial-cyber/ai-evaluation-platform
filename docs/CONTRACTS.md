# Contracts

The executable boundary is now implemented in `evaluation_platform/contracts.py` and exercised by `tests/test_engine.py`.

## Domain contract
- Case IDs and required inputs are non-empty.
- Scores are bounded to [0, 1].
- A run must have a non-empty run ID and at least one result.
- Evaluator identity is explicit.

## Failure contract
Invalid domain input and invalid evaluator output fail closed with `ValueError`. No implicit retry is performed by the core engine.

## Extension contract
Provider/tool adapters must return a normalized `(score, passed)` result and remain responsible for their own timeout/retry policy.
