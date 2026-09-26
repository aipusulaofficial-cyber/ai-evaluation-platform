from collections.abc import Callable, Iterable
from .contracts import EvaluationCase, EvaluationResult, EvaluationRun

Evaluator = Callable[[EvaluationCase], tuple[float, bool]]

class EvaluationEngine:
    def __init__(self, evaluator: Evaluator, *, evaluator_name: str = "default") -> None:
        if not evaluator_name.strip():
            raise ValueError("evaluator_name must not be empty")
        self._evaluator = evaluator
        self._evaluator_name = evaluator_name

    def evaluate(self, cases: Iterable[EvaluationCase], *, run_id: str) -> EvaluationRun:
        if not run_id.strip():
            raise ValueError("run_id must not be empty")
        results: list[EvaluationResult] = []
        for case in cases:
            score, passed = self._evaluator(case)
            if not 0.0 <= score <= 1.0:
                raise ValueError(f"evaluator returned invalid score for {case.case_id}")
            results.append(
                EvaluationResult(
                    case_id=case.case_id,
                    score=score,
                    passed=passed,
                    evaluator=self._evaluator_name,
                )
            )
        if not results:
            raise ValueError("evaluation run requires at least one case")
        return EvaluationRun(run_id=run_id, results=tuple(results), metadata={"evaluator": self._evaluator_name})
