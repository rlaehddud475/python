class TodoManager:
    def __init__(self):
        self.todos = []

    def show_list(self):
        print("\n--- [ 할 일 목록 ] ---")
        if not self.todos:
            print("등록된 할 일이 없습니다.")
        else:
            for idx, item in enumerate(self.todos):
                status = "[완료]" if item["done"] else "[진행중]"
                print(f"{idx + 1}. {status} {item['task']}")
        print(f"전체 {len(self.todos)}개 / 완료 {sum(1 for t in self.todos if t['done'])}개\n")

    def add_task(self, task):
        if task.strip():
            self.todos.append({"task": task.strip(), "done": False})
            print(f"'{task}'이(가) 추가되었습니다.")

    def mark_done(self, index):
        if 0 <= index < len(self.todos):
            self.todos[index]["done"] = True
            print(f"{index + 1}번 항목이 완료 처리되었습니다.")
        else:
            print("잘못된 번호입니다.")

    def delete_task(self, index):
        if 0 <= index < len(self.todos):
            removed = self.todos.pop(index)
            print(f"'{removed['task']}'이(가) 삭제되었습니다.")
        else:
            print("잘못된 번호입니다.")

def main():
    manager = TodoManager()
    
    while True:
        manager.show_list()
        print("1. 추가  2. 완료  3. 삭제  4. 종료")
        choice = input("선택하세요: ").strip()

        if choice == "1":
            task = input("추가할 할 일을 입력하세요: ")
            manager.add_task(task)
        elif choice == "2":
            try:
                idx = int(input("완료할 항목 번호: ")) - 1
                manager.mark_done(idx)
            except ValueError:
                print("숫자를 입력해주세요.")
        elif choice == "3":
            try:
                idx = int(input("삭제할 항목 번호: ")) - 1
                manager.delete_task(idx)
            except ValueError:
                print("숫자를 입력해주세요.")
        elif choice == "4":
            print("프로그램을 종료합니다.")
            break
        else:
            print("올바른 번호를 선택해주세요.")

if __name__ == "__main__":
    main()