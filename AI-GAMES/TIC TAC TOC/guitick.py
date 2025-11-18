import tkinter as tk

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe with AI (Minimax)")
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.player_symbol = "X"
        self.ai_symbol = "O"
        self.create_board()

    def create_board(self):
        for r in range(3):
            for c in range(3):
                btn = tk.Button(self.root, text=" ", font=("Arial", 24), width=5, height=2,
                                command=lambda row=r, col=c: self.player_move(row, col))
                btn.grid(row=r, column=c)
                self.buttons[r][c] = btn

    def player_move(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.player_symbol
            self.buttons[row][col].config(text=self.player_symbol, state="disabled")
            if self.check_winner(self.player_symbol):
                self.end_game("You win!")
            elif self.is_full():
                self.end_game("It's a draw!")
            else:
                self.root.after(500, self.ai_move)

    def ai_move(self):
        row, col = self.get_best_move()
        self.board[row][col] = self.ai_symbol
        self.buttons[row][col].config(text=self.ai_symbol, state="disabled")
        if self.check_winner(self.ai_symbol):
            self.end_game("AI wins!")
        elif self.is_full():
            self.end_game("It's a draw!")

    def get_best_move(self):
        best_score = float('-inf')
        best_move = None
        for r in range(3):
            for c in range(3):
                if self.board[r][c] == " ":
                    self.board[r][c] = self.ai_symbol
                    score = self.minimax(False)
                    self.board[r][c] = " "
                    if score > best_score:
                        best_score = score
                        best_move = (r, c)
        return best_move

    def minimax(self, is_maximizing):
        if self.check_winner(self.ai_symbol):
            return 1
        elif self.check_winner(self.player_symbol):
            return -1
        elif self.is_full():
            return 0

        if is_maximizing:
            best_score = float('-inf')
            for r in range(3):
                for c in range(3):
                    if self.board[r][c] == " ":
                        self.board[r][c] = self.ai_symbol
                        score = self.minimax(False)
                        self.board[r][c] = " "
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for r in range(3):
                for c in range(3):
                    if self.board[r][c] == " ":
                        self.board[r][c] = self.player_symbol
                        score = self.minimax(True)
                        self.board[r][c] = " "
                        best_score = min(score, best_score)
            return best_score

    def check_winner(self, player):
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)): return True
            if all(self.board[j][i] == player for j in range(3)): return True
        if all(self.board[i][i] == player for i in range(3)): return True
        if all(self.board[i][2 - i] == player for i in range(3)): return True
        return False

    def is_full(self):
        return all(cell != " " for row in self.board for cell in row)

    def end_game(self, message):
        for row in self.buttons:
            for btn in row:
                btn.config(state="disabled")
        result = tk.Label(self.root, text=message, font=("Arial", 18), fg="blue")
        result.grid(row=3, column=0, columnspan=3)

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
