from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 24, 'normal')

points = {(255.0, 0.0, 0.0): 7,
          (255.0, 128.0, 0.0): 5,
          (0.0, 255.0, 0.0): 3,
          (255.0, 255.0, 0.0): 1}

class ScoreBord(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.color("white")
        self.score = 0
        self.lives = 3

    def count_score(self, color):
        self.clear()
        self.score += points[color]
        self.write(f"{self.lives}❤️      Score: {self.score}", align=ALIGNMENT, font=FONT)
        # print(self.score)

    def update_score(self):
        self.clear()
        self.write(f"{self.lives}❤️      Score: {self.score}", align=ALIGNMENT, font=FONT)

    def count_lives(self, attempt):
        self.clear()
        self.write(f"{self.lives}❤️      Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.lives = 3 - attempt
        # print(self.lives)