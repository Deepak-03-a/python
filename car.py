class Car:
    def __init__(self,model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"Your drive {self.color} {self.model} car")

    def stop(self):
        print(f"You stopped {self.color} {self.model}car")

    def describe(self):
        print(f"{self.model} {self.year} {self.color}")