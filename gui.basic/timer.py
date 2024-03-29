import time
import tkinter
from datetime import datetime

root = tkinter.Tk()
root.geometry("640x480")
root.title("시계 타이머")

def clock_time():
    timer = datetime.now().strftime("%Y-%M-%D %H:%M:%S")
    clock.config(text=timer)
    clock.after(1000, sec)

clock = tkinter.Label(root, font=("고딕", 15), fg="green")
clock.pack()

sec()

root.mainloop()



    
    
