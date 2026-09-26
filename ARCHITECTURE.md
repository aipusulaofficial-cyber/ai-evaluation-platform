# Architecture

## Purpose
A deterministic evaluation engine for versioned AI evaluation cases.

## Boundary
The core runtime owns domain validation, evaluator invocation and reproducible result assembly. External model/provider adapters are outside the core and must return normalized scores.

## Data flow
EvaluationCase → Evaluator adapter → bounded score → EvaluationResult → EvaluationRun.

## Failure semantics
Invalid inputs and invalid evaluator outputs fail closed. The core engine performs no hidden retries or network calls.

## Non-functional requirements
Deterministic, auditable, bounded and testable. Provider-specific timeouts/retries remain at the adapter boundary.
