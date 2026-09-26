import pytest

from evaluation_platform import EvaluationCase, EvaluationEngine


def test_evaluates_cases_deterministically():
    engine = EvaluationEngine(
        lambda case: (
            1.0 if case.input == case.expected else 0.0,
            case.input == case.expected,
        )
    )
    run = engine.evaluate(
        [
            EvaluationCase("case-1", "hello", "hello"),
            EvaluationCase("case-2", "bye", "hello"),
        ],
        run_id="run-1",
    )
    assert [result.score for result in run.results] == [1.0, 0.0]
    assert [result.passed for result in run.results] == [True, False]


def test_rejects_invalid_case():
    with pytest.raises(ValueError):
        EvaluationCase("", "input", "expected")


def test_rejects_invalid_score():
    engine = EvaluationEngine(lambda _: (1.5, False))
    with pytest.raises(ValueError):
        engine.evaluate([EvaluationCase("case-1", "x", "y")], run_id="run-1")


def test_rejects_non_boolean_passed():
    engine = EvaluationEngine(lambda _: (1.0, 1))  # type: ignore[arg-type]
    with pytest.raises(ValueError, match="non-boolean"):
        engine.evaluate([EvaluationCase("case-1", "x", "y")], run_id="run-1")


def test_rejects_empty_run():
    engine = EvaluationEngine(lambda _: (1.0, True))
    with pytest.raises(ValueError):
        engine.evaluate([], run_id="run-1")


def test_bounds_untrusted_case_stream():
    engine = EvaluationEngine(lambda _: (1.0, True), max_cases=2)
    cases = (EvaluationCase(f"case-{i}", "x", "y") for i in range(3))
    with pytest.raises(ValueError, match="max_cases=2"):
        engine.evaluate(cases, run_id="run-1")


def test_rejects_invalid_max_cases():
    with pytest.raises(ValueError, match="max_cases"):
        EvaluationEngine(lambda _: (1.0, True), max_cases=0)
