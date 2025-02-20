class Car:
    def __init__(self, model, color, year, for_sale):
        self.model = model
        self.color = color
        self.year = year
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive the {self.color} {self.model}.")

# Creating instances outside the class
car1 = Car("Range Rover", "black", 2024, False)
car2 = Car("Ferrari", "yellow", 2024, True)

# Calling the drive method
car1.drive()
car2.drive()
