from tkinter import *

root = Tk()
root.title("하하하하하")
root.geometry("640x480")

message = Text(root, width=30, height=5) #텍스트 위젯 구현
message.pack()

message.insert(END, "글자를 입력하세요") # 위젯에 기본글자 넣기

entry = Entry(root, width=30)
entry.pack()
entry.insert(0, "한 줄만 입력하세요")

def btncmd():
    # 내용 출력
    print(message.get("1.0", END)) # 1 : 첫번째 라인, 0 : 0번째 column 위치(column=열)
    print(entry.get())
    
    # 내용 삭제
    message.delete("1.0", END)
    entry.delete(0, END)
    
btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()