import tkinter as tk

current_color = "black"
current_width = 3
current_tool = "pencil"

start_x, start_y = None, None
old_x, old_y = None, None
temp_shape = None

def set_color(color):
    global current_color, current_tool
    current_color = color
    if color != "white":
        current_tool = "pencil"

def set_eraser():
    global current_color, current_tool
    current_color = "white"
    current_tool = "pencil"

def set_tool(tool):
    global current_tool
    current_tool = tool

def set_width(val):
    global current_width
    current_width = int(val)

def start_draw(event):
    global start_x, start_y, old_x, old_y, temp_shape
    start_x, start_y = event.x, event.y
    old_x, old_y = event.x, event.y
    if current_tool == "rect":
        temp_shape = cvs.create_rectangle(start_x, start_y, start_x, start_y, outline=current_color, width=current_width)
    elif current_tool == "oval":
        temp_shape = cvs.create_oval(start_x, start_y, start_x, start_y, outline=current_color, width=current_width)

def draw_line(event):
    global old_x, old_y, temp_shape
    if current_tool == "pencil":
        if old_x and old_y:
            cvs.create_line(old_x, old_y, event.x, event.y, width=current_width, fill=current_color, capstyle=tk.ROUND, smooth=True)
            old_x, old_y = event.x, event.y
    elif current_tool == "rect" and temp_shape:
        cvs.coords(temp_shape, start_x, start_y, event.x, event.y)
    elif current_tool == "oval" and temp_shape:
        cvs.coords(temp_shape, start_x, start_y, event.x, event.y)

def stop_draw(event):
    global temp_shape
    temp_shape = None

def clear_canvas():
    cvs.delete("all")

root = tk.Tk()
root.title("그림판")

top_frame = tk.Frame(root)
top_frame.pack(pady=5)

colors = [
    ("검정", "black"),
    ("빨강", "red"),
    ("파랑", "blue"),
    ("초록", "green"),
    ("노랑", "#FFD700")
]

for name, code in colors:
    b = tk.Button(top_frame, text=name, bg=code, fg="white" if code != "#FFD700" else "black", width=5, command=lambda c=code: set_color(c))
    b.pack(side=tk.LEFT, padx=2)

eraser_btn = tk.Button(top_frame, text="지우개", bg="white", fg="black", width=5, command=set_eraser)
eraser_btn.pack(side=tk.LEFT, padx=2)

rect_btn = tk.Button(top_frame, text="사각형", width=5, command=lambda: set_tool("rect"))
rect_btn.pack(side=tk.LEFT, padx=2)

oval_btn = tk.Button(top_frame, text="원", width=5, command=lambda: set_tool("oval"))
oval_btn.pack(side=tk.LEFT, padx=2)

clear_btn = tk.Button(top_frame, text="전체 삭제", bg="lightgray", command=clear_canvas)
clear_btn.pack(side=tk.LEFT, padx=10)

bottom_frame = tk.Frame(root)
bottom_frame.pack(pady=2)

width_label = tk.Label(bottom_frame, text="굵기:")
width_label.pack(side=tk.LEFT, padx=5)

width_slider = tk.Scale(bottom_frame, from_=1, to=20, orient=tk.HORIZONTAL, command=set_width)
width_slider.set(3)
width_slider.pack(side=tk.LEFT)

cvs = tk.Canvas(root, width=400, height=300, bg="white", cursor="crosshair")
cvs.pack(padx=10, pady=5)

cvs.bind("<Button-1>", start_draw)
cvs.bind("<B1-Motion>", draw_line)
cvs.bind("<ButtonRelease-1>", stop_draw)

root.mainloop()