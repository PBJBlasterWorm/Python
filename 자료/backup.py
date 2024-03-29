
import tkinter as tk
from tkinter import messagebox
import random

class GameMenu(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Game Menu")
        self.geometry("400x300")

        self.current_frame = None

        self.show_menu()

    def show_menu(self):
        if self.current_frame is not None:
            self.current_frame.destroy()

        self.current_frame = tk.Frame(self)
        self.current_frame.pack(padx=20, pady=20)

        label = tk.Label(self.current_frame, text="게임을 선택하세요", font=("Helvetica", 20))
        label.pack(pady=20)

        omok_btn = tk.Button(self.current_frame, text="오목", command=self.play_omok)
        omok_btn.pack(pady=10)

        snake_btn = tk.Button(self.current_frame, text="스네이크 게임", command=self.play_snake)
        snake_btn.pack(pady=10)

        logic_btn = tk.Button(self.current_frame, text="네모네모로직", command=self.play_logic)
        logic_btn.pack(pady=10)

        home_btn = tk.Button(self.current_frame, text="홈", command=self.show_menu)
        home_btn.pack(pady=20)

    def play_omok(self):
        omok_window = tk.Toplevel(self)
        omok_window.title("오목 게임")
        omok_window.geometry("400x400")
        board = OmokBoard(omok_window)
        board.pack()

    def play_snake(self):
        snake_window = tk.Toplevel(self)
        snake_window.title("스네이크 게임")
        snake_window.geometry("400x400")
        snake_game = SnakeGame(snake_window)
        snake_game.pack()

    def play_logic(self):
        logic_window = tk.Toplevel(self)
        logic_window.title("네모네모로직 게임")
        logic_window.geometry("400x400")
        logic_game = NemoLogicGame(logic_window)
        logic_game.pack()

class OmokBoard(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_board()

    def create_board(self):
        self.cells = [[None for _ in range(15)] for _ in range(15)]
        for row in range(15):
            for col in range(15):
                cell = tk.Label(self, width=2, height=1, bg="white", relief="ridge")
                cell.grid(row=row, column=col)
                cell.bind("<Button-1>", lambda event, r=row, c=col: self.place_piece(r, c))

    def place_piece(self, row, col):
        if self.cells[row][col] is None:
            piece_color = "black" if random.random() > 0.5 else "white"
            piece = tk.Label(self, width=2, height=1, bg=piece_color, relief="ridge")
            piece.grid(row=row, column=col)
            self.cells[row][col] = piece_color
            # 여기에 오목 게임 로직 추가 가능

class SnakeGame(tk.Canvas):
    def __init__(self, master):
        super().__init__(master, width=400, height=400, bg="black")
        self.snake = [(20, 20)]
        self.food = self.set_food()
        self.direction = "Right"
        self.bind_all("<KeyPress>", self.on_key_press)
        self.draw_snake()
        self.draw_food()
        self.after(100, self.update_snake)

    def on_key_press(self, event):
        key = event.keysym
        if key in ["Left", "Right", "Up", "Down"]:
            self.direction = key

    def draw_snake(self):
        self.delete(tk.ALL)
        for x, y in self.snake:
            self.create_rectangle(x, y, x + 10, y + 10, fill="green", outline="white")

    def draw_food(self):
        x, y = self.food
        self.create_rectangle(x, y, x + 10, y + 10, fill="red", outline="white")

    def set_food(self):
        x = random.randint(0, 39) * 10
        y = random.randint(0, 39) * 10
        return x, y

    def update_snake(self):
        self.move_snake()
        self.check_collision()
        self.draw_snake()
        self.draw_food()
        self.after(100, self.update_snake)

    def move_snake(self):
        head_x, head_y = self.snake[0]
        if self.direction == "Left":
            new_head = (head_x - 10, head_y)
        elif self.direction == "Right":
            new_head = (head_x + 10, head_y)
        elif self.direction == "Up":
            new_head = (head_x, head_y - 10)
        elif self.direction == "Down":
            new_head = (head_x, head_y + 10)

        self.snake.insert(0, new_head)
        self.snake.pop()

    def check_collision(self):
        head_x, head_y = self.snake[0]
        if head_x < 0 or head_x >= 400 or head_y < 0 or head_y >= 400:
            messagebox.showinfo("Game Over", "벽에 부딪혀 게임 오버!")
            self.master.destroy()

class NemoLogicGame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_board()

    def create_board(self):
        self.cells = []
        for row in range(8):
            row_cells = []
            for col in range(8):
                color = random.choice(["red", "blue", "green", "yellow"])
                cell = tk.Label(self, width=2, height=1, bg=color, relief="ridge")
                cell.grid(row=row, column=col)
                row_cells.append(color)
            self.cells.append(row_cells)
            # 네모네모로직 게임 로직은 각 셀의 색을 클릭했을 때 변경하거나 다른 동작을 추가 가능

if __name__ == "__main__":
    app = GameMenu()
    app.mainloop()
    