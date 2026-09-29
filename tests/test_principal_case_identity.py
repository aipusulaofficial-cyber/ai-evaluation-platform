import pytest

from evaluation_platform import EvaluationCase, EvaluationEngine


def test_duplicate_case_id_is_rejected_before_second_evaluation():
    invoked = []

    def evaluator(case):
        invoked.append(case.case_id)
        return 1.0, True

    engine = EvaluationEngine(evaluator)
    with pytest.raises(ValueError, match="duplicate evaluation case_id"):
        engine.evaluate(
            [
                EvaluationCase("same", "first", "first"),
                EvaluationCase("same", "second", "second"),
            ],
            run_id="run-1",
        )
    assert invoked == ["same"]


def test_distinct_case_ids_remain_valid():
    engine = EvaluationEngine(lambda _: (1.0, True))
    run = engine.evaluate(
        [
            EvaluationCase("a", "first", "first"),
            EvaluationCase("b", "second", "second"),
        ],
        run_id="run-2",
    )
    assert len(run.results) == 2
