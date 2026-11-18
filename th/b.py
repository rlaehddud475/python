import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import mysql.connector

class DBConfigDialog(simpledialog.Dialog):
    """프로그램 실행 시 MySQL 접속 정보를 입력받는 다이얼로그 창"""
    def body(self, master):
        tk.Label(master, text="Host:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        tk.Label(master, text="Port:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        tk.Label(master, text="User:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        tk.Label(master, text="Password:").grid(row=3, column=0, sticky="w", padx=5, pady=5)
        tk.Label(master, text="Database:").grid(row=4, column=0, sticky="w", padx=5, pady=5)

        self.e_host = tk.Entry(master)
        self.e_host.insert(0, "127.0.0.1")
        self.e_port = tk.Entry(master)
        self.e_port.insert(0, "3306")
        self.e_user = tk.Entry(master)
        self.e_user.insert(0, "root")
        self.e_password = tk.Entry(master, show="*")
        self.e_db = tk.Entry(master)
        self.e_db.insert(0, "school_db")

        self.e_host.grid(row=0, column=1, padx=5, pady=5)
        self.e_port.grid(row=1, column=1, padx=5, pady=5)
        self.e_user.grid(row=2, column=1, padx=5, pady=5)
        self.e_password.grid(row=3, column=1, padx=5, pady=5)
        self.e_db.grid(row=4, column=1, padx=5, pady=5)

        return self.e_host

    def apply(self):
        self.result = {
            "host": self.e_host.get(),
            "port": int(self.e_port.get()),
            "user": self.e_user.get(),
            "password": self.e_password.get(),
            "database": self.e_db.get()
        }


class StudentApp:
    def __init__(self, root, db_config):
        self.root = root
        self.db_config = db_config
        self.root.title("학생 정보 관리 시스템 (Auto ID)")
        self.root.geometry("650x500")
        
        # 상단 타이틀
        title_label = tk.Label(root, text="학생 종합 관리 프로그램", font=("맑은 고딕", 14, "bold"))
        title_label.pack(pady=10)
        
        # 버튼 프레임
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=5)
        
        btn_fetch = tk.Button(btn_frame, text="새로고침", font=("맑은 고딕", 10), command=self.load_data)
        btn_fetch.pack(side=tk.LEFT, padx=3)
        
        btn_add = tk.Button(btn_frame, text="학생 추가", font=("맑은 고딕", 10), bg="#d4edda", command=self.open_add_dialog)
        btn_add.pack(side=tk.LEFT, padx=3)
        
        btn_edit = tk.Button(btn_frame, text="선택 수정", font=("맑은 고딕", 10), bg="#d1ecf1", command=self.open_edit_dialog)
        btn_edit.pack(side=tk.LEFT, padx=3)
        
        btn_delete = tk.Button(btn_frame, text="선택 삭제", font=("맑은 고딕", 10), bg="#f8d7da", command=self.delete_student)
        btn_delete.pack(side=tk.LEFT, padx=3)
        
        guide_label = tk.Label(root, text="* 수정 또는 삭제하려면 아래 목록에서 학생을 먼저 클릭하세요.", fg="gray", font=("맑은 고딕", 9))
        guide_label.pack(pady=2)

        # 테이블 프레임
        table_frame = tk.Frame(root)
        table_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        tree_scroll = ttk.Scrollbar(table_frame)
        tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.tree = ttk.Treeview(
            table_frame, 
            columns=("ID", "Name", "Department"), 
            show="headings", 
            yscrollcommand=tree_scroll.set
        )
        self.tree.pack(fill=tk.BOTH, expand=True)
        tree_scroll.config(command=self.tree.yview)
        
        self.tree.heading("ID", text="학번 (ID)")
        self.tree.heading("Name", text="이름 (Name)")
        self.tree.heading("Department", text="학과 (Department)")
        
        self.tree.column("ID", width=100, anchor=tk.CENTER)
        self.tree.column("Name", width=150, anchor=tk.CENTER)
        self.tree.column("Department", width=250, anchor=tk.W)
        
        self.load_data()

    def load_data(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        try:
            with mysql.connector.connect(**self.db_config, charset='utf8mb4') as connection:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT id, name, department FROM students ORDER BY id")
                    rows = cursor.fetchall()
                    for row in rows:
                        self.tree.insert("", tk.END, values=row)
        except mysql.connector.Error as err:
            messagebox.showerror("데이터베이스 오류", f"조회 실패:\n{err}")

    def open_add_dialog(self):
        """학번을 입력받지 않고 이름과 학과만 입력받아 추가하는 창"""
        add_win = tk.Toplevel(self.root)
        add_win.title("새 학생 추가")
        add_win.geometry("300x200")
        
        tk.Label(add_win, text="이름 (Name):").pack(anchor="w", padx=20, pady=(15,0))
        e_name = tk.Entry(add_win)
        e_name.pack(fill=tk.X, padx=20)
        
        tk.Label(add_win, text="학과 (Department):").pack(anchor="w", padx=20, pady=(10,0))
        e_dept = tk.Entry(add_win)
        e_dept.pack(fill=tk.X, padx=20)
        
        def save_student():
            s_name = e_name.get().strip()
            s_dept = e_dept.get().strip()
            
            if not s_name or not s_dept:
                messagebox.showwarning("경고", "모든 항목을 입력해주세요.", parent=add_win)
                return
                
            try:
                with mysql.connector.connect(**self.db_config, charset='utf8mb4') as connection:
                    with connection.cursor() as cursor:
                        # id는 자동 증가이므로 이름과 학과만 INSERT 쿼리에 포함합니다.
                        query = "INSERT INTO students (name, department) VALUES (%s, %s)"
                        cursor.execute(query, (s_name, s_dept))
                        connection.commit()
                
                messagebox.showinfo("성공", "학생 정보가 추가되었습니다!", parent=add_win)
                add_win.destroy()
                self.load_data()
            except mysql.connector.Error as err:
                messagebox.showerror("오류", f"추가 실패:\n{err}", parent=add_win)

        tk.Button(add_win, text="저장하기", bg="#007bff", fg="white", font=("맑은 고딕", 10, "bold"), command=save_student).pack(pady=20)

    def open_edit_dialog(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("경고", "수정할 학생을 목록에서 선택해주세요.")
            return
            
        item_data = self.tree.item(selected_item[0])['values']
        orig_id, orig_name, orig_dept = item_data[0], item_data[1], item_data[2]
        
        edit_win = tk.Toplevel(self.root)
        edit_win.title("학생 정보 수정")
        edit_win.geometry("300x250")
        
        tk.Label(edit_win, text="학번 (ID - 변경 불가):").pack(anchor="w", padx=20, pady=(10,0))
        e_id = tk.Entry(edit_win)
        e_id.insert(0, str(orig_id))
        e_id.config(state="disabled")
        e_id.pack(fill=tk.X, padx=20)
        
        tk.Label(edit_win, text="이름 (Name):").pack(anchor="w", padx=20, pady=(10,0))
        e_name = tk.Entry(edit_win)
        e_name.insert(0, orig_name)
        e_name.pack(fill=tk.X, padx=20)
        
        tk.Label(edit_win, text="학과 (Department):").pack(anchor="w", padx=20, pady=(10,0))
        e_dept = tk.Entry(edit_win)
        e_dept.insert(0, orig_dept)
        e_dept.pack(fill=tk.X, padx=20)
        
        def update_student():
            new_name = e_name.get().strip()
            new_dept = e_dept.get().strip()
            
            if not new_name or not new_dept:
                messagebox.showwarning("경고", "모든 항목을 입력해주세요.", parent=edit_win)
                return
                
            try:
                with mysql.connector.connect(**self.db_config, charset='utf8mb4') as connection:
                    with connection.cursor() as cursor:
                        query = "UPDATE students SET name = %s, department = %s WHERE id = %s"
                        cursor.execute(query, (new_name, new_dept, orig_id))
                        connection.commit()
                
                messagebox.showinfo("성공", "학생 정보가 수정되었습니다!", parent=edit_win)
                edit_win.destroy()
                self.load_data()
            except mysql.connector.Error as err:
                messagebox.showerror("오류", f"수정 실패:\n{err}", parent=edit_win)

        tk.Button(edit_win, text="수정 완료", bg="#17a2b8", fg="white", font=("맑은 고딕", 10, "bold"), command=update_student).pack(pady=20)

    def delete_student(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("경고", "삭제할 학생을 목록에서 선택해주세요.")
            return
            
        item_data = self.tree.item(selected_item[0])['values']
        target_id, target_name = item_data[0], item_data[1]
        
        confirm = messagebox.askyesno("확인", f"정말 '{target_name}' (학번: {target_id}) 학생을 삭제하시겠습니까?")
        if confirm:
            try:
                with mysql.connector.connect(**self.db_config, charset='utf8mb4') as connection:
                    with connection.cursor() as cursor:
                        query = "DELETE FROM students WHERE id = %s"
                        cursor.execute(query, (target_id,))
                        connection.commit()
                
                messagebox.showinfo("성공", "학생 정보가 삭제되었습니다.")
                self.load_data()
            except mysql.connector.Error as err:
                messagebox.showerror("오류", f"삭제 실패:\n{err}")


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    
    dialog = DBConfigDialog(root, title="MySQL 접속 설정")
    db_config = dialog.result
    
    if not db_config:
        root.destroy()
    else:
        root.deiconify()
        app = StudentApp(root, db_config)
        root.mainloop()