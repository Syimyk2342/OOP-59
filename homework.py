
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def info(self):
        return f"{self.brand} {self.model}, год выпуска: {self.year}"

car1 = Car("Kia", "K5", 2018)
car2 = Car("Toyota", "Camry", 2021)

print(car1.info())
print(car2.info())
