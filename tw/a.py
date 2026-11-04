import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog

# 1. 메인 윈도우(창) 생성 및 기본 설정
root = tk.Tk()
root.title("첫 메모장")
root.geometry("800x500")

# 2. 파일 메뉴 관련 기능 함수 정의
def new_file():
    # 새 파일 생성: 알림창을 띄우고 텍스트 영역을 초기화
    messagebox.showinfo("알림", "새파일 기능이 선택되었습니다.", parent=root)
    text_area.delete("1.0", tk.END)

def open_file():
    # 파일 열기: 파일 대화상자를 열어 텍스트 파일을 읽어와 텍스트 영역에 표시
    messagebox.showinfo("알림", "열기 기능이 선택되었습니다.", parent=root)
    file_path = filedialog.askopenfilename(
        title="파일 열기",
        filetypes=[("텍스트 파일", "*.txt"), ("모든 파일", "*.*")],
        parent=root
    )
    if file_path:
        with open(file_path, "r", encoding="utf-8") as f:
            text_area.delete("1.0", tk.END)
            text_area.insert("1.0", f.read())

def save_file():
    # 파일 저장: 다른 이름으로 저장 대화상자를 열어 현재 텍스트 내용을 파일로 기록
    messagebox.showinfo("알림", "저장 기능이 선택되었습니다.", parent=root)
    file_path = filedialog.asksaveasfilename(
        title="파일 저장",
        defaultextension=".txt",
        filetypes=[("텍스트 파일", "*.txt"), ("모든 파일", "*.*")],
        parent=root
    )
    if file_path:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(text_area.get("1.0", tk.END))

def exit_app():
    # 프로그램 종료: 확인 창을 띄운 뒤 예(Yes)를 누르면 창을 닫음
    if messagebox.askyesno("확인", "정말 종료할까요?", parent=root):
        root.destroy()

# 3. 편집 메뉴 관련 기능 함수 정의
def cut_text():
    # 잘라내기: 선택된 텍스트를 클립보드로 이동하고 삭제
    messagebox.showinfo("알림", "잘라내기 기능이 선택되었습니다.", parent=root)
    text_area.event_generate("<<Cut>>")

def copy_text():
    # 복사: 선택된 텍스트를 클립보드에 복사
    messagebox.showinfo("알림", "복사 기능이 선택되었습니다.", parent=root)
    text_area.event_generate("<<Copy>>")

def paste_text():
    # 붙여넣기: 클립보드에 있는 내용을 텍스트 영역에 삽입
    messagebox.showinfo("알림", "붙여넣기 기능이 선택되었습니다.", parent=root)
    text_area.event_generate("<<Paste>>")

def select_all():
    # 전체 선택: 텍스트 영역의 전체 내용을 선택 상태로 지정하고 포커스 이동
    text_area.tag_add("sel", "1.0", tk.END)
    text_area.focus_set()

def find_text():
    # 찾기: 입력받은 문자열을 찾아 해당 위치를 강조 표시
    target = simpledialog.askstring("찾기", "찾을 문자를 입력하세요:", parent=root)
    if target:
        content = text_area.get("1.0", tk.END)
        pos = content.find(target)
        if pos != -1:
            idx = f"1.0 + {pos} chars"
            end_idx = f"{idx} + {len(target)} chars"
            text_area.tag_remove("sel", "1.0", tk.END)
            text_area.tag_add("sel", idx, end_idx)
            text_area.mark_set(tk.INSERT, end_idx)
            text_area.see(idx)
            messagebox.showinfo("찾기 성공", f"'{target}'을(를) 찾았습니다.", parent=root)
        else:
            messagebox.showwarning("찾기 실패", f"'{target}'을(를) 찾을 수 없습니다.", parent=root)

# 4. 도움말 메뉴 관련 기능 함수 정의
def show_info():
    # 프로그램 정보: 개발 정보나 프로그램 버전을 안내하는 팝업 창 출력
    messagebox.showinfo("프로그램 정보", "첫 번째 메모장 프로그램 v1.0", parent=root)

# 5. 상단 메뉴바 구성
mnu_bar = tk.Menu(root) 

# 파일 하위 메뉴 설정
file_mnu = tk.Menu(mnu_bar, tearoff=0)
file_mnu.add_command(label="새파일", command=new_file)
file_mnu.add_command(label="열기", command=open_file)
file_mnu.add_command(label="저장", command=save_file)
file_mnu.add_separator()
file_mnu.add_command(label="종료", command=exit_app)

# 편집 하위 메뉴 설정
edit_mnu = tk.Menu(mnu_bar, tearoff=0)
edit_mnu.add_command(label="잘라내기", command=cut_text)
edit_mnu.add_command(label="복사", command=copy_text)
edit_mnu.add_command(label="붙여넣기", command=paste_text)
edit_mnu.add_separator()
edit_mnu.add_command(label="찾기", command=find_text)
edit_mnu.add_command(label="전체 선택", command=select_all)

# 도움말 하위 메뉴 설정
help_mnu = tk.Menu(mnu_bar, tearoff=0)
help_mnu.add_command(label="프로그램정보", command=show_info)

# 메뉴바에 각 상위 메뉴(파일, 편집, 도움말) 등록
mnu_bar.add_cascade(label="파일", menu=file_mnu)
mnu_bar.add_cascade(label="편집", menu=edit_mnu)
mnu_bar.add_cascade(label="도움말", menu=help_mnu)

# 메인 창에 메뉴바 설정 적용
root.config(menu=mnu_bar)

# 6. 본문 텍스트 입력 영역(Text Widget) 생성 및 배치
text_area = tk.Text(root, wrap="word")
text_area.pack(expand=True, fill="both")

# 7. 프로그램 실행 루프 시작
root.mainloop()