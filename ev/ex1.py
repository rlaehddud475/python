import tkinter as tk

root = tk.Tk()
root.geometry("300x120")
mnu_bar = tk.Menu(root) 
file_mnu = tk.Menu(mnu_bar, tearoff=0)    # 2) 하위 메뉴 생성
file_mnu.add_command(label="새파일", command=root.destroy)
file_mnu.add_command(label="열기", command=lambda: print("열기 클릭"))    # 3) 항목 채우기
file_mnu.add_command(label="저장", command=root.destroy)
file_mnu.add_command(label="종료", command=root.destroy)

edit_mnu = tk.Menu(mnu_bar, tearoff=0)    # 2) 하위 메뉴 생성
edit_mnu.add_command(label="잘라내기", command=lambda: print("잘라내기"))
edit_mnu.add_command(label="복사", command=lambda: print("복사"))
edit_mnu.add_command(label="붙여넣기", command=lambda: print("붙여넣기"))

help_mnu = tk.Menu(mnu_bar, tearoff=0)    # 2) 하위 메뉴 생성
help_mnu.add_command(label="프로그램정보", command=lambda: print("프로그램정보"))

mnu_bar.add_cascade(label="파일", menu=file_mnu)
mnu_bar.add_cascade(label="편집", menu=edit_mnu)
mnu_bar.add_cascade(label="도움말", menu=help_mnu)
root.config(menu=mnu_bar)
root.mainloop()