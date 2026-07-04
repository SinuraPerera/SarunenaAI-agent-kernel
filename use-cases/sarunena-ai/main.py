from agents.weather_agent import get_weather
from agents.disease_agent import detect_disease
from agents.market_agent import get_market_price
from agents.memory_agent import save_farmer, get_farmer_crop

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

    print(get_weather())
    print(detect_disease(user))
    print(get_market_price(user))