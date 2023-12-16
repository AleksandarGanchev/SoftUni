countries = input().split(", ")
capitals = input().split(", ")


dictionary = {country:capital for country,capital in zip(countries, capitals)}

for country, capital in dictionary.items():
    print(f"{country} -> {capital}")