import tkinter as tk
from tkinter import ttk


root = tk.Tk()

lbl = ttk.Label(root, text="이름 : ")
lbl.grid(row=0, column=0, padx=5, pady=5)

ent = ttk.Entry(root)
ent.grid(row=0, column=1, padx=5, pady=5)

btn = ttk.Button(root, text="확인", command=lambda: print(ent.get()))
btn.grid(row=1, column=0, columnspan=2, pady=5)

root.mainloop()
print("Tk Version:", tk.TkVersion)
print("Tcl Version:", tk.TclVersion)

root = tk.Tk()

style = ttk.Style()
style.configure("TButton", font=("맑은 고딕", 11), padding=6)
style.configure("Accent.TButton", foreground="lightgreen", background="green")

basic_btn = ttk.Button(root, text="기본 버튼")
basic_btn.pack(padx=50, pady=5)

accent_btn = ttk.Button(root, text="강조 버튼", style="Accent.TButton")
accent_btn.pack(padx=50, pady=5)

root.mainloop()

root = tk.Tk()

style = ttk.Style()
print(style.theme_names())
print(style.theme_use())

root.mainloop()

root = tk.Tk()
style = ttk.Style()

frm = ttk.Frame(root, padding=20)
frm.pack()

cur = tk.StringVar(value=style.theme_use())
cmb = ttk.Combobox(frm, values=style.theme_names(), textvariable=cur, state="readonly")
cmb.pack(pady=5)
cmb.bind("<<ComboboxSelected>>", lambda e: style.theme_use(cur.get()))

ttk.Button(frm, text="버튼").pack(pady=5)
ttk.Checkbutton(frm, text="체크박스").pack(pady=5)
ttk.Progressbar(frm, value=60).pack(pady=5)

root.mainloop()
root = tk.Tk()

style = ttk.Style()
style.theme_use("clam")

style.map("TButton",
    background=[("active", "lightblue"),
                ("pressed", "blue"),
                ("disabled", "lightyellow")],
    foreground=[("disabled", "gray")])

ttk.Button(root, text="마우스를 올려보세요").pack(padx=20, pady=10)
ttk.Button(root, text="비활성 버튼", state="disabled").pack(padx=20, pady=10)

root.mainloop()