class Transport:
    def __init__(self, speed):
        self.speed = speed

    def move(self):
        return f"Транспорт движется со скоростью {self.speed} км/ч"



class Car(Transport):
    def __init__(self, brand, speed):
        super().__init__(speed)   # вызываем конструктор родителя
        self.brand = brand

    def move(self):
        return f"Машина {self.brand} едет со скоростью {self.speed} км/ч"


my_car = Car("BMW", 120)
print(my_car.move())
