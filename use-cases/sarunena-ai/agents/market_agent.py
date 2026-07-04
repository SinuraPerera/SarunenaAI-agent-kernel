def get_market_price(crop):
    crop = crop.lower()

    if "tomato" in crop:
        return "💰 Tomato market price: Rs. 220/kg"

    if "rice" in crop:
        return "💰 Rice market price: Rs. 170/kg"

    return "💰 Market data unavailable."