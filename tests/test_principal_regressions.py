import pytest

from evaluation_platform import EvaluationCase, EvaluationEngine


def test_duplicate_case_ids_rejected_before_second_evaluation():
    calls = []

    def evaluator(case):
        calls.append(case.case_id)
        return 1.0, True

    engine = EvaluationEngine(evaluator)
    cases = [
        EvaluationCase("same", "question", "answer"),
        EvaluationCase("same", "other", "answer"),
    ]
    with pytest.raises(ValueError, match="duplicate"):
        engine.evaluate(cases, run_id="duplicate-test")
    assert calls == ["same"]
