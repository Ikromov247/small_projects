from turtle import Turtle
UP_DISTANCE = 60
SIDE_DISTANCE = 40
SIDE_BOUNDARY = 280


class MyTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.shapesize(1, 1)
        self.color("black")
        self.up()
        self.seth(90)
        self.goto(0, -270)

    def reset_turtle(self):
        self.goto(0, -270)
    def go_up(self):
        new_y = self.ycor() + UP_DISTANCE
        self.goto(self.xcor(), new_y)
    def go_right(self):
        new_x = self.xcor() + SIDE_DISTANCE
        if new_x > SIDE_BOUNDARY:
            new_x -= SIDE_DISTANCE
        self.goto(new_x, self.ycor())
    def go_left(self):
        new_x = self.xcor() - SIDE_DISTANCE
        if new_x < -SIDE_BOUNDARY:
            new_x += SIDE_DISTANCE
        self.goto(new_x, self.ycor())

    def is_at_finish_lane(self):
        if self.ycor() > 270:
            self.reset_turtle()
            return True
        else:
            return False