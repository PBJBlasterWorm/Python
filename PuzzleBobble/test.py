import tkinter as tk
from tkinter import Button
import subprocess

def open_python_file():
    try:
        # 실행할 파이썬 파일의 경로 지정
        file_path = "PuzzleBobble/12_game_over.py"  # 실행할 파일의 경로로 수정해야 합니다.

        # 파이썬 파일 실행
        subprocess.Popen(["python", file_path])
    except Exception as e:
        print("파일을 실행하는 중 오류가 발생했습니다:", e)

def open_tkinter_window():
    # Tkinter 창 생성
    root = tk.Tk()
    root.title("Tkinter Window")

    # 버튼 생성
    btn_open_file = Button(root, text="Open Python File", command=open_python_file)
    btn_open_file.pack()

    # Tkinter 창 실행
    root.mainloop()

# Tkinter 창 열기
open_tkinter_window()
