from agents.weather_agent import get_weather
from agents.disease_agent import detect_disease
from agents.market_agent import get_market_price
from agents.memory_agent import save_farmer, get_farmer_crop
from agents.location_agent import get_location_coordinates
from agents.risk_agent import calculate_risk
from agents.recommendation_agent import get_recommendation

print("🌱 SaruNena AI Started")

farmer_name = input("Enter Farmer Name: ")

while True:
    user = input("\nFarmer: ")

    if user.lower() == "exit":
        break

    previous_crop = get_farmer_crop(farmer_name)

    if previous_crop:
        print(f"\n👋 Welcome back {farmer_name}")
        print(f"🌱 Last crop discussed: {previous_crop}")

    save_farmer(farmer_name, user)

    print("\n--- AGENT RESPONSES ---")

    location_name, coords = get_location_coordinates(user)

    latitude, longitude = coords

    temp, rain = get_weather(latitude, longitude)

    print(f"📍 Location: {location_name.title()}")
    print(f"🌡 Temperature: {temp}°C")
    print(f"🌧 Rain: {rain} mm")

    score, level = calculate_risk(user, rain)

    print(f"📊 Farm Health Score: {score}/100")
    print(level)
    print(get_recommendation(score))
    
    print(detect_disease(user))
    print(get_market_price(user))