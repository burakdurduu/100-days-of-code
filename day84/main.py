class TicTacToe:
    def __init__(self):
        self.gb = [["-", "-", "-"],
                   ["-", "-", "-"],
                   ["-", "-", "-"]]
        self.current_player = "x"
        self.game_running = True

    def print_gameboard(self):
        for row in self.gb:
            print(f"{row[0]} | {row[1]} | {row[2]}")

    def player_input(self):
        while True:
            try:
                p_row = int(input(f"Current player is: {self.current_player}. Choose row (1-3): ")) - 1
                p_column = int(input(f"Current player is: {self.current_player}. Choose column (1-3): ")) - 1
                if 0 <= p_row < 3 and 0 <= p_column < 3 and self.gb[p_row][p_column] == "-":
                    self.gb[p_row][p_column] = self.current_player
                    break
                else:
                    print("Spot is not available, try again.")
            except ValueError:
                print("Invalid input, please enter numbers between 1-3.")

    def change_player(self):
        self.current_player = "o" if self.current_player == "x" else "x"

    def check_win(self):
        for i in range(3):
            if self.gb[i][0] == self.gb[i][1] == self.gb[i][2] != "-":
                return True
            elif self.gb[0][i] == self.gb[1][i] == self.gb[2][i] != "-":
                return True
        if self.gb[0][0] == self.gb[1][1] == self.gb[2][2] != "-":
            return True
        elif self.gb[0][2] == self.gb[1][1] == self.gb[2][0] != "-":
            return True
        return False

    def check_tie(self):
        for row in self.gb:
            if "-" in row:
                return False
        return True

    def game_over(self):
        if self.check_win():
            print(f"Player '{self.current_player}' has won!")
            self.game_running = False
        elif self.check_tie():
            print("It's a tie!")
            self.game_running = False

    def main(self):
        while self.game_running:
            self.print_gameboard()
            self.player_input()
            self.game_over()
            self.change_player()
        self.print_gameboard()


if __name__ == "__main__":
    game = TicTacToe()
    game.main()
