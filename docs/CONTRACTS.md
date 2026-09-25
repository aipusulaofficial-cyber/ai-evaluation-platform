# Contracts

This repository currently documents the contract boundary for dataset → evaluator → regression gate → scorecard; it does not claim a production runtime that is not present.

- API contract: future executable interface.
- Domain contract: invariants and decision semantics.
- Provider/tool contract: adapter capability, timeout/error taxonomy and normalized result.
- Event contract: versioned envelope where asynchronous execution is introduced.
- Configuration contract: bounded, validated configuration.

A runtime implementation must add executable contract tests before these interfaces are presented as shipped behavior.