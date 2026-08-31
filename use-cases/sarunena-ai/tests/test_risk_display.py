import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from farm_specialists.risk_agent import normalize_risk_level


def test_normalize_risk_level_produces_css_safe_class():
    assert normalize_risk_level("🟢 Low Risk") == "low"
    assert normalize_risk_level("🟡 Medium Risk") == "medium"
    assert normalize_risk_level("🔴 High Risk") == "high"
