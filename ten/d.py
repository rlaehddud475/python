import tkinter as tk

root = tk.Tk()

message = tk.StringVar()
message.set("데이터 상태와 바인딩")

lbl = tk.Label(root, textvariable=message)
lbl.pack(padx=20, pady=20)

root.mainloop()

root = tk.Tk()

floor = tk.IntVar()
floor.set(1)

lbl = tk.Label(root, textvariable=floor, font=("맑은 고딕", 30))
lbl.pack(padx=30, pady=20)

def go_up():
    floor.set(floor.get() + 1)

btn = tk.Button(root, text="올라가기", command=go_up, width=10)
btn.pack(pady=5)

root.mainloop()