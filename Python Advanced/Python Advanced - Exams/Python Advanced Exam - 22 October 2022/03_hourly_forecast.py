def forecast(*args):
    sunny_locations = []
    cloudy_locations = []
    rainy_locations = []

    for city, weather in args:
        if weather == "Sunny":
            sunny_locations.append(city)
        elif weather == "Cloudy":
            cloudy_locations.append(city)
        elif weather == "Rainy":
            rainy_locations.append(city)

    sunny_locations = sorted(sunny_locations)
    cloudy_locations = sorted(cloudy_locations)
    rainy_locations = sorted(rainy_locations)

    output = ''
    if sunny_locations:
        for location in sunny_locations:
            output += f"{location} - Sunny\n"

    if cloudy_locations:
        for location in cloudy_locations:
            output += f"{location} - Cloudy\n"

    if rainy_locations:
        for location in rainy_locations:
            output += f"{location} - Rainy\n"

    return output
