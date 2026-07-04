def get_insight(crop, score, rain):

    crop = crop.lower()

    if score >= 80 and rain == 0:
        return "🌟 Best time for farming activities. High productivity expected."

    if "tomato" in crop and rain > 0:
        return "⚠ Tomato crops are vulnerable to fungal infection due to rain."

    if score < 60:
        return "🚨 Consider crop protection measures immediately."

    return "📊 Monitor conditions regularly for optimal yield."