import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from PIL import Image, ImageTk, ImageGrab  # 이미지 처리를 위한 Pillow 라이브러리
import pickle  # 텍스트와 이미지 데이터를 함께 직렬화하여 .dat 파일로 저장하기 위한 모듈

# -------------------------------------------------------------------------
# 1. 메인 윈도우(창) 생성 및 기본 설정
# -------------------------------------------------------------------------
root = tk.Tk()
root.title("첫 메모장")
root.geometry("800x500")

# -------------------------------------------------------------------------
# 2. 파일 메뉴 관련 기능 함수 정의
# -------------------------------------------------------------------------
def new_file():
    # [새파일] 알림창을 띄운 뒤, 텍스트 영역과 이미지 매핑 정보를 초기화함
    messagebox.showinfo("알림", "새파일 기능이 선택되었습니다.", parent=root)
    text_area.delete("1.0", tk.END)
    if hasattr(text_area, "image_name_to_pil"):
        text_area.image_name_to_pil.clear()
    if hasattr(text_area, "image_refs"):
        text_area.image_refs.clear()

def open_file():
    # [열기] 커스텀 데이터 파일(.dat) 또는 일반 텍스트 파일(.txt)을 불러옴
    messagebox.showinfo("알림", "열기 기능이 선택되었습니다.", parent=root)
    file_path = filedialog.askopenfilename(
        title="파일 열기",
        filetypes=[("메모장 데이터 파일", "*.dat"), ("텍스트 파일", "*.txt"), ("모든 파일", "*.*")],
        parent=root
    )
    if file_path:
        # 기존 데이터 초기화
        text_area.delete("1.0", tk.END)
        if not hasattr(text_area, "image_name_to_pil"):
            text_area.image_name_to_pil = {}
        else:
            text_area.image_name_to_pil.clear()
            
        if not hasattr(text_area, "image_refs"):
            text_area.image_refs = []
        else:
            text_area.image_refs.clear()

        try:
            # 1차 시도: .dat 형식의 직렬화된 데이터(텍스트 + 이미지) 불러오기
            with open(file_path, "rb") as f:
                data_list = pickle.load(f)
                
                for item in data_list:
                    if isinstance(item, str):
                        # 텍스트인 경우 그대로 삽입
                        text_area.insert(tk.END, item)
                    else:
                        # PIL Image 객체인 경우 Tkinter용 이미지로 변환 후 위젯에 생성
                        img_tk = ImageTk.PhotoImage(item)
                        text_area.image_refs.append(img_tk)  # 가비지 컬렉션 방지
                        
                        img_index = text_area.image_create(tk.END, image=img_tk)
                        img_name = text_area.image_cget(img_index, "image")
                        text_area.image_name_to_pil[img_name] = item
        except Exception:
            # 2차 시도: 실패할 경우 일반 텍스트 파일(.txt)로 간주하고 읽어오기
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    text_area.insert("1.0", f.read())
            except Exception as e:
                messagebox.showerror("에러", f"파일을 열 수 없습니다: {e}", parent=root)

def save_file():
    # [저장] 화면에 있는 텍스트와 이미지들을 순서대로 수집하여 .dat 파일로 안전하게 직렬화 저장
    messagebox.showinfo("알림", "저장 기능이 선택되었습니다.", parent=root)
    file_path = filedialog.asksaveasfilename(
        title="파일 저장",
        defaultextension=".dat",
        filetypes=[("메모장 데이터 파일", "*.dat"), ("텍스트 파일", "*.txt"), ("모든 파일", "*.*")],
        parent=root
    )
    if file_path:
        try:
            # 확장자가 .txt인 경우 순수 텍스트만 저장
            if file_path.endswith(".txt"):
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(text_area.get("1.0", tk.END))
                return

            # .dat 또는 기타 확장자일 경우 텍스트와 이미지를 순서대로 리스트에 담아 직렬화
            data_to_save = []
            
            if not hasattr(text_area, "image_name_to_pil"):
                text_area.image_name_to_pil = {}

            # 텍스트 위젯의 내용을 dump 메서드로 순회하며 텍스트와 이미지 요소 추출
            def dump_callback(key, value, index):
                if key == "text":
                    data_to_save.append(value)
                elif key == "image":
                    # 해당 위치에 있는 이미지 이름으로 원본 PIL Image를 찾아 저장 리스트에 추가
                    if value in text_area.image_name_to_pil:
                        data_to_save.append(text_area.image_name_to_pil[value])

            text_area.dump("1.0", tk.END, text=True, image=True, command=dump_callback)

            with open(file_path, "wb") as f:
                pickle.dump(data_to_save, f)
                
        except Exception as e:
            messagebox.showerror("에러", f"파일을 저장할 수 없습니다: {e}", parent=root)

