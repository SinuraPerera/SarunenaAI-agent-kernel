LOCATIONS = {
    "colombo": (6.9271, 79.8612),
    "kandy": (7.2906, 80.6337),
    "galle": (6.0535, 80.2210),
    "kurunegala": (7.4863, 80.3623),
    "anuradhapura": (8.3114, 80.4037)
}

def get_location_coordinates(text):
    text = text.lower()

    for city, coords in LOCATIONS.items():
        if city in text:
            return city, coords

    return "colombo", LOCATIONS["colombo"]