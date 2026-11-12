class Planet:
    def __init__(self, name, planet_type, star):
        if not isinstance(name, str) or not isinstance(planet_type, str) or not isinstance(star, str):
            raise TypeError('name, planet type, and star must be strings')

        if not name or not planet_type or not star:
            raise ValueError("name, planet_type, and star must be non-empty strings")

        self.name = name
        self.planet_type = planet_type
        self.star = star

    def orbit(self):
        return f"{self.name} is orbiting around {self.star}..."

    def __str__(self):
        return f"Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}"

planet_1 = Planet("Kepler-186f", "Rocky", "Kepler-186")
planet_2 = Planet("HD 209458 b", "Hot Jupiter", "HD 209458")
planet_3 = Planet("TRAPPIST-1e", "Rocky", "TRAPPIST-1")


print(planet_1)
print(planet_2)
print(planet_3)

print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())
