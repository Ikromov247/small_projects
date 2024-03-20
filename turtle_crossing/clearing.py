from turtle import Turtle


class Clearing(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("square")
        self.seth(0)
        self.color("gray")
        self.up()
        self.goto(-300, -240)
        self.draw_lane()
        self.goto(-300, 300)
        self.draw_lane()

    def draw_lane(self):
        self.down()
        self.begin_poly()
        self.begin_fill()
        self.goto(self.xcor()+600, self.ycor())
        self.goto(self.xcor(), self.ycor()-60)
        self.goto(self.xcor() - 600, self.ycor())
        self.goto(self.xcor(), self.ycor() + 60)
        self.end_poly()
        self.end_fill()
        self.up()
