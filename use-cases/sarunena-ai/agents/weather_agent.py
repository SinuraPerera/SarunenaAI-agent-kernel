import requests

import requests

def get_weather(latitude, longitude):

    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        f"&current=temperature_2m,rain"
    )

    try:
        response = requests.get(url)
        data = response.json()

        temp = data["current"]["temperature_2m"]
        rain = data["current"]["rain"]

        return temp, rain

    except:
        return None, None

    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        f"&current=temperature_2m,rain"
    )

    try:
        response = requests.get(url)
        data = response.json()

        temp = data["current"]["temperature_2m"]
        rain = data["current"]["rain"]

        if rain > 0:
            advice = "Avoid spraying today."
        else:
            advice = "Weather suitable for farming."

        return f"🌡 {temp}°C | 🌧 {rain} mm | 💡 {advice}"

    except Exception:
        return "⚠ Unable to fetch weather data"