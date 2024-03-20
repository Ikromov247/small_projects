from turtle import Turtle
FONT = ("Arial", 10, "bold")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.hideturtle()
        self.up()
        self.goto(0, 280)
        self.update_level()

    def update_level(self):
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_level()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align=ALIGNMENT, font=("Ariel", 40, "bold"))