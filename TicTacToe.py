import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.current_player = "X"
        self.board = [["", "", ""], ["", "", ""], ["", "", ""]]
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")

        self.buttonsGrid = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.window, text="", width=20, height=10)
                button.grid(row=i, column=j)
                button.config(command=lambda row=i, col=j: self.make_move(row, col))
                row.append(button)
            self.buttonsGrid.append(row)

    def make_move(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttonsGrid[row][col].config(text=self.current_player)

            if self.check_winner(self.current_player):
                messagebox.showinfo("Game Over", f"Winner: {self.current_player}")
                self.disable_buttons()
                self.window.quit()
            elif self.is_draw():
                messagebox.showinfo("Game Over", "It's a Draw!")
                self.disable_buttons()
                self.window.quit()

            self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self, player):
        # Check rows
        for row in self.board:
            if all(cell == player for cell in row):
                return True

        # Check columns
        for col in range(3):
            if all(row[col] == player for row in self.board):
                return True

        # Check diagonals
        if all(self.board[i][i] == player for i in range(3)) or \
           all(self.board[i][2 - i] == player for i in range(3)):
            return True

        return False

    def is_draw(self):
        for row in self.board:
            if "" in row:
                return False
        return True

    def disable_buttons(self):
        for row in self.buttonsGrid:
            for button in row:
                button.config(state=tk.DISABLED)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
