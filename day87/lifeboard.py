from turtle import Turtle


class LifeBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("red")
        self.penup()
        self.hideturtle()
        self.lives = 3
        self.goto(470, 250)
        self.update_lives()

    def update_lives(self):
        self.clear()
        current_lives = ""
        for i in range(self.lives):
            current_lives += "❤️"
        self.write(current_lives, align="center", font=("Courier", 40, "normal"))

    def lose_life(self):
        self.lives -= 1
        self.update_lives()

    def reset_lives(self):
        self.lives = 3
        self.update_lives()
