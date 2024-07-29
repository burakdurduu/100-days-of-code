from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.turtlesize(1, 1)
        self.penup()


class Parts:
    def __init__(self):
        self.parts = []
        self.x_cor = -100
        self.y_cor = -250
        self.parts_len = 14
        self.create_parts()
        self.right_part = self.parts[len(self.parts) - 1]
        self.left_part = self.parts[0]
        self.middle_part = self.parts[int(len(self.parts) / 2) - 1]

    def create_parts(self):
        for row in range(self.parts_len):
            part = Paddle()
            part.goto(self.x_cor + row * 20, self.y_cor)
            self.parts.append(part)

    def go_right(self):
        if self.right_part.xcor() < 580:
            for part in self.parts:
                new_xcor = part.xcor() + 40
                part.goto(x=new_xcor, y=self.y_cor)

    def go_left(self):
        if self.left_part.xcor() > -580:
            for part in self.parts:
                new_xcor = part.xcor() - 40
                part.goto(x=new_xcor, y=self.y_cor)

    def reset_position(self):
        for i in range(len(self.parts)):
            self.parts[i].goto(self.x_cor + i * 20, self.y_cor)
