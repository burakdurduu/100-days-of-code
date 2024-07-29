from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 5
        self.y_move = 5

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1

    def bounce_y_straight(self):
        self.y_move *= -1
        self.x_move = 0

    def bounce_y_left_wide(self):
        self.y_move *= -1
        self.x_move = 15 * random.choice([-1, -0.9, -0.8, -0.7])

    def bounce_y_left_narrow(self):
        self.y_move *= -1
        self.x_move = 15 * random.choice([-0.5, -0.3, -0.2])

    def bounce_y_right_wide(self):
        self.y_move *= -1
        self.x_move = 15 * random.choice([0.7, 0.8, 0.9, 1])

    def bounce_y_right_narrow(self):
        self.y_move *= -1
        self.x_move = 15 * random.choice([0.2, 0.3, 0.5])

    def reset_position(self):
        self.goto(0, -50)
        self.bounce_y_straight()

    def window_collision(self, paddle, lifeboard):
        if self.xcor() > 580 or self.xcor() < -570:
            self.bounce_x()
        if self.ycor() > 280:
            self.bounce_y()
        if self.ycor() < -350:
            lifeboard.lose_life()
            paddle.reset_position()
            self.reset_position()

    def paddle_collision(self, paddle):
        right_paddle = paddle.parts.index(paddle.right_part)
        left_paddle = paddle.parts.index(paddle.left_part)
        mid_paddle = paddle.parts.index(paddle.middle_part)
        for part in paddle.parts:
            part_index = paddle.parts.index(part)
            if self.distance(part) < 40 and self.ycor() < part.ycor() + 30:
                if part_index < mid_paddle:
                    if part_index < left_paddle:
                        self.bounce_y_left_wide()
                    elif part_index >= left_paddle:
                        self.bounce_y_left_narrow()
                elif part_index > mid_paddle:
                    if part_index > right_paddle:
                        self.bounce_y_right_wide()
                    elif part_index <= right_paddle:
                        self.bounce_y_right_narrow()
                else:
                    self.bounce_y_straight()
                break

    def bricks_collision(self, bricks, scoreboard):
        for brick in bricks.bricks:
            if self.distance(brick) < 40:
                scoreboard.increase_score()
                brick.hideturtle()
                bricks.bricks.remove(brick)
                self.bounce_y()
