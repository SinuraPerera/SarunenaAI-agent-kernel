import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "ak-py" / "src"))

from sarunena_kernel import _normalize_label, orchestrator


def test_normalize_label_maps_risk_names_to_css_classes():
    assert _normalize_label("Low Risk") == "low"
    assert _normalize_label("Medium Risk") == "medium"
    assert _normalize_label("High Risk") == "high"


def test_orchestrator_analysis_has_expected_product_fields():
    analysis = orchestrator.analyze_query("tomato plants in kandy with yellowing leaves")
    assert analysis["location"] == "Kandy"
    assert analysis["crop"] == "Tomato"
    assert analysis["risk_score"] >= 0
    assert analysis["risk_class"] in {"low", "medium", "high"}
    assert analysis["temp"] is not None
    assert "symptoms" in analysis
