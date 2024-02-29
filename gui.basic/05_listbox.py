from tkinter import *

root = Tk()
root.title("하하하하하")
root.geometry("640x480")

eat = Listbox(root, selectmode="extended", height=0) # single = 한개만 선택
eat.insert(0, "사과")                       # extended = 여러개 선택가능
eat.insert(1, "딸기")
eat.insert(2, "바나나")
eat.insert(END, "수박")
eat.insert(END, "포도")
eat.pack()

def btncmd():
   # 삭제
   # listbox.delete(0) # 맨 앞에 항목을 삭제

   # 갯수 확인
    print("리스트에는", eat.size(), "개가 있어요")
   
   # 항목 확인 (시작 index, 끝 index)
    print("1번째부터 3번째까지의 항목 : ", eat.get(0, 2))

   # 선택된 항목 확인 (위치로 반환 (ex) (1,2,3))
    print("선택된 항목 : ", eat.curselection())




btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()