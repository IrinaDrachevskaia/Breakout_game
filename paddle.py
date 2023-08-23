from turtle import Turtle
import time

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1, 6)
        self.setheading(0)
        self.color("light grey")
        self.penup()
        self.goto(0, -272)
        self.speed("fastest")

    def right(self):
        self.forward(20)

    def left(self):
        self.backward(20)

    def change_paddle(self):
        self.shapesize(1, 3)