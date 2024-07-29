from turtle import Screen
from paddle import Parts
from ball import Ball
from bricks import Bricks
from scoreboard import Scoreboard
from lifeboard import LifeBoard
from game_manager import GameManager


class Breakout:

    def __init__(self):
        self.screen = Screen()
        self.screen.title("Breakout")
        self.screen.setup(width=1200, height=600)
        self.screen.bgcolor("black")
        self.screen.tracer(0)

        self.paddle = Parts()
        self.ball = Ball()
        self.bricks = Bricks()
        self.scoreboard = Scoreboard()
        self.lifeboard = LifeBoard()
        self.game_manager = GameManager()

        self.screen.listen()
        self.screen.onkeypress(self.paddle.go_left,"Left")
        self.screen.onkeypress(self.paddle.go_right, "Right")
        self.screen.onkeypress(self.game_manager.press_to_start, "space")
        self.screen.onkeypress(self.game_manager.press_to_quit, "q")

    def game_over(self):
        if len(self.bricks.bricks) == 0:
            return True
        elif self.lifeboard.lives == 0:
            return True
        return False

    def reset_game(self):
        self.ball.reset_position()
        self.paddle.reset_position()
        self.bricks.reset_bricks()
        self.scoreboard.reset_score()
        self.lifeboard.reset_lives()
        self.game_manager.reset_intro()

    def mainloop(self):
        while True:
            self.screen.update()
            if self.game_manager.start_game():
                self.ball.move()
                self.ball.paddle_collision(self.paddle)
                self.ball.bricks_collision(self.bricks, self.scoreboard)
                self.ball.window_collision(self.paddle, self.lifeboard)
            if self.game_over():
                self.game_manager.start = False
                self.game_manager.ask_play_again()
                while not self.game_manager.start and not self.game_manager.quit_game():
                    self.screen.update()
                if self.game_manager.start:
                    self.reset_game()
                else:
                    break
            if self.game_manager.quit_game():
                break


if __name__ == "__main__":
    game = Breakout()
    game.mainloop()
