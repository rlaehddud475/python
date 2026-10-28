import tkinter as tk

root = tk.Tk()
root.geometry("400x120")

mnu_bar = tk.Menu(root)    # 1) 메뉴바 생성

file_mnu = tk.Menu(mnu_bar, tearoff=0)    # 2) 하위 메뉴 생성
file_mnu.add_command(label="열기", command=lambda: print("열기 클릭"))    # 3) 항목 채우기
file_mnu.add_separator()
file_mnu.add_command(label="종료", command=root.destroy)

mnu_bar.add_cascade(label="파일", menu=file_mnu)    # 4) 메뉴바에 연결

root.config(menu=mnu_bar)    # 5) 창에 부착


root = tk.Tk()
root.geometry("300x120")

mnu = tk.Menu(root, tearoff=0)
mnu.add_command(label="복사", command=lambda: print("복사"))
mnu.add_command(label="붙여넣기", command=lambda: print("붙여넣기"))

lbl = tk.Label(root, text="이 글자 위에서 오른쪽 클릭", bg="lightyellow")
lbl.pack(pady=30)

lbl.bind("<Button-3>", lambda e: mnu.tk_popup(e.x_root, e.y_root))

root.mainloop()
