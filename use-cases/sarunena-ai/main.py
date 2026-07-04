from agents.weather_agent import get_weather
from agents.disease_agent import detect_disease
from agents.market_agent import get_market_price
from agents.memory_agent import save_farmer, get_farmer_crop
from agents.location_agent import get_location_coordinates
from agents.risk_agent import calculate_risk
from agents.recommendation_agent import get_recommendation
from agents.insight_agent import get_insight

print("🌱 SaruNena AI Started")

farmer_name = input("Enter Farmer Name: ")

while True:
    user = input("\nFarmer: ")

    if user.lower() == "exit":
        break

    previous_crop = get_farmer_crop(farmer_name)

    print("\n🌾 =============================")
    print("      SaruNena AI Report")
    print("==============================")

    print(f"📍 Location: {location_name.title()}")
    print(f"🌡 Temperature: {temp}°C")
    print(f"🌧 Rain: {rain} mm")

    print("\n🍅 Disease Analysis:")
    print(detect_disease(user))

    print("\n💰 Market Analysis:")
    print(get_market_price(user))

    score, level = calculate_risk(user, rain)

    print("\n📊 Risk Analysis:")
    print(f"Score: {score}/100")
    print(level)

    print("\n💡 Recommendation:")
    print(get_recommendation(score))

    print("\n🧠 AI Insight:")
    print(get_insight(user, score, rain))

    print("==============================\n")