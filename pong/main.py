"""Gameplay"""
from turtle import Screen
from time import sleep
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(350)
l_paddle = Paddle(-350)
ball = Ball()
screen.update()
l_score = Scoreboard((-50, 240))
r_score = Scoreboard((50, 240))

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")
sleep_time = 0.1


def restart():
    sleep(2)
    ball.reset_position()
    r_paddle.reset_position()
    l_paddle.reset_position()


game_is_on = True
while game_is_on:
    if sleep_time == 0:
        game_is_on = False
        l_score.goto(0, 0)
        l_score.write("Game Over!", align="center", font=("Arial", 20, "normal"))

    ball.move()
    sleep(sleep_time)
    # collision with upper walls. bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # collision with paddles
    if not (-330 < ball.xcor() < 330) and \
            (r_paddle.distance(ball.pos()) < 60 or l_paddle.distance(ball.pos()) < 60):
        ball.bounce_x()

    # collision with side walls. update score and restart game
    if ball.xcor() > 380:
        restart()
        l_score.increase_score()
    elif ball.xcor() < -385:
        restart()
        r_score.increase_score()
    sleep_time = 0.1 - max(l_score.score, r_score.score) * 0.01
    print(sleep_time)
    screen.update()

screen.exitonclick()
