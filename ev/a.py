# # import tkinter as tk
# import tkinter as tk

# root = tk.Tk()
# # root = tk.Tk()
# # # root.title("이곳이 제목 표시줄")
# # # root.geometry("200x50")
# # # root.title("창 위치 설정")
# # # root.geometry("400x300+100+200")
# # # root.geometry("200x50")
# # # root.configure(bg="lightblue")
# root.geometry("400x300")
# # # root.resizable(False, False)
# # # root.geometry("400x300")
# # # root.minsize(300, 200)
# # # root.maxsize(800, 600)
# # # root.mainloop()


# # # lbl = tk.Label(root, text="라벨입니다.")
# # # lbl.pack()

# # root.mainloop()
# bold_btn = tk.Button(root, text="두꺼운 테두리", bd=5, relief="raised", width=15)
# bold_btn.pack(pady=5)

# cursor_btn = tk.Button(root, text="커서 변경 (손가락)", cursor="hand2", bg="lightyellow")
# cursor_btn.pack(pady=5)

# disabled_btn = tk.Button(root, text="클릭 불가", state="disabled")
# disabled_btn.pack(pady=5)

# root.mainloop()

# lbl = tk.Label(
#     root,
#     text="Python GUI",
#     font=("맑은 고딕", 16),
#     fg="white",
#     bg="navy"
# )
# lbl.pack(padx=40,pady=10)

# root.mainloop()
# def hello():
#     lbl.config(text="버튼을 클릭했습니다!")

# root = tk.Tk()

# lbl = tk.Label(root, text="버튼을 눌러보세요", padx=40, pady=10)
# lbl.pack()

# btn = tk.Button(root, text="클릭", command=hello)
# btn.pack()

# root.mainloop()

import tkinter as tk

def change_text():
    text = ent.get()
    ent.delete(0, tk.END)
    ent.insert(0, text.upper())

root = tk.Tk()
password_ent = tk.Entry(root, show="*", width=30)
password_ent.pack(pady=20)
txt = tk.Text(root)
txt.pack(pady=10)
ent = tk.Entry(root)
ent.pack(padx=10, pady=10)

btn = tk.Button(root, text="대문자로 변경", command=change_text)
btn.pack(padx=10, pady=10)

def show_result():
    if agree_var.get():
        lbl.config(text="동의했습니다.")

root = tk.Tk()
agree_var = tk.BooleanVar()

check_btn = tk.Checkbutton(root, text="동의합니다", variable=agree_var, command=show_result)
check_btn.pack(padx=20, pady=20)

lbl = tk.Label(root, text="")
lbl.pack(pady=10)

food = tk.IntVar(value=1)

rb_meat = tk.Radiobutton(root, text="육고기", variable=food, value=1)
rb_seafood = tk.Radiobutton(root, text="해산물", variable=food, value=2)
rb_meat.pack()
rb_seafood.pack()
def show_selected(event):
    selection = lang_lb.curselection()
    if selection:
        result_lbl.config(text="선택한 항목: " + lang_lb.get(selection[0]))

root = tk.Tk()
lang_lb = tk.Listbox(root, height=5)
lang_lb.pack(padx=10, pady=10)

for item in ["Python", "Java", "JavaScript", "C", "C++"]:
    lang_lb.insert(tk.END, item)

lang_lb.bind("<<ListboxSelect>>", show_selected)

result_lbl = tk.Label(root, text="")
result_lbl.pack(pady=10)
def show_value():
    lbl.config(text=f"선택한 밝기: {scl.get()}")

root = tk.Tk()

scl = tk.Scale(root, from_=0, to=100, orient="vertical")
scl.pack(pady=10)

tk.Button(root, text="확인", command=show_value).pack()

lbl = tk.Label(root)
lbl.pack(pady=10)

def change_value(value):
    lbl.config(text=f"현재 값: {value}")

root = tk.Tk()

scl = tk.Scale(root, from_=0, to=100, orient="horizontal", command=change_value)
scl.pack(pady=10)

lbl = tk.Label(root, text="현재 값: 0")
lbl.pack(pady=10)
root.geometry("200x150")

