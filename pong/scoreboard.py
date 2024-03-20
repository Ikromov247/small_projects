"""scoreboard for paddles"""
from turtle import Turtle
FONT = ("Arial", 40, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.hideturtle()
        self.up()
        self.goto(position)
        self.score = 0
        self.color("white")
        self.update_score()

    def update_score(self):
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
