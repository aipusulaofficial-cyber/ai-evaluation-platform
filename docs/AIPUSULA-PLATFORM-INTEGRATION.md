# AIPusula Platform Integration — AI Quality Gate

This repository is the quality-control component of the AIPusula platform.

## Release contract
`evaluation -> calibration -> independent scoring -> adjudication -> agreement measurement -> threshold gate -> release decision`

Every production candidate MUST carry:
- model + model version
- prompt version
- dataset/version
- evaluator version
- correlation/trace ID
- security policy result
- cost policy result
- quality decision
- immutable audit record

## Required metrics
Track Recall@K, Precision@K, MRR/NDCG where retrieval is evaluated, plus faithfulness, context relevance, answer relevance and citation correctness for RAG/LLM workloads.

For human evaluation use calibration, independent scoring, adjudication and agreement measurement. Do not replace measured results with synthetic claims.

## CI/CD quality gate
A release is blocked when a configured quality threshold is not met, evaluation evidence is missing, or evaluator disagreement exceeds the configured adjudication rule.

## Platform decision contract
Emit a machine-readable decision:
`PASS|FAIL`, reason codes, metric values, evaluator version, timestamp and audit reference.

## Integration points
- secure-ai-gateway: policy decision before evaluation workload
- enterprise-rag-platform: retrieval/citation evidence
- distributed-ai-inference-platform: inference traces and latency
- mlops-model-platform: candidate/promotion lifecycle
- ai-cost-optimization-platform: quality-per-cost signal
- ai-observability-platform: end-to-end trace

## Engineering standard
Code -> Contract -> Test -> Security -> Runtime -> Observability -> Deployment -> Evidence
