"""Paddle and its movement"""
from turtle import Turtle
UPPER_BORDER = 300
LOWER_BORDER = -300


class Paddle(Turtle):
    def __init__(self, cor):
        super().__init__()
        self.cor = cor
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.up()
        self.goto(self.cor, 0)

    def go_up(self):
        current_ycor = self.ycor()
        if LOWER_BORDER < current_ycor < UPPER_BORDER:
            self.goto(self.xcor(), current_ycor+20)

    def go_down(self):
        current_ycor = self.ycor()
        if LOWER_BORDER < current_ycor < UPPER_BORDER:
            self.goto(self.xcor(), current_ycor - 20)

    def reset_position(self):
        self.goto(self.cor, 0)