def exit_app():
    # [종료] 프로그램 종료 확인 창 띄우기
    if messagebox.askyesno("확인", "정말 종료할까요?", parent=root):
        root.destroy()

# -------------------------------------------------------------------------
# 3. 편집 메뉴 관련 기능 함수 정의
# -------------------------------------------------------------------------
def undo_text():
    # [되돌리기] 직전 작업 취소
    try:
        text_area.event_generate("<<Undo>>")
    except Exception:
        pass

def redo_text():
    # [다시 실행] 되돌리기 취소
    try:
        text_area.event_generate("<<Redo>>")
    except Exception:
        pass

def cut_text():
    # [잘라내기]
    text_area.event_generate("<<Cut>>")

def copy_text():
    # [복사]
    text_area.event_generate("<<Copy>>")

def paste_text():
    # [붙여넣기] 클립보드에 이미지가 있는지 확인 후 이미지 삽입 또는 텍스트 붙여넣기 수행
    try:
        clipboard_img = ImageGrab.grabclipboard()
        if clipboard_img is not None:
            img_tk = ImageTk.PhotoImage(clipboard_img)
            
            if not hasattr(text_area, "image_refs"):
                text_area.image_refs = []
            text_area.image_refs.append(img_tk)
            
            if not hasattr(text_area, "image_name_to_pil"):
                text_area.image_name_to_pil = {}
                
            img_index = text_area.image_create(tk.INSERT, image=img_tk)
            img_name = text_area.image_cget(img_index, "image")
            text_area.image_name_to_pil[img_name] = clipboard_img
            text_area.insert(tk.INSERT, "\n")
            return
    except Exception:
        pass
    
    text_area.event_generate("<<Paste>>")

def insert_image():
    # [이미지 삽입] 파일 탐색기를 통해 로컬 이미지를 선택하여 본문에 삽입
    file_path = filedialog.askopenfilename(
        title="이미지 선택",
        filetypes=[("이미지 파일", "*.png *.jpg *.jpeg *.gif"), ("모든 파일", "*.*")],
        parent=root
    )
    if file_path:
        try:
            img = Image.open(file_path)
            img_tk = ImageTk.PhotoImage(img)
            
            if not hasattr(text_area, "image_refs"):
                text_area.image_refs = []
            text_area.image_refs.append(img_tk)
            
            if not hasattr(text_area, "image_name_to_pil"):
                text_area.image_name_to_pil = {}
                
            img_index = text_area.image_create(tk.INSERT, image=img_tk)
            img_name = text_area.image_cget(img_index, "image")
            text_area.image_name_to_pil[img_name] = img
            text_area.insert(tk.INSERT, "\n")
        except Exception as e:
            messagebox.showerror("에러", f"이미지를 불러올 수 없습니다: {e}", parent=root)

def select_all():
    # [전체 선택]
    text_area.tag_add("sel", "1.0", tk.END)
    text_area.focus_set()

