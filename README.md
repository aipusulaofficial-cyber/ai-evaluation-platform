# AI Evaluation Platform

An evaluation execution platform that turns versioned datasets, evaluators and scoring rules into reproducible quality evidence.

## Evaluation flow
```text
Dataset version + rubric
        -> evaluation run
        -> evaluator / judge adapters
        -> deterministic scoring
        -> run metadata + evidence
```

## Project boundaries
- Dataset and rubric versioning define the evaluation input contract.
- Evaluator adapters isolate model/provider dependencies.
- Scoring remains a separate domain concern from transport and infrastructure.
- Run metadata makes results reproducible and reviewable.
- Quality gates can consume evaluation evidence without coupling to provider APIs.

## Failure semantics
Invalid datasets, incompatible evaluator configuration and dependency failures are explicit outcomes. External services are isolated so failure-path tests do not depend on live providers.

## Verification
Contract, edge-case and failure-path tests are part of CI. Security and production validation protect the delivery path.

## Evidence
[docs/PRINCIPAL-ENGINEERING.md](docs/PRINCIPAL-ENGINEERING.md) · [ARCHITECTURE.md](ARCHITECTURE.md) · [ADRs](ADRs/)

The project is designed around reproducible evaluation runs, not ad-hoc prompt experimentation.