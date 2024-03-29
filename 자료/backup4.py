import tkinter as tk
from tkinter import messagebox
import random

class OmokGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Omok Game")

        self.canvas = tk.Canvas(master, width=600, height=700, bg="tan")
        self.canvas.pack()

        self.board_size = 19
        self.cell_size = 25
        self.margin = 80

        self.board = [[0 for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.turn = 1
        self.game_over = False

        self.draw_board()
        self.canvas.bind("<Button-1>", self.click_handler)

        self.time_limit = 3
        self.timer_label = tk.Label(master, text="Time Left: ", font=("맑은고딕", 16))
        self.timer_label.pack(side="bottom")

        self.timer_event = None
        self.create_menu()

    def create_menu(self):
        menu_bar = tk.Menu(self.master)

        game_menu = tk.Menu(menu_bar, tearoff=0)
        game_menu.add_command(label="New Game", command=self.restart_game)
        game_menu.add_separator()
        game_menu.add_command(label="Exit", command=self.master.quit)
        menu_bar.add_cascade(label="Game", menu=game_menu)

        self.master.config(menu=menu_bar)

    def draw_board(self):
        for i in range(self.board_size):
            start = self.margin + i * self.cell_size
            self.canvas.create_line(self.margin, start, self.margin + (self.board_size - 1) * self.cell_size, start)
            self.canvas.create_line(start, self.margin, start, self.margin + (self.board_size - 1) * self.cell_size)

    def click_handler(self, event):
        if not self.game_over:
            col = round((event.x - self.margin) / self.cell_size)
            row = round((event.y - self.margin) / self.cell_size)
            if 0 <= row < self.board_size and 0 <= col < self.board_size and self.board[row][col] == 0:
                self.draw_piece(row, col)
                self.check_winner(row, col)
                self.reset_timer()
                self.ai_move()  # AI의 수를 놓습니다.

    def draw_piece(self, row, col):
        x = self.margin + col * self.cell_size
        y = self.margin + row * self.cell_size
        if self.turn == 1:
            self.canvas.create_oval(x - 11, y - 11, x + 11, y + 11, fill="black")
            self.board[row][col] = 1
            self.turn = -1
        else:
            self.canvas.create_oval(x - 11, y - 11, x + 11, y + 11, fill="white")
            self.board[row][col] = -1
            self.turn = 1

    def check_winner(self, row, col):
        player = self.board[row][col]
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        for d in directions:
            count = self.count_consecutive(row, col, d[0], d[1], player) + self.count_consecutive(row, col, -d[0], -d[1], player) + 1
            if count == 5:
                self.game_over = True
                self.show_winner(player)
                return

    def count_consecutive(self, row, col, d_row, d_col, player):
        count = 0
        r, c = row + d_row, col + d_col
        while 0 <= r < self.board_size and 0 <= c < self.board_size and self.board[r][c] == player:
            count += 1
            r, c = r + d_row, c + d_col
        return count

    def show_winner(self, player):
        winner = "Black" if player == 1 else "White"
        messagebox.showinfo("Game Over", f"{winner} wins!")

    def start_timer(self):
        self.timer_event = self.master.after(1000, self.update_timer)

    def update_timer(self):
        if not self.game_over:
            self.time_limit -= 1
            self.timer_label.config(text=f"Time Left: {self.time_limit}")
            if self.time_limit <= 0:
                self.place_random_piece()
                self.reset_timer()
                self.ai_move()  # AI의 수를 놓습니다.
            else:
                self.timer_event = self.master.after(1000, self.update_timer)

    def reset_timer(self):
        if self.timer_event:
            self.master.after_cancel(self.timer_event)
        self.time_limit = 3
        self.timer_label.config(text="Time Left: 3")
        self.start_timer()

    def place_random_piece(self):
        empty_cells = [(i, j) for i in range(self.board_size) for j in range(self.board_size) if self.board[i][j] == 0]
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.draw_piece(row, col)
        else:
            self.game_over = True
            messagebox.showinfo("Game Over", "No more empty cells.")

    def restart_game(self):
        self.canvas.delete("all")
        self.board = [[0 for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.game_over = False
        self.draw_board()
        self.reset_timer()

    def ai_move(self):
        if not self.game_over:
            best_score = -float("inf")
            best_move = None
            for i in range(self.board_size):
                for j in range(self.board_size):
                    if self.board[i][j] == 0:
                        self.board[i][j] = -1
                        score = self.minimax(self.board, 2, False, -float("inf"), float("inf"))
                        self.board[i][j] = 0
                        if score > best_score:
                            best_score = score
                            best_move = (i, j)
            if best_move:
                self.draw_piece(best_move[0], best_move[1])
                self.check_winner(best_move[0], best_move[1])
                self.reset_timer()

    def minimax(self, board, depth, is_maximizing, alpha, beta):
        if depth == 0 or self.game_over:
            return self.evaluate_board(board)
        
        if is_maximizing:
            max_eval = -float("inf")
            for i in range(self.board_size):
                for j in range(self.board_size):
                    if board[i][j] == 0:
                        board[i][j] = -1
                        eval = self.minimax(board, depth - 1, False, alpha, beta)
                        board[i][j] = 0
                        max_eval = max(max_eval, eval)
                        alpha = max(alpha, eval)
                        if beta <= alpha:
                            break
            return max_eval
        else:
            min_eval = float("inf")
            for i in range(self.board_size):
                for j in range(self.board_size):
                    if board[i][j] == 0:
                        board[i][j] = 1
                        eval = self.minimax(board, depth - 1, True, alpha, beta)
                        board[i][j] = 0
                        min_eval = min(min_eval, eval)
                        beta = min(beta, eval)
                        if beta <= alpha:
                            break
            return min_eval

    def evaluate_board(self, board):
        # 각 셀을 평가하여 점수를 매깁니다.
        # 더 복잡한 평가 기준을 도입하여 AI를 개선할 수 있습니다.
        score = 0
        return score

def main():
    root = tk.Tk()
    game = OmokGame(root)
    game.start_timer()
    root.mainloop()

if __name__ == "__main__":
    main()
