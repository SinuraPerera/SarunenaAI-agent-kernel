def detect_disease(crop):
    crop = crop.lower()

    if "tomato" in crop:
        return "🍅 Possible Early Blight detected."

    if "rice" in crop:
        return "🌾 Possible Brown Spot disease detected."

    return "🌿 No disease information available."