class Car:
    def __init__(self, registration_number, max_speed):
        # Initialize car properties
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0  # Automatically set to 0
        self.travelled_distance = 0  # Automatically set to 0

# Main program
if __name__ == "__main__":
    # Create a new car with registration number ABC-123 and max speed of 142 km/h
    car = Car("ABC-123", 142)

    # Print out all properties of the car
    print(f"Registration number: {car.registration_number}")
    print(f"Maximum speed: {car.max_speed} km/h")
    print(f"Current speed: {car.current_speed} km/h")
    print(f"Travelled distance: {car.travelled_distance} km")
