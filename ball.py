from turtle import Turtle
import random

ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(1, 1)
        self.color("white")
        self.penup()
        self.reset_position()
        self.move_speed = 0.1

    def move(self):
        self.forward(20)

    def change_direction(self, minus_angel):
        angle = minus_angel - self.heading()
        self.setheading(angle)
        self.move()

    def game_over(self):
        self.goto(0, -20)
        self.color('red')
        self.write("Game over.", align=ALIGNMENT, font=FONT)

    def reset_position(self):
        self.goto(0, -250)
        heading = random.randint(50, 130)
        self.setheading(heading)
        self.move_speed = 0.1
