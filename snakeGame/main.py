from turtle import Screen
import time
from Snake import Snake
from Food import Food
from Scoreboard import Scoreboard
import sys
import os
# create screen canvas, set size, color and title
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

# objects
snake = Snake()
food = Food()
screen.update()
scoreboard = Scoreboard()


def finish_game():
    sys.exit(0)

# action listener
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(finish_game, "space")
# start game

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.add_tail()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        # game_is_on = False
        scoreboard.reset_scoreboard()
        snake.reset_snake()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # game_is_on = False
            scoreboard.reset_scoreboard()
            snake.reset_snake()

screen.exitonclick()
