from turtle import Turtle


class GameManager(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.write_message("Press Space to Start")
        self.start = False
        self.quit = False

    def write_message(self, message):
        self.clear()
        self.goto(0, 0)
        self.write(message, align="center", font=("Courier", 24, "normal"))

    def press_to_start(self):
        self.start = True
        self.clear()

    def press_to_quit(self):
        self.quit = True

    def start_game(self):
        return self.start

    def quit_game(self):
        return self.quit

    def ask_play_again(self):
        self.write_message("Game Over. Press Space to Play Again or Q to Quit")

    def reset_intro(self):
        self.clear()
        self.write_message("Press Space to Start")
        self.start = False
        self.quit = False
