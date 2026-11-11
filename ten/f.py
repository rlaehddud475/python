import tkinter as tk

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("300x80")
        self.lbl = tk.Label(self, text="안녕하세요")
        self.lbl.pack(pady=5)
        tk.Button(self, text="클릭", command=self.on_click).pack()

    def on_click(self):
        self.lbl.config(text="버튼을 눌렀습니다")


if __name__ == "__main__":
    Application().mainloop()
class CounterFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.count = 0
        self.lbl = tk.Label(self, text="0", font=("맑은 고딕", 24))
        self.lbl.pack(pady=10)
        tk.Button(self, text="+1", command=self.increase).pack()

    def increase(self):
        self.count += 1
        self.lbl.config(text=str(self.count))


if __name__ == "__main__":
    root = tk.Tk()
    CounterFrame(root).pack(padx=20, pady=20)
    root.mainloop()

    def __init__(self, master, on_submit):
        super().__init__(master)
        self.on_submit = on_submit
        self.ent = tk.Entry(self)
        self.ent.pack(side="left")
        tk.Button(self, text="인사하기", command=self.submit).pack(side="left")

    def submit(self):
        self.on_submit(self.ent.get())


class Greeting(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.lbl = tk.Label(self, text="", font=("맑은 고딕", 14))
        self.lbl.pack()

    def show(self, name):
        self.lbl.config(text=f"안녕하세요, {name}님!")


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("300x120")
        self.greeting = Greeting(self)
        self.name_input = NameInput(self, on_submit=self.greeting.show)
        self.name_input.pack(pady=10)
        self.greeting.pack(pady=10)


if __name__ == "__main__":
    App().mainloop()

class PageOne(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        tk.Label(self, text="첫 번째 페이지", font=("맑은 고딕", 16)).pack(pady=20)
        tk.Button(self, text="다음으로",
                  command=lambda: controller.show_page("PageTwo")).pack()


class PageTwo(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        tk.Label(self, text="두 번째 페이지", font=("맑은 고딕", 16)).pack(pady=20)
        tk.Button(self, text="이전으로",
                  command=lambda: controller.show_page("PageOne")).pack()


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("300x200")
        self.pages = {}
        for PageClass in (PageOne, PageTwo):
            page = PageClass(self, self)
            self.pages[PageClass.__name__] = page
            page.grid(row=0, column=0, sticky="nsew")
        self.show_page("PageOne")

    def show_page(self, name):
        self.pages[name].tkraise()


if __name__ == "__main__":
    App().mainloop()

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("300x350")
        self.total_count = 0
        self.done_count = 0

        self._create_widgets()
        self.update_status()

    def _create_widgets(self):
        self.lb = tk.Listbox(self.root)
        self.lb.pack(fill="both", expand=True, padx=10, pady=(0, 7))

        self.ent = tk.Entry(self.root)
        self.ent.pack(fill="x", padx=10, pady=10)

        self.lbl = tk.Label(self.root)
        self.lbl.pack()

        buttons = [
            ("추가", self.add_item),
            ("완료 처리", self.mark_done),
            ("삭제", self.delete_item),
            ("전체 비우기", self.clear_all),
        ]
        for text, command in buttons:
            tk.Button(self.root, text=text, command=command).pack()

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
            self.lb.delete(selected[0])
            self.total_count -= 1
            self.update_status()

    def mark_done(self):
        selected = self.lb.curselection()
        if selected:
            index = selected[0]
            text = self.lb.get(index)
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