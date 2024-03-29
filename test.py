import tkinter
from tkinter import *

root = Tk()

def enter(btn):
    if btn == "C":
        entry.delete(0, END)
    elif btn == "=":
        input = eval(entry.get())
        entry.delete(0, END)
        entry.insert(END, input)
    else:
        entry.insert(END, btn)

entry = Entry(root, width=15, justify="right", font=("맑은고딕",40))
entry.pack(pady=5)

buttons = ["1234","5678","90+=","C/*-"]
for col in buttons:
    frame = Frame(root)
    frame.pack(side="left")
    for row in col:
        btn = Button(frame, text=row, width=5, height=2, font=30, command=lambda char=row:enter(char))
        btn.pack(fill=X, padx=15, pady=15)

root.mainloop()