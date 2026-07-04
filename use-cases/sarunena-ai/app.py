from flask import Flask, render_template, request

from agents.location_agent import get_location_coordinates
from agents.weather_agent import get_weather
from agents.disease_agent import detect_disease
from agents.market_agent import get_market_price
from agents.risk_agent import calculate_risk
from agents.recommendation_agent import get_recommendation
from agents.insight_agent import get_insight

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":

        user_input = request.form["input"]

        location_name, coords = get_location_coordinates(user_input)
        lat, lon = coords

        temp, rain = get_weather(lat, lon)

        score, level = calculate_risk(user_input, rain)

        result = {
            "location": location_name.title(),
            "temp": temp,
            "rain": rain,
            "disease": detect_disease(user_input),
            "market": get_market_price(user_input),
            "risk_score": score,
            "risk_level": level,
            "recommendation": get_recommendation(score),
            "insight": get_insight(user_input, score, rain)
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)