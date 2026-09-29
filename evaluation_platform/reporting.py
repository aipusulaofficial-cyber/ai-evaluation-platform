from __future__ import annotations

import json
from dataclasses import asdict
from pathlib import Path

from .contracts import EvaluationRun


def summarize_run(run: EvaluationRun) -> dict[str, object]:
    scores = [result.score for result in run.results]
    passed = sum(result.passed for result in run.results)
    return {
        "run_id": run.run_id,
        "evaluator": run.metadata.get("evaluator", "unknown"),
        "case_count": len(run.results),
        "pass_count": passed,
        "pass_rate": passed / len(run.results),
        "mean_score": sum(scores) / len(scores),
        "min_score": min(scores),
        "results": [asdict(result) for result in run.results],
        "metadata": dict(run.metadata),
    }


def write_report(run: EvaluationRun, path: str | Path) -> dict[str, object]:
    report = summarize_run(run)
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return report
