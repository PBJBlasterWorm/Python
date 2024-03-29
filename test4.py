import tkinter as tk

def get_button_text(text):
    if input_entry.get() == "":
        input_entry.delete(0, tk.END)
        input_entry.insert(0, text)
    else:
        destination_entry.delete(0, tk.END)
        destination_entry.insert(0, text)

root = tk.Tk()

subway_lines_1 = ["Subway 1", "Subway 2", "Subway 3"]  # 예시 버튼 텍스트 리스트

for i in range(len(subway_lines_1)):
    text = subway_lines_1[i]
    button = tk.Button(root, text=text, command=lambda t=text: get_button_text(t))
    button.place(x=5, y=5)

input_entry = tk.Entry(root)
input_entry.pack()

destination_entry = tk.Entry(root)
destination_entry.pack()

root.mainloop()
