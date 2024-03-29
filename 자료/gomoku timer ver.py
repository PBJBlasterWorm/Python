import tkinter as tk
from tkinter import messagebox
import random

class OmokGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Omok Game")

        self.canvas = tk.Canvas(master, width=600, height=700, bg="tan")
        self.canvas.pack()

        self.board_size = 20
        self.cell_size = 25
        self.margin = 60

        self.board = [[0 for _ in range(self.board_size)] for _ in range(self.board_size)]  # 20x20 보드 생성
        self.turn = 1  # 1: 흑돌, -1: 백돌
        self.game_over = False

        self.draw_board()
        self.canvas.bind("<Button-1>", self.click_handler)

        self.time_limit = 3
        self.timer_label = tk.Label(master, text="Time Left: ", font=("맑은고딕", 16))
        self.timer_label.pack(side="bottom")

        self.timer_event = None  # 타이머 이벤트 변수 추가
        self.create_menu()
        
    def create_menu(self):
        menu_bar = tk.Menu(self.master)

        game_menu = tk.Menu(menu_bar, tearoff=0)
        game_menu.add_command(label="새 게임", command=self.restart_game)
        game_menu.add_separator()
        game_menu.add_command(label="종료", command=self.master.quit)
        menu_bar.add_cascade(label="게임", menu=game_menu)

        self.master.config(menu=menu_bar)

    def draw_board(self):
        for i in range(self.board_size):
            start = self.margin + i * self.cell_size
            self.canvas.create_line(self.margin, start, self.margin + (self.board_size - 1) * self.cell_size, start)  # 수평선
            self.canvas.create_line(start, self.margin, start, self.margin + (self.board_size - 1) * self.cell_size)  # 수직선

    def click_handler(self, event):
        if not self.game_over:
            col = round((event.x - self.margin) / self.cell_size)
            row = round((event.y - self.margin) / self.cell_size)
            if 0 <= row < self.board_size and 0 <= col < self.board_size and self.board[row][col] == 0:
                self.draw_piece(row, col)
                self.check_winner(row, col)
                self.reset_timer()

                # 컴퓨터 턴
                if not self.game_over:
                    self.computer_turn()

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
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]  # 가로, 세로, 대각선(↘), 대각선(↗)
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
        winner = "흑돌" if player == 1 else "백돌"
        messagebox.showinfo("게임 종료", f"{winner}이(가) 승리했습니다!")

    def start_timer(self):
        self.timer_event = self.master.after(1000, self.update_timer)

    def update_timer(self):
        if not self.game_over:
            self.time_limit -= 1
            self.timer_label.config(text=f"Time Left: {self.time_limit}")
            if self.time_limit <= 0:
                self.place_random_piece()
                self.reset_timer()
            else:
                self.timer_event = self.master.after(1000, self.update_timer)

    def reset_timer(self):
        if self.timer_event:
            self.master.after_cancel(self.timer_event)  # 이전 타이머 이벤트를 취소
        self.time_limit = 3
        self.timer_label.config(text="Time Left: 3")
        self.start_timer()  # 타이머 재시작

    def place_random_piece(self):
        empty_cells = [(i, j) for i in range(self.board_size) for j in range(self.board_size) if self.board[i][j] == 0]
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.draw_piece(row, col)
        else:
            self.game_over = True
            messagebox.showinfo("게임 종료", "더 이상 놓을 수 있는 자리가 없습니다.")

    def computer_turn(self):
        # 간단한 미니맥스 알고리즘 구현
        best_score = float("-inf")
        best_move = None
        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.board[i][j] == 0:
                    self.board[i][j] = -1
                    score = self.minimax(self.board, 0, False)
                    self.board[i][j] = 0
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        if best_move:
            self.draw_piece(best_move[0], best_move[1])
            self.check_winner(best_move[0], best_move[1])
            self.reset_timer()

    def minimax(self, board, depth, is_maximizing):
        result = self.check_winner_util(board)
        if result != 0:
            return result

        if is_maximizing:
            best_score = float("-inf")
            for i in range(self.board_size):
                for j in range(self.board_size):
                    if board[i][j] == 0:
                        board[i][j] = -1
                        score = self.minimax(board, depth + 1, False)
                        board[i][j] = 0
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float("inf")
            for i in range(self.board_size):
                for j in range(self.board_size):
                    if board[i][j] == 0:
                        board[i][j] = 1
                        score = self.minimax(board, depth + 1, True)
                        board[i][j] = 0
                        best_score = min(score, best_score)
            return best_score

    def check_winner_util(self, board):
        for i in range(self.board_size):
            for j in range(self.board_size):
                if board[i][j] != 0:
                    player = board[i][j]
                    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
                    for d in directions:
                        count = self.count_consecutive_util(board, i, j, d[0], d[1], player) + \
                                self.count_consecutive_util(board, i, j, -d[0], -d[1], player) + 1
                        if count == 5:
                            return player
        return 0

    def count_consecutive_util(self, board, row, col, d_row, d_col, player):
        count = 0
        r, c = row + d_row, col + d_col
        while 0 <= r < self.board_size and 0 <= c < self.board_size and board[r][c] == player:
            count += 1
            r, c = r + d_row, c + d_col
        return count

    def restart_game(self):
        self.canvas.delete("all")
        self.board = [[0 for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.game_over = False
        self.draw_board()
        self.reset_timer()

def main():
    root = tk.Tk()
    game = OmokGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
