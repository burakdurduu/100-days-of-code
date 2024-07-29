from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(0, 250)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(self.score, align="center", font=("Courier", 40, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset_score(self):
        self.score = 0
        self.update_score()
