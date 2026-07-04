def get_recommendation(score):

    if score >= 80:
        return "✅ Conditions are favorable. Continue normal farming activities."

    elif score >= 60:
        return "⚠ Monitor crop conditions and check for disease symptoms."

    return "🚨 High risk detected. Immediate inspection is recommended."