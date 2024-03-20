from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in range(3):
            segment = Turtle("square")
            segment.color("white")
            segment.up()
            segment.goto(-20 * i, 0)
            self.segments.append(segment)

    def add_tail(self):
        new_tail = Turtle("square")
        new_tail.color("white")
        new_tail.up()
        new_tail_xpos = self.segments[-1].xcor()
        new_tail_ypos = self.segments[-1].ycor()
        new_tail.goto(new_tail_xpos, new_tail_ypos)
        self.segments.append(new_tail)

    def move(self):
        # move snake's segments except head
        for i in range(len(self.segments) - 1, 0, -1):
            new_pos = self.segments[i - 1].pos()
            self.segments[i].goto(new_pos)
        self.head.forward(MOVE_DISTANCE)

    def reset_snake(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)
