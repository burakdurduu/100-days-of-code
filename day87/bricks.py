from turtle import Turtle
import random

COLOR_LIST = ['light blue', 'royal blue', 'light steel blue', 'steel blue',
              'light cyan', 'light sky blue', 'violet', 'salmon', 'tomato',
              'sandy brown', 'purple', 'deep pink', 'medium sea green', 'khaki']


class Brick(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLOR_LIST))
        self.turtlesize(1, 3)
        self.penup()


class Bricks:
    def __init__(self):
        self.bricks = []
        self.x_cor = -480
        self.y_cor = 230
        self.create_bricks()

    def create_bricks(self):
        for row in range(7):
            for col in range(16):
                brick = Brick()
                brick.goto(self.x_cor + col * 65, self.y_cor)
                self.bricks.append(brick)
            self.y_cor -= 28

    def reset_bricks(self):
        for brick in self.bricks:
            brick.hideturtle()
        self.bricks = []
        self.y_cor = 230
        self.create_bricks()
