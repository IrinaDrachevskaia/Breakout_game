from turtle import Screen
from paddle import Paddle
from ball import Ball
from bricks import Bricks
import math
from scoreboard import ScoreBord
import time

RED = (255.0, 0.0, 0.0)
ORANGE = (255.0, 128.0, 0.0)

screen = Screen()
screen.colormode(255)
ball = Ball()
paddle = Paddle()
bricks = Bricks()
scoreboard = ScoreBord()

screen.setup(width=890, height=600)
screen.bgcolor("black")
screen.title("Break Game")
screen.tracer(0)

screen.listen()
screen.onkey(key="Left", fun=paddle.left)
screen.onkey(key="Right", fun=paddle.right)

t = 0.2
attempt = 0
red_bricks = 0
orange_brick = 0
dist = 61

game_is_on = True
while game_is_on:
    screen.update()
    scoreboard.update_score()
    time.sleep(t)
    ball.move()

    #detect a colision with a wall
    if ball.xcor() > 435 or ball.xcor() < -435:
        ball.change_direction(180)

    # detect a colision with a top
    elif ball.ycor() > 239:
        ball.change_direction(0)
        paddle.change_paddle()
        dist = 32

    # detect a colision with a paddle
    elif ball.distance(paddle) < dist and ball.ycor() < -251:
        ball.change_direction(0)

    # detect a colision with bricks
    for brick in bricks.bricks[::-1]:
        if ball.distance(brick) < 36 and math.fabs(ball.ycor()-brick.ycor()) < 21:
            color = brick.color()[0]
            scoreboard.count_score(color)
            scoreboard.update_score()
            if color == RED:
                red_bricks += 1
            elif color == ORANGE:
                orange_brick += 1
            ball.change_direction(0)
            bricks.bricks.remove(brick)
            brick.reset()
            #move away knocked down bricks
            brick.color('black')
            brick.penup()
            brick.speed('fastest')
            brick.goto(-443, 290)
            # increase in speed
            if len(bricks.bricks) == 100 or len(bricks.bricks) == 108 or red_bricks == 1 or orange_brick == 1:
                t *= 0.8
    #check the rest of bricks
    if len(bricks.bricks) == 0:
        game_is_on = False
        ball.game_over()
        scoreboard.update_score()

    # detect a colision with a bottom
    elif ball.ycor() < -295:
        num_colission = 0
        if attempt < 2:
            ball.reset_position()
            attempt += 1
            scoreboard.count_lives(attempt)
            scoreboard.update_score()
        else:
            ball.game_over()
            attempt += 1
            scoreboard.count_lives(attempt)
            scoreboard.update_score()
            game_is_on = False






screen.exitonclick()