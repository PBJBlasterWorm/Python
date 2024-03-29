import tkinter as tk

def move_image():
    global x, y
    # 이미지의 위치를 변경
    x += dx
    y += dy
    # 이미지가 화면 밖으로 나가는 것을 방지
    if x < 0:
        x = 0
        dx *= -1
    elif x > canvas_width - image_width:
        x = canvas_width - image_width
        dx *= -1
    if y < 0:
        y = 0
        dy *= -1
    elif y > canvas_height - image_height:
        y = canvas_height - image_height
        dy *= -1
    # 이미지의 위치를 업데이트
    canvas.coords(image_id, x, y)
    # 일정 시간 후에 함수를 재호출
    root.after(interval, move_image)

root = tk.Tk()
root.title("자동 이미지 움직이기")

# 캔버스 생성
canvas_width = 400
canvas_height = 400
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

# 이미지 로드
image = tk.PhotoImage(file="Python/Metro Line Map2.png")
image_width = image.width()
image_height = image.height()

# 이미지를 캔버스에 추가
x = 100
y = 100
image_id = canvas.create_image(x, y, anchor=tk.NW, image=image)

# 이미지의 초기 이동 속도
dx = 2
dy = 2

# 이미지 이동 간격(ms)
interval = 50

# move_image 함수 호출
move_image()

root.mainloop()
