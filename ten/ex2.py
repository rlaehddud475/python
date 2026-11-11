import tkinter as tk

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("투두 리스트")
        self.root.geometry("320x400")
        
        self.total_count = 0
        self.done_count = 0

        self._create_widgets()
        self.update_status()

    def _create_widgets(self):
        # 입력 영역 (Entry + 추가 버튼)
        input_frame = tk.Frame(self.root)
        input_frame.pack(fill="x", padx=10, pady=10)

        self.ent = tk.Entry(input_frame, font=("맑은 고딕", 11))
        self.ent.pack(side=tk.LEFT, fill="x", expand=True, padx=(0, 5))
        self.ent.bind("<Return>", lambda event: self.add_item())

        add_btn = tk.Button(input_frame, text="추가", command=self.add_item, width=6)
        add_btn.pack(side=tk.RIGHT)

        # 리스트 영역 (Listbox + Scrollbar)
        list_frame = tk.Frame(self.root)
        list_frame.pack(fill="both", expand=True, padx=10, pady=(0, 5))

        self.lb = tk.Listbox(list_frame, font=("맑은 고딕", 11), selectmode=tk.SINGLE)
        self.lb.pack(side=tk.LEFT, fill="both", expand=True)

        scrollbar = tk.Scrollbar(list_frame, orient="vertical", command=self.lb.yview)
        scrollbar.pack(side=tk.RIGHT, fill="y")
        self.lb.config(yscrollcommand=scrollbar.set)

        # 상태 표시 라벨
        self.lbl = tk.Label(self.root, font=("맑은 고딕", 10))
        self.lbl.pack(pady=5)

        # 하단 제어 버튼 영역 (완료, 삭제, 전체 비우기)
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(fill="x", padx=10, pady=(0, 10))

        done_btn = tk.Button(btn_frame, text="완료 처리", command=self.mark_done, width=9)
        done_btn.pack(side=tk.LEFT, expand=True, padx=2)

        del_btn = tk.Button(btn_frame, text="삭제", command=self.delete_item, width=9)
        del_btn.pack(side=tk.LEFT, expand=True, padx=2)

        clear_btn = tk.Button(btn_frame, text="전체 삭제", command=self.clear_all, width=9)
        clear_btn.pack(side=tk.LEFT, expand=True, padx=2)

    def update_status(self):
        self.lbl.config(
            text=f"전체 {self.total_count}개 / 완료 {self.done_count}개"
        )

    def add_item(self):
        text = self.ent.get().strip()
        if text:
            self.lb.insert(tk.END, text)
            self.ent.delete(0, tk.END)
            self.total_count += 1
            self.update_status()

    def delete_item(self):
        selected = self.lb.curselection()
        if selected:
            index = selected[0]
            item_text = self.lb.get(index)
            if item_text.startswith("[완료]"):
                self.done_count -= 1
            self.lb.delete(index)
            self.total_count -= 1
            self.update_status()

    def mark_done(self):
        selected = self.lb.curselection()
        if selected:
            index = selected[0]
            text = self.lb.get(index)
            if not text.startswith("[완료]"):
                self.lb.delete(index)
                self.lb.insert(index, "[완료] " + text)
                self.done_count += 1
                self.update_status()

    def clear_all(self):
        self.lb.delete(0, tk.END)
        self.total_count = 0
        self.done_count = 0
        self.update_status()

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()