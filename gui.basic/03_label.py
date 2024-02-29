from tkinter import *

root = Tk()
root.title("하하하하하")
root.geometry("640x480")

label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file="gui.basic\img.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="또 만나요") #글자 변경하는 기능
    
    global photo2
    photo2 = PhotoImage(file="gui.basic\img2.png")
    label2.config(image=photo2)

btn = Button(root, text="클릭", command=change) #command 기능구현
btn.pack()

root.mainloop()