tk.Label(root, text="첫 번째 라벨 위젯", bg="red").pack()
tk.Label(root, text="두 번째 라벨 위젯", bg="green").pack()
tk.Label(root, text="세 번째 라벨 위젯", bg="yellow").pack()
tk.Button(root, text="LEFT").pack(side="left")
tk.Button(root, text="RIGHT").pack(side="right")
x_btn = tk.Button(root, text="가로만 채우기")
b_btn = tk.Button(root, text="전체 확장")
x_btn.pack(fill="x")
b_btn.pack(expand=True, fill="both")

tk.Label(root, text="이름").grid(row=0, column=0)
tk.Entry(root).grid(row=0, column=1)
tk.Label(root, text="나이").grid(row=1, column=0)
tk.Entry(root).grid(row=1, column=1)
root = tk.Tk()
root.grid_columnconfigure(1, weight=1)      # 1번 열만 늘어남

opt = {"padx": 5, "pady": 5}
tk.Label(root, text="이메일 주소", bg="lightblue").grid(row=1, column=0, sticky="w", **opt)            # 왼쪽 정렬
tk.Entry(root, bg="lightyellow").grid(row=1, column=1, sticky="we", **opt)                      # 좌우로 꽉 참
tk.Button(root, text="로그인", bg="lightgreen").grid(row=2, columnspan=2, sticky="we", **opt)  # 두 열 차지

tk.Label(root, text="절대 위치 (50, 30)", bg="lightblue").place(x=50, y=30) # 절대 좌표 배치 (x, y는 픽셀)

tk.Label(root, text="상대 좌표 배치 (정중앙)", bg="lightgreen").place(
    relx=0.5, rely=0.5, anchor="center"
) # 상대 좌표 배치 (relx, rely는 0.0 ~ 1.0 비율)

tk.Label(root, text="상대 크기 지정 (너비 80%)", bg="lightyellow").place(
    relx=0.1, rely=0.8, relwidth=0.8
) # 상대 크기 지정 (relwidth, relheight)
root.geometry("360x150")
root.configure(bg="#797777")

# 위쪽 프레임: 입력 폼 (내부는 grid)
top_frm = tk.Frame(root, bg="#d7ecff", padx=5, pady=5)
top_frm.pack(side="top", fill="x", padx=5, pady=5)

tk.Label(top_frm, text="이메일 주소", bg="#d7ecff").grid(row=0, column=0, sticky="w", padx=(0, 8))
tk.Entry(top_frm, bg="white").grid(row=0, column=1, sticky="we")
top_frm.grid_columnconfigure(1, weight=1)  # 입력칸이 가로로 늘어나도록

# 아래쪽 프레임: 버튼 (내부는 pack)
bottom_frm = tk.Frame(root, bg="#ffe0e0", padx=5, pady=5)
bottom_frm.pack(side="bottom", fill="x", padx=5, pady=5)

tk.Button(bottom_frm, text="확인", bg="#7bc96f", fg="white", width=8).pack(side="left")
tk.Button(bottom_frm, text="취소", bg="#e87a7a", fg="white", width=8).pack(side="right")
def order_coffee():
    lbl.config(text="아메리카노 주문 완료!")
lbl = tk.Label(root, text="메뉴를 골라 주세요")
lbl.pack(padx=20, pady=10)

btn = tk.Button(root, text="아메리카노", command=order_coffee)
btn.pack(padx=20, pady=10)

def order(menu):
    lbl.config(text=f"{menu} 주문 완료!")

root = tk.Tk()

lbl = tk.Label(root, text="메뉴를 골라 주세요")
lbl.pack(padx=20, pady=10)

for menu in ["아메리카노", "카페라테", "바닐라라테"]:
    btn = tk.Button(root, text=menu, command=lambda m=menu: order(m))
    btn.pack(fill="x", padx=20, pady=2)
def on_scale(value):
    lbl.config(text=f"샷 추가 : {value}번")

root = tk.Tk()

lbl = tk.Label(root, text="샷 추가 : 0번")
lbl.pack(padx=20, pady=10)

scl = tk.Scale(root, from_=0, to=4, orient="horizontal", command=on_scale)
scl.pack(padx=20, pady=10)
def on_key(event):
    lbl.config(text=f"문자 : {event.char}  /  키 이름 : {event.keysym}")

root = tk.Tk()

ent = tk.Entry(root, width=30)
ent.pack(padx=20, pady=10)

lbl = tk.Label(root, text="키를 눌러 보세요", bg="lightyellow")
lbl.pack(padx=20, pady=10)

ent.bind("<Key>", on_key)
root.mainloop()
