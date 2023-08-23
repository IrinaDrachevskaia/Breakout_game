import random
from turtle import Turtle

colors = [(255, 0, 0), (255, 0, 0), (255, 128, 0), (255, 128, 0), (0, 255, 0), (0, 255, 0), (255, 255, 0), (255, 255, 0)]

class Bricks:

    def __init__(self):
        self.bricks = []
        self.create_bricks()

    def create_bricks(self):
        y = 230
        color = 0
        for yposition in range(8):
            x = -410
            for xposition in range(14):
                new_brick = Turtle('square')
                new_brick.shapesize(1, 3)
                new_brick.color(colors[color])
                new_brick.penup()
                new_brick.speed("fastest")
                new_brick.goto(x, y)
                self.bricks.append(new_brick)
                x += 63
            y -= 23
            color += 1
