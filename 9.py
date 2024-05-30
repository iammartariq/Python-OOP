class TollBooth:

    def __init__(self, no_of_cars = 0, amount_collected = 0):
        self.no_of_cars = no_of_cars
        self.amount_collected = amount_collected
        no_of_cars = 0
        amount_collected = 0

    def payingCar(self):
        self.no_of_cars += 1
        self.amount_collected += 1

    def nopayCar(self):
        self.no_of_cars += 1

    def display(self):
        print(self.no_of_cars, ":", self.amount_collected)

tollbooth = TollBooth()

while True:
        user = input("Enter choice: ")
        if user.lower() == "p":
            tollbooth.payingCar()

        elif user.lower() == "n":
            tollbooth.nopayCar()

        elif user.lower() == "esc":
            tollbooth.display()
            break

        else:
            print("None")

