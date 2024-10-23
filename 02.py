class Auto:
    def __init__(self, huippunopeus):
        self.huippunopeus = huippunopeus  # The car's top speed
        self.nopeus = 0  # The car's current speed

    def kiihdytä(self, nopeuden_muutos):
        # Change the speed while ensuring it's within allowed limits
        uusi_nopeus = self.nopeus + nopeuden_muutos

        if uusi_nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus  # Set to top speed if exceeded
        elif uusi_nopeus < 0:
            self.nopeus = 0  # Set to 0 if speed drops below zero
        else:
            self.nopeus = uusi_nopeus  # Update to the new speed

# Main program:
if __name__ == "__main__":
    auto = Auto(huippunopeus=150)  # Create a car object with top speed of 150 km/h

    # Increase speed to +30 km/h
    auto.kiihdytä(30)
    print(f"Speed after +30 km/h: {auto.nopeus} km/h")

    # Increase speed to +70 km/h
    auto.kiihdytä(70)
    print(f"Speed after +70 km/h: {auto.nopeus} km/h")

    # Increase speed to +50 km/h
    auto.kiihdytä(50)
    print(f"Speed after +50 km/h: {auto.nopeus} km/h")

    # Emergency braking with -200 km/h
    auto.kiihdytä(-200)
    print(f"Speed after emergency braking (-200 km/h): {auto.nopeus} km/h")
