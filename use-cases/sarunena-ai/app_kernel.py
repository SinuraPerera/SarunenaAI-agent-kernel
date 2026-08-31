"""
SaruNena AI - Flask Web Application using Agent Kernel (optional LLM path).

Uses the same deterministic analysis pipeline as app.py, with optional
multi-agent LLM orchestration when openai-agents is installed.
"""

import logging
import os
from datetime import datetime

from flask import Flask, jsonify, render_template, request, session, send_file

from sarunena_kernel import orchestrator

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "sarunena_secret_key_2026")


def validate_environment():
    """Validate required environment variables and configuration."""
    warnings = []
    
    # Check for optional OpenAI API key
    if not os.getenv("OPENAI_API_KEY"):
        warnings.append("OPENAI_API_KEY not set - running in deterministic mode only")
    
    # Check for optional WhatsApp credentials
    if not os.getenv("WHATSAPP_PHONE_NUMBER_ID"):
        warnings.append("WHATSAPP_PHONE_NUMBER_ID not set - WhatsApp integration disabled")
    
    # Log warnings if any
    for warning in warnings:
        logger.warning("Configuration warning: %s", warning)
    
    return warnings


@app.route("/", methods=["GET", "POST"])
def home():
    """Main route for the web interface."""
    result = None
    error = None

    if request.method == "POST":
        user_input = request.form.get("input", "").strip()
        farmer_id = request.form.get("farmer_id") or session.get("farmer_id", "web_user")

        if not user_input:
            error = "Please enter a crop or farming query"
        else:
            try:
                analysis = orchestrator.analyze_query(user_input)
                llm_response = orchestrator.process_farmer_query(farmer_id, user_input)
                result = {**analysis, "llm_response": llm_response, "query": user_input}
            except Exception as exc:
                logger.error("Error processing query: %s", exc)
                error = f"Error processing query: {str(exc)[:100]}"

    return render_template("index.html", result=result, error=error, history=None, now=datetime.now())


@app.route("/api/analyze", methods=["POST"])
def analyze():
    """API endpoint for comprehensive farming analysis."""
    try:
        data = request.get_json(force=True) or {}
        user_input = data.get("query") or f"{data.get('crop', 'tomato')} in {data.get('location', 'Kandy')}"
        analysis = orchestrator.analyze_query(user_input)
        return jsonify({"success": True, "analysis": analysis})
    except Exception as exc:
        logger.error("Error in analysis: %s", exc)
        return jsonify({"success": False, "error": str(exc)}), 500


@app.route("/logo.png")
def logo():
    """Serve the logo image."""
    logo_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logo.png")
    return send_file(logo_path, mimetype='image/png')


@app.route("/health", methods=["GET"])
def health():
    """Health check endpoint."""
    return jsonify({"status": "healthy", "system": "sarunena-ai"})


if __name__ == "__main__":
    # Validate environment configuration
    validate_environment()
    
    # Initialize orchestrator
    try:
        orchestrator.initialize()
        logger.info("SaruNena AI orchestrator initialized successfully")
    except Exception as exc:
        logger.warning("Multi-agent runtime unavailable; running deterministic analysis mode: %s", exc)
    
    # Run Flask application
    port = int(os.getenv("PORT", 5000))
    debug = os.getenv("FLASK_DEBUG", "True").lower() == "true"
    logger.info("Starting SaruNena AI web server on port %d", port)
    app.run(debug=debug, host="0.0.0.0", port=port)
