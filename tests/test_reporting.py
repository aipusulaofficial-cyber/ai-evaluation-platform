from evaluation_platform import EvaluationCase, EvaluationEngine, summarize_run, write_report


def test_summary_contains_reproducible_metrics(tmp_path):
    engine = EvaluationEngine(
        lambda case: (1.0 if case.input == case.expected else 0.0, case.input == case.expected),
        evaluator_name="exact-match",
    )
    run = engine.evaluate(
        [
            EvaluationCase("case-1", "hello", "hello"),
            EvaluationCase("case-2", "bye", "hello"),
        ],
        run_id="ci-evidence-1",
    )

    report = summarize_run(run)

    assert report["run_id"] == "ci-evidence-1"
    assert report["case_count"] == 2
    assert report["pass_count"] == 1
    assert report["pass_rate"] == 0.5
    assert report["mean_score"] == 0.5
    assert report["min_score"] == 0.0


def test_write_report_creates_machine_readable_json(tmp_path):
    engine = EvaluationEngine(lambda _: (1.0, True), evaluator_name="deterministic")
    run = engine.evaluate([EvaluationCase("case-1", "x", "x")], run_id="json-1")
    destination = tmp_path / "evaluation-report.json"

    report = write_report(run, destination)

    assert destination.exists()
    assert destination.read_text(encoding="utf-8").startswith("{")
    assert report["case_count"] == 1
    assert report["pass_rate"] == 1.0
