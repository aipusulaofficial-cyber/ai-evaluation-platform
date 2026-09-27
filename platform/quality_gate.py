"""Deterministic quality release gate."""
from dataclasses import dataclass

@dataclass(frozen=True)
class QualityDecision:
    decision: str
    score: float
    reason: str

def evaluate(score: float, minimum: float = 0.80, evidence: bool = True) -> QualityDecision:
    if not evidence:
        return QualityDecision("DENY", score, "MISSING_EVIDENCE")
    if score < minimum:
        return QualityDecision("DENY", score, "QUALITY_THRESHOLD")
    return QualityDecision("ALLOW", score, "QUALITY_PASS")
