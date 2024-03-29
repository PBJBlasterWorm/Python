import tkinter
from tkinter import *

win = tkinter.Tk()

def enter(btn):
    if btn == 'C':
        ent.delete(0,END)
    elif btn == '=':
        ar = eval(ent.get())
        ent.delete(0,END)
        ent.insert(END,ar)
    else:
        ent.insert(END,btn)

ent = Entry(win,width=15,justify="right",font=("궁서체",40))
ent.pack(pady=5)


buttons = ['7410','852=','963+','C/*-']
for col in buttons:
    frm = Frame(win)
    frm.pack(side="left")
    for row in col:
        btn = Button(frm, text=row,width=5,height=2,font=(30),command=lambda char=row:enter(char))
        btn.pack(fill='x',padx=15,pady=15)

win.mainloop()