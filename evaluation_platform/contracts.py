from dataclasses import dataclass
from typing import Mapping, Sequence

@dataclass(frozen=True)
class EvaluationCase:
    case_id: str
    input: str
    expected: str

    def __post_init__(self) -> None:
        if not self.case_id.strip():
            raise ValueError("case_id must not be empty")
        if not self.input.strip():
            raise ValueError("input must not be empty")
        if not self.expected.strip():
            raise ValueError("expected must not be empty")

@dataclass(frozen=True)
class EvaluationResult:
    case_id: str
    score: float
    passed: bool
    evaluator: str
    error_type: str | None = None

    def __post_init__(self) -> None:
        if not 0.0 <= self.score <= 1.0:
            raise ValueError("score must be between 0 and 1")
        if not self.evaluator.strip():
            raise ValueError("evaluator must not be empty")

@dataclass(frozen=True)
class EvaluationRun:
    run_id: str
    results: Sequence[EvaluationResult]
    metadata: Mapping[str, str]

    def __post_init__(self) -> None:
        if not self.run_id.strip():
            raise ValueError("run_id must not be empty")
        if not self.results:
            raise ValueError("results must not be empty")
