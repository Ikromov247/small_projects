from turtle import Screen
from turtle_manager import MyTurtle
from scoreboard import Scoreboard
from clearing import Clearing
from car_manager import Cars
from time import sleep

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle crossing")
screen.tracer(0)

game_turtle = MyTurtle()
lane_clearing = Clearing()
level = Scoreboard()
cars = Cars()
screen.update()

screen.listen()
screen.onkeypress(game_turtle.go_up, "Up")
screen.onkeypress(game_turtle.go_right, "Right")
screen.onkeypress(game_turtle.go_left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.2)
    cars.generate_car()
    cars.move_cars()

    if game_turtle.is_at_finish_lane():
        level.increase_level()
        cars.increase_speed()

    for car in cars.all_cars:
        if game_turtle.distance(car) < 40:
            screen.update()
            level.game_over()
            game_is_on=False

screen.exitonclick()
