def calculate_risk(crop, rain):

    score = 100

    if rain > 0:
        score -= 20

    crop = crop.lower()

    if "tomato" in crop:
        score -= 10

    if "rice" in crop:
        score -= 5

    if score >= 80:
        level = "🟢 Low Risk"
    elif score >= 60:
        level = "🟡 Medium Risk"
    else:
        level = "🔴 High Risk"

    return score, level