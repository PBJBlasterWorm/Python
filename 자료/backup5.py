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
                self.ai_move(row, col)  # AI의 수를 놓습니다.

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

    def ai_move(self, row, col):
        if not self.game_over:
            # AI가 놓을 수 있는 후보 위치를 계산합니다.
            candidate_positions = []
            for i in range(max(0, row - 1), min(self.board_size, row + 1)):  # 행 범위를 늘려 검사합니다.
                for j in range(max(0, col - 1), min(self.board_size, col + 1)):  # 열 범위를 늘려 검사합니다.
                    if self.board[i][j] == 0:
                        candidate_positions.append((i, j))

            if candidate_positions:
                for pos in candidate_positions:
                    i, j = pos
                    # 해당 위치에 돌을 놓았을 때 3개 이상의 돌이 연속되는지 검사합니다.
                    if self.count_consecutive(i, j, 0, 1, self.turn) >= 3 \
                            or self.count_consecutive(i, j, 1, 0, self.turn) >= 3 \
                            or self.count_consecutive(i, j, 1, 1, self.turn) >= 3 \
                            or self.count_consecutive(i, j, 1, -1, self.turn) >= 3:
                        continue  # 3개 이상의 돌이 연속되는 경우 해당 위치를 무시합니다.
                    # 3개 이상의 돌이 연속되지 않는 경우 해당 위치에 돌을 놓고 종료합니다.
                    self.draw_piece(i, j)
                    self.check_winner(i, j)
                    self.reset_timer()
                    return
                # 모든 후보 위치에 대해 3개 이상의 돌이 연속되는 경우가 없으면 무작위로 선택하여 돌을 놓습니다.
                row, col = random.choice(candidate_positions)
                self.draw_piece(row, col)
                self.check_winner(row, col)
                self.reset_timer()



def main():
    root = tk.Tk()
    game = OmokGame(root)
    game.start_timer()
    root.mainloop()

if __name__ == "__main__":
    main()