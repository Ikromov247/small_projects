import turtle
from turtle import Turtle
import random
turtle.colormode(255)
# range (240, -240), 8 lanes with height 60 each.
# cars are 40 in height, 80 in length.
# car's starting y_coordinate -- 210. +-60 in each lane.
CAR_YCORS = [x for x in range(-210, 211, 60)]
COLORS = ["red", "blue", "green", "black", "gray", "cyan"]
INCREMENT = 10


class Cars:
    def __init__(self):
        self.all_cars = []
        self.car_speed = 20

    def generate_car(self):
        chance = random.randint(1, 3)
        if chance == 1:
            new_car = Turtle("square")
            color = random.choice(COLORS)
            new_car.up()
            new_car.seth(180)
            new_car.color(color)
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            y_cor = random.choice(CAR_YCORS)
            new_car.goto(280, y_cor)
            self.all_cars.append(new_car)

            print(len(self.all_cars))

    def move_cars(self):
        self.remove_cars()
        for car in self.all_cars:
            car.forward(self.car_speed)

    def increase_speed(self):
        self.car_speed += INCREMENT

    def remove_cars(self):
        for car in self.all_cars[:10]:
            if car.xcor() < -300:
                car.reset()
                self.all_cars.remove(car)
                print("cars removed")
