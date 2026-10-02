from turtle import Screen
from scoreboard import Scoreboard
from paddle import Paddle
from border import Border, Midline
from ball import Ball
import time

INITIAL_POSITIONS = [(350, 0), (-350, 0)]
MAX_SCORE = 5

## Screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

## Game components
border = Border()
midline = Midline()
right_paddle = Paddle(INITIAL_POSITIONS[0])
left_paddle = Paddle(INITIAL_POSITIONS[1])
ball = Ball()
scoreboard = Scoreboard()
game_on = True

## Movements
screen.listen()
screen.onkey(key="Up", fun=right_paddle.go_up)
screen.onkey(key="Down", fun=right_paddle.go_down)
screen.onkey(key="w", fun=left_paddle.go_up)
screen.onkey(key="s", fun=left_paddle.go_down)

## Game body
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    ### Collision with Top/Bottom wall
    if (
            ball.ycor() > 280
            or ball.ycor() < -280
    ):
        ball.y_bounce()

    ### Scoring
    if ball.xcor() > 380:
        scoreboard.increase_l_score()
        ball.refresh()
    elif ball.xcor() < -380:
        scoreboard.increase_r_score()
        ball.refresh()

    ### Collision with paddles
    if (
        ball.distance(right_paddle) < 50 and ball.xcor() > 320 or
        ball.distance(left_paddle) < 50 and ball.xcor() < -320
    ):
        ball.x_bounce()

    ### Game over
    if (
        scoreboard.left_score == MAX_SCORE or
        scoreboard.right_score == MAX_SCORE
    ):
        scoreboard.game_over()
        game_on = False























screen.exitonclick()