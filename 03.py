class Auto:
    def __init__(self, huippunopeus):
        self.huippunopeus = huippunopeus  # The car's top speed (km/h)
        self.nopeus = 0  # The car's current speed (km/h)
        self.matka = 0  # The car's traveled distance (km)

    def kiihdytä(self, nopeuden_muutos):
        # Change the speed while ensuring it's within allowed limits
        uusi_nopeus = self.nopeus + nopeuden_muutos

        if uusi_nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus  # Set to top speed if exceeded
        elif uusi_nopeus < 0:
            self.nopeus = 0  # Set to 0 if speed drops below zero
        else:
            self.nopeus = uusi_nopeus  # Update to the new speed

    def kulje(self, tunnit):
        # Increase the traveled distance based on current speed and time in hours
        self.matka += self.nopeus * tunnit

# Main program

# Create a car with a top speed of 180 km/h
auto = Auto(180)

# Increase speed to 30 km/h
auto.kiihdytä(30)
print(f"Current speed: {auto.nopeus} km/h")

# Increase speed to 70 km/h
auto.kiihdytä(70)
print(f"Current speed: {auto.nopeus} km/h")

# Increase speed to 50 km/h
auto.kiihdytä(50)
print(f"Current speed: {auto.nopeus} km/h")

# Perform emergency braking
auto.kiihdytä(-200)
print(f"New speed after emergency braking: {auto.nopeus} km/h")

# Set an initial distance of 2000 km and drive for 1.5 hours
auto.matka = 2000
auto.kulje(1.5)
print(f"New traveled distance: {auto.matka} km")
