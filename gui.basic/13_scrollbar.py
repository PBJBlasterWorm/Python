from tkinter import *


root = Tk()
root.title("하하하하하")
root.geometry("640x480")

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

# set이 없으면 스크롤을 내려도 다시 올라옴(scrollbar.set)
listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand = scrollbar.set)
for i in range(1, 32): # 1 ~ 31 일
    listbox.insert(END, str(i) + "일") # 1일, 2일, ...
listbox.pack(side="left")

scrollbar.config(command=listbox.yview) # yview를 넣어서 서로 매핑하도록 해야함

root.mainloop() 