import random

class Auto:
    def __init__(self, huippunopeus, rekisterinumero):
        self.huippunopeus = huippunopeus  # The car's top speed (km/h)
        self.nopeus = 0  # The car's current speed (km/h)
        self.matka = 0  # The car's traveled distance (km)
        self.rekisterinumero = rekisterinumero  # The car's registration number

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

# Create a list of 10 car objects with random top speeds and registration numbers
cars = []
for i in range(1, 11):
    huippunopeus = random.randint(100, 200)  # Random top speed between 100 and 200 km/h
    rekisterinumero = f"ABC-{i}"  # Registration number format ABC-1, ABC-2, ..., ABC-10
    car = Auto(huippunopeus, rekisterinumero)
    cars.append(car)

# Print details of each car before the race starts
for car in cars:
    print(f"Car {car.rekisterinumero}: Top speed = {car.huippunopeus} km/h, Initial distance = {car.matka} km")
