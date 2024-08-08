class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

obj1 = Vehicle(240, 18)
print(obj1.max_speed, obj1.mileage)