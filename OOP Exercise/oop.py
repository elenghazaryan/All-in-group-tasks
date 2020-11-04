#Question1
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


#Question2
class Vehicle2:
    pass


#Question3
class Vehicle3:
    color = "White"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle3):
    pass


#Question4
class Vehicle4:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"


class Bus4(Vehicle4):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)


#Question5
class Bus5(Vehicle3):
    pass


class Car(Vehicle3):
    pass


#Question6
class Vehicle6:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100


class Bus6(Vehicle6):
    def fare(self):
        amount = super().fare()
        amount += amount * 10/100
        return amount


#Question7
def check_which_class():
    school_bus7 = Bus6("Volvo", 15, 55)
    print(type(school_bus7))


#Question8
def check():
    bus8 = Bus4("volvo", 35, 55)
    print(isinstance(bus8, Vehicle4))


if __name__ == "__main__":
    while True:
        case = int(input("\nEnter the number of question which you want to run 1/2/3/.../10, 0 to QUIT\t"))
        if case == 1:
            model1 = Vehicle(240, 18)
            print(model1.max_speed, model1.mileage)
        elif case == 2:
            pass
        elif case == 3:
            bus = Bus("School Volvo", 180, 12)
            print("Vehicle Name: {}, Speed: {}, Mileage: {}".format(bus.name, bus.max_speed, bus.mileage))
        elif case == 4:
            bus4 = Bus4("School Volvo", 180, 12)
            print(bus4.seating_capacity())
        elif case == 5:
            school_bus = Bus5("School Volvo", 180, 12)
            print(school_bus.color, school_bus.name, "Speed:", school_bus.max_speed, "mileage:", school_bus.mileage)
            car = Car("BMW i8", 240, 18)
            print(car.color, car.name, "Speed:", car.max_speed, "Mileage:", car.mileage)
        elif case == 6:
            sc_bus = Bus6("School Volvo", 12, 50)
            print("Total Bus fare is:", int(sc_bus.fare()))
        elif case == 7:
            check_which_class()
        elif case == 8:
            check()
        elif case == 0:
            break
        else:
            print("Input correct question number")