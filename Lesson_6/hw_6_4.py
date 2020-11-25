class Car:

    def __init__(self, s, c, n, i):
        self.speed = s
        self.color = c
        self.name = n
        self.is_police = i

    def go(self, a):
        self.speed = a
        print(f"Машина {self.name} поехала")

    def stop(self):
        self.speed = 0
        print(f"Машина {self.name} остановилась")

    def turn(self, direction):
        if direction == -1:
            print(f"Машина {self.name} повернула налево ")
        if direction == 1:
            print(f"Машина {self.name} повернула направо")

    def show_speed(self):
        print(self.speed)

class TownCar(Car):
    def __init__(self, s, c, n, i):
        super().__init__(s, c, n, i)

    def show_speed(self):
        if self.speed > 60:
            print("Превышение скорости")

class SportCar(Car):
    def __init__(self, s, c, n, i):
        super().__init__(s, c, n, i)

    def show_speed(self):
        if self.speed == 180:
            print( "need for speed!")

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print( "stop!")

class PoliceCar(Car):
    def show_speed(self):
        if self.speed > 150:
            print("Good luck!")

town_car = TownCar(70, "red", "bmw", False)
town_car.show_speed()

police_car = PoliceCar(90, "red", "bmw", True)
police_car.go(200)
police_car.show_speed()
police_car.turn(-1)

sport_car = SportCar(180, "red", "bmw", False)
sport_car.show_speed()

work_car = WorkCar(190, "red", "bmw", False)
work_car.show_speed()








