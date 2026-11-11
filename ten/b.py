import tkinter as tk

root = tk.Tk()
cvs = tk.Canvas(root, width=400, height=250, bg="#F8F3C0", highlightthickness=0)
cvs.pack()

cvs.create_line(50, 50, 350, 50, fill="#6194FA", width=7)
cvs.create_rectangle(50, 90, 150, 190, fill="#F58C9F", width=1)
cvs.create_oval(200, 90, 300, 190, fill="#88EBD4", width=1, dash=(5, 2))

root.mainloop()

root = tk.Tk()
cvs = tk.Canvas(root, width=400, height=300, bg="white")
cvs.pack()

cvs.create_text(200, 50, text="Canvas 입니다.", font=("Arial", 15, "bold"), fill="purple")

try:
    img = tk.PhotoImage(file="image.png")
    cvs.image = img 
    cvs.create_image(200, 180, image=img, anchor="center")
except tk.TclError:
    cvs.create_text(200, 180, text="(이미지가 없습니다.)")

root.mainloop()

def move_circle():
    cvs.move("my_circle", 5, 0)
    coords = cvs.coords("my_circle")

    if coords[2] < 400:
        root.after(50, move_circle)

root = tk.Tk()
cvs = tk.Canvas(root, width=400, height=200, bg="white")
cvs.pack()

cvs.create_oval(10, 80, 50, 120, fill="blue", tags="my_circle")

btn = tk.Button(root, text="이동 시작", command=move_circle)
btn.pack(pady=10)

root.mainloop()
old_x, old_y = None, None

def start_draw(event):
    global old_x, old_y
    old_x, old_y = event.x, event.y

def draw_line(event):
    global old_x, old_y
    if old_x and old_y:
        cvs.create_line(old_x, old_y, event.x, event.y, width=2, fill="black")
        old_x, old_y = event.x, event.y

root = tk.Tk()

cvs = tk.Canvas(root, width=400, height=300, bg="white", cursor="crosshair")
cvs.pack()

cvs.bind("<Button-1>", start_draw)
cvs.bind("<B1-Motion>", draw_line)

root.mainloop()