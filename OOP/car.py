# Starting Out with Python (4th Edition).
# Tony Gaddis.
# Page 569.
# Q. 2 Car Class.


class Car:

    def __init__(self, model, make, speed):
        self.__year_model = model
        self.__make = make
        self.__speed = speed = 0

    def set_model(self, model):
        self.__year_model = model
    
    def set_make(self, make):
        self.__make = make
    
    def set_speed(self, speed):
        self.__speed = speed
    
    def get_model(self):
        return self.__year_model

    def get_make(self):
        return self.__make

    def get_speed(self):
        return self.__speed

    def accelerate(self, speed):
        self.__speed += 5

    def brake(self, speed):
        self.__speed -= 5

def main():

    model = input("Enter Car Model: ")
    make = input("Enter Car Make: ")
    speed = 0

    car = Car(model, make, speed)

    for i in range(0, 5):
        car.accelerate(speed)
        print("Speed = ", car.get_speed())

    for i in range(0, 5):
        car.brake(speed)
        print("Speed = ", car.get_speed())
 
main()
