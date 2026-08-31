"""
SaruNena AI - Agent Kernel-based agricultural intelligence use case.

This module keeps the implementation aligned with the real Agent Kernel framework
patterns used by the repository: Agent objects, Runtime, Session, AgentService,
and OpenAIModule registration.
"""

import json
import logging
import re
from typing import Any

from tools import (
    assess_disease_risk,
    calculate_farm_risk,
    get_location_context,
    get_market_snapshot,
    get_weather_snapshot,
    remember_farmer_context,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def _normalize_label(value: str) -> str:
    """Convert risk labels like '🟢 Low Risk' into CSS-safe classes."""
    cleaned = (value or "medium").lower()
    for emoji in ["🟢", "🟡", "🔴", "✅", "⚠️", "🚨"]:
        cleaned = cleaned.replace(emoji, "")
    cleaned = re.sub(r"[^a-z\s]", "", cleaned)
    cleaned = " ".join(cleaned.split())

    if "low" in cleaned:
        return "low"
    if "high" in cleaned:
        return "high"
    if "medium" in cleaned or "moderate" in cleaned:
        return "medium"
    return "medium"


def _parse_risk_report(report: str) -> tuple[int, str]:
    """Extract score and display label from calculate_farm_risk output."""
    score = 50
    level = "Medium Risk"

    for line in report.splitlines():
        if "Overall Risk Score:" in line:
            match = re.search(r"(\d+)/100", line)
            if match:
                score = int(match.group(1))
        if line.strip().startswith("Risk Level:"):
            raw = line.split(":", 1)[1].strip()
            normalized = raw.lower()
            if "high" in normalized:
                level = "High Risk"
            elif "medium" in normalized or "moderate" in normalized:
                level = "Medium Risk"
            elif "low" in normalized:
                level = "Low Risk"
            else:
                level = raw.title()

    return score, level


def _parse_weather_metrics(weather: str) -> tuple[float, float]:
    """Extract temperature and rainfall from weather tool output."""
    temp_match = re.search(r"Current:\s*([\d.]+)\s*°C", weather)
    rain_match = re.search(r"Rain:\s*([\d.]+)\s*mm", weather)
    temp = float(temp_match.group(1)) if temp_match else 27.0
    rain = float(rain_match.group(1)) if rain_match else 0.0
    return temp, rain


def _build_recommendation(crop: str, location: str, score: int, symptoms: str) -> str:
    """Generate a practical recommendation from risk score and context."""
    crop_title = crop.title()
    location_title = location.title()

    if score >= 70:
        return (
            f"URGENT: Inspect {crop_title} in {location_title} today. "
            f"Improve drainage, remove affected plant material, and delay spraying until fields dry. "
            f"Symptoms reported ({symptoms}) need daily monitoring."
        )
    if score >= 50:
        return (
            f"{crop_title} in {location_title} needs a field check now. "
            f"Prioritize drainage, remove severely affected leaves, and review irrigation before the next wet spell."
        )
    if score >= 30:
        return (
            f"{crop_title} in {location_title} looks manageable. "
            f"Continue regular monitoring, maintain spacing for airflow, and apply preventive care if humidity stays high."
        )
    return (
        f"Conditions in {location_title} are favorable for {crop_title}. "
        f"Proceed with normal field work and keep routine monitoring."
    )


def _build_insight(crop: str, score: int, level: str, rain: float, symptoms: str) -> str:
    """Generate a concise farming insight from analysis signals."""
    crop_title = crop.title()
    if rain > 10:
        weather_note = "Heavy recent rainfall increases moisture-related stress"
    elif rain > 0:
        weather_note = "Recent rainfall is adding moisture stress"
    else:
        weather_note = "Current weather is relatively dry"

    return (
        f"Based on {weather_note.lower()} and reported symptoms ({symptoms}), "
        f"{crop_title} is at {level.lower()} ({score}/100). "
        f"The risk is driven by local weather exposure and crop stress patterns."
    )


class SaruNenaOrchestrator:
    """Minimal but real Agent Kernel orchestrator for the SaruNena farming assistant."""

    def __init__(self):
        self.runtime = None
        self.agent_service = None
        self._agents_initialized = False

    def initialize(self):
        """Register all agents with the current Agent Kernel runtime."""
        if self._agents_initialized:
            return None

        try:
            from agentkernel.core import AgentService, Runtime
            from agentkernel.openai import OpenAIModule, OpenAIToolBuilder
            from agents import Agent as OpenAIAgent
        except ImportError as exc:
            logger.warning(
                "Agent Kernel OpenAI module unavailable; deterministic analysis still works: %s",
                exc,
            )
            return None

        logger.info("Initializing SaruNena multi-agent system")
        self.runtime = Runtime.current()
        module = OpenAIModule(self._create_agents(OpenAIAgent, OpenAIToolBuilder))
        self.agent_service = AgentService()
        self.agent_service.select(name="triage", session_id="sarunena_default")
        self._agents_initialized = True
        return module

    def _create_agents(self, openai_agent_cls, tool_builder) -> list:
        """Create the specialized SaruNena agents and triage router."""

        memory_agent = openai_agent_cls(
            name="memory",
            handoff_description="Stores farmer session context and remembers previous crop/location context.",
            instructions=(
                "You are the Memory Agent for SaruNena. Remember crop, location, symptoms, and previous advice "
                "for each farmer. Use session context when it is helpful and keep the farmer record concise."
            ),
            tools=tool_builder.bind([remember_farmer_context]),
        )

        location_agent = openai_agent_cls(
            name="location",
            handoff_description="Detects location and local agriculture context for Sri Lankan farmers.",
            instructions=(
                "You are the Location Agent. Resolve the farmer's place and agricultural conditions. "
                "Support Sri Lankan cities and villages. Keep responses short and practical."
            ),
            tools=tool_builder.bind([get_location_context]),
        )

        weather_agent = openai_agent_cls(
            name="weather",
            handoff_description="Fetches weather, rainfall, and climate context relevant to crop health.",
            instructions=(
                "You are the Weather Agent. Use the weather tool to get rainfall and temperature conditions, "
                "then explain how they affect crop health and field work in straightforward farmer language."
            ),
            tools=tool_builder.bind([get_weather_snapshot]),
        )

        disease_agent = openai_agent_cls(
            name="disease",
            handoff_description="Assesses crop disease likelihood using symptoms and local weather signals.",
            instructions=(
                "You are the Disease Agent. Use visible symptoms and weather conditions to assess likely crop problems. "
                "Be clear that diagnosis is uncertain unless confirmed by a field inspection."
            ),
            tools=tool_builder.bind([assess_disease_risk]),
        )

        market_agent = openai_agent_cls(
            name="market",
            handoff_description="Returns relevant crop market context and pricing trends for Sri Lanka.",
            instructions=(
                "You are the Market Agent. Provide clear, simple market context for the crop, using demo market values "
                "when live market API access is not available and clearly labeling that data as demo or indicative."
            ),
            tools=tool_builder.bind([get_market_snapshot]),
        )

        risk_agent = openai_agent_cls(
            name="risk",
            handoff_description="Combines weather, disease, and market signals to identify probable farm risk.",
            instructions=(
                "You are the Risk Agent. Combine weather, disease, and market context into a concise risk assessment. "
                "Return a score, a risk level, and a short explanation."
            ),
            tools=tool_builder.bind([calculate_farm_risk]),
        )

        recommendation_agent = openai_agent_cls(
            name="recommendation",
            handoff_description="Synthesizes the data into a practical next-step recommendation for farmers.",
            instructions=(
                "You are the Recommendation Agent. Turn all the inputs into a short, useful action plan for the farmer, "
                "explaining why it was recommended in farmer-friendly language."
            ),
        )

        triage_agent = openai_agent_cls(
            name="triage",
            instructions=(
                "You are the Triage Agent for SaruNena. Understand the farmer's crop, location, symptoms, and concern, "
                "route to the most relevant specialists, and produce a cohesive answer in simple Sri Lankan farmer language."
            ),
            handoffs=[
                memory_agent,
                location_agent,
                weather_agent,
                disease_agent,
                market_agent,
                risk_agent,
                recommendation_agent,
            ],
        )

        return [
            triage_agent,
            memory_agent,
            location_agent,
            weather_agent,
            disease_agent,
            market_agent,
            risk_agent,
            recommendation_agent,
        ]

    def analyze_query(self, user_input: str) -> dict[str, Any]:
        """Create an analysis result using live weather data and deterministic risk scoring."""
        text = (user_input or "").strip()
        location = self._extract_location(text)
        crop = self._extract_crop(text)
        symptoms = self._extract_symptoms(text)

        weather = get_weather_snapshot(location, crop)
        disease = assess_disease_risk(crop, symptoms, weather)
        market = get_market_snapshot(crop)
        risk_report = calculate_farm_risk(weather, disease, market)

        score, level = _parse_risk_report(risk_report)
        temp, rain = _parse_weather_metrics(weather)
        risk_class = _normalize_label(level)
        health_bar = "█" * max(1, score // 10) + "░" * max(0, 10 - (score // 10))
        recommendation = _build_recommendation(crop, location, score, symptoms)
        insight = _build_insight(crop, score, level, rain, symptoms)

        return {
            "location": location.title(),
            "temp": round(temp, 1),
            "rain": round(rain, 1),
            "disease": disease,
            "market": market,
            "risk_score": score,
            "risk_level": level,
            "risk_class": risk_class,
            "recommendation": recommendation,
            "insight": insight,
            "health_bar": health_bar,
            "crop": crop.title(),
            "symptoms": symptoms,
            "weather_detail": weather,
            "risk_detail": risk_report,
        }

    def process_farmer_query(self, farmer_id: str, user_input: str) -> str:
        """Process a query through the Agent Kernel-based orchestration flow."""
        context = self.analyze_query(user_input)

        if not self._agents_initialized:
            self.initialize()

        if self.runtime is None or self.agent_service is None:
            return (
                f"{context['location']} • {context['crop']}\n"
                f"Risk: {context['risk_level']} ({context['risk_score']}/100)\n"
                f"Recommendation: {context['recommendation']}"
            )

        from agentkernel.core import AgentService, Session

        session = Session(id=farmer_id)
        session.set("latest_context", json.dumps(context, ensure_ascii=False))

        agent = self.runtime.agents().get("triage")
        if agent is not None:
            try:
                service = AgentService()
                service.select(session_id=farmer_id, name="triage")
                prompt = (
                    f"Farmer question: {user_input}\n"
                    f"Agricultural context: {json.dumps(context, ensure_ascii=False)}"
                )
                return service.run(prompt)
            except Exception as exc:  # pragma: no cover - fallback for local/demo environments
                logger.warning("Agent runtime unavailable; falling back to deterministic farm summary: %s", exc)

        return (
            f"{context['location']} • {context['crop']}\n"
            f"Risk: {context['risk_level']} ({context['risk_score']}/100)\n"
            f"Recommendation: {context['recommendation']}"
        )

    @staticmethod
    def _extract_location(text: str) -> str:
        for place in [
            "kandy",
            "colombo",
            "galle",
            "jaffna",
            "nuwara eliya",
            "badulla",
            "kurunegala",
            "anuradhapura",
        ]:
            if place in text.lower():
                return place.title()
        return "Kandy"

    @staticmethod
    def _extract_crop(text: str) -> str:
        for crop in ["tomato", "rice", "chili", "potato", "onion", "carrot", "banana", "coconut", "tea"]:
            if crop in text.lower():
                return crop
        return "tomato"

    @staticmethod
    def _extract_symptoms(text: str) -> str:
        symptoms = [
            "yellow spots",
            "wilting",
            "leaf curl",
            "blight",
            "yellowing leaves",
            "wet field",
            "mold",
            "spots",
        ]
        found = [s for s in symptoms if s in text.lower()]
        return found[0] if found else "general crop stress"


orchestrator = SaruNenaOrchestrator()


if __name__ == "__main__":
    orchestrator.initialize()
    print(
        orchestrator.process_farmer_query(
            "demo_farmer",
            "My tomato plants have yellow spots in Kandy and the weather has been very wet.",
        )
    )