# --- [다음/이전 찾기 창 및 검색 기능 구현] ---
def open_find_dialog():
    find_win = tk.Toplevel(root)
    find_win.title("찾기")
    find_win.geometry("300x120")
    find_win.resizable(False, False)
    find_win.transient(root)

    tk.Label(find_win, text="찾을 문자:").pack(pady=5)
    ent_target = tk.Entry(find_win, width=30)
    ent_target.pack(pady=5)
    ent_target.focus_set()

    def find_next():
        target = ent_target.get()
        if not target:
            return
        content = text_area.get("1.0", tk.END)
        current_index = text_area.index(tk.INSERT)
        
        start_pos = len(text_area.get("1.0", current_index))
        pos = content.find(target, start_pos)
        
        if pos == -1:
            pos = content.find(target)
            
        if pos != -1:
            idx = f"1.0 + {pos} chars"
            end_idx = f"{idx} + {len(target)} chars"
            
            text_area.tag_remove("sel", "1.0", tk.END)
            text_area.tag_add("sel", idx, end_idx)
            text_area.mark_set(tk.INSERT, end_idx)
            text_area.see(idx)
            text_area.focus_set()
        else:
            messagebox.showwarning("찾기", f"'{target}'을(를) 찾을 수 없습니다.", parent=find_win)

    def find_prev():
        target = ent_target.get()
        if not target:
            return
        content = text_area.get("1.0", tk.END)
        current_index = text_area.index(tk.INSERT)
        
        end_pos = len(text_area.get("1.0", current_index))
        pos = content.rfind(target, 0, end_pos)
        
        if pos == -1:
            pos = content.rfind(target)
            
        if pos != -1:
            idx = f"1.0 + {pos} chars"
            end_idx = f"{idx} + {len(target)} chars"
            
            text_area.tag_remove("sel", "1.0", tk.END)
            text_area.tag_add("sel", idx, end_idx)
            text_area.mark_set(tk.INSERT, idx)
            text_area.see(idx)
            text_area.focus_set()
        else:
            messagebox.showwarning("찾기", f"'{target}'을(를) 찾을 수 없습니다.", parent=find_win)

    btn_frame = tk.Frame(find_win)
    btn_frame.pack(pady=5)

    tk.Button(btn_frame, text="이전 찾기", command=find_prev, width=10).pack(side=tk.LEFT, padx=5)
    tk.Button(btn_frame, text="다음 찾기", command=find_next, width=10).pack(side=tk.LEFT, padx=5)

# -------------------------------------------------------------------------
# 4. 도움말 메뉴 관련 기능 함수 정의
# -------------------------------------------------------------------------
def show_info():
    messagebox.showinfo("프로그램 정보", "첫 번째 메모장 프로그램 v1.0", parent=root)

# -------------------------------------------------------------------------
# 5. 상단 메뉴바 구성
# -------------------------------------------------------------------------
mnu_bar = tk.Menu(root) 

file_mnu = tk.Menu(mnu_bar, tearoff=0)
file_mnu.add_command(label="새파일", command=new_file)
file_mnu.add_command(label="열기", command=open_file)
file_mnu.add_command(label="저장", command=save_file)
file_mnu.add_separator()
file_mnu.add_command(label="종료", command=exit_app)

edit_mnu = tk.Menu(mnu_bar, tearoff=0)
edit_mnu.add_command(label="되돌리기", command=undo_text)
edit_mnu.add_command(label="다시 실행", command=redo_text)
edit_mnu.add_separator()
edit_mnu.add_command(label="잘라내기", command=cut_text)
edit_mnu.add_command(label="복사", command=copy_text)
edit_mnu.add_command(label="붙여넣기", command=paste_text)
edit_mnu.add_command(label="이미지 삽입", command=insert_image)
edit_mnu.add_separator()
edit_mnu.add_command(label="찾기", command=open_find_dialog)  
edit_mnu.add_command(label="전체 선택", command=select_all)

help_mnu = tk.Menu(mnu_bar, tearoff=0)
help_mnu.add_command(label="프로그램정보", command=show_info)

mnu_bar.add_cascade(label="파일", menu=file_mnu)
mnu_bar.add_cascade(label="편집", menu=edit_mnu)
mnu_bar.add_cascade(label="도움말", menu=help_mnu)

root.config(menu=mnu_bar)

# -------------------------------------------------------------------------
# 6. 본문 텍스트 입력 영역 및 스크롤바 생성 및 배치
# -------------------------------------------------------------------------
frame = tk.Frame(root)
frame.pack(expand=True, fill="both")

scroll_bar = tk.Scrollbar(frame)
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)

text_area = tk.Text(frame, wrap="word", yscrollcommand=scroll_bar.set, undo=True)
text_area.pack(side=tk.LEFT, expand=True, fill="both")

scroll_bar.config(command=text_area.yview)

# -------------------------------------------------------------------------
# 7. 프로그램 실행 루프 시작
# -------------------------------------------------------------------------
root.mainloop()