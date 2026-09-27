from platform.quality_gate import evaluate

def test_quality_gate():
    assert evaluate(0.90).decision == "ALLOW"
    assert evaluate(0.70).decision == "DENY"
    assert evaluate(0.90, evidence=False).decision == "DENY"
