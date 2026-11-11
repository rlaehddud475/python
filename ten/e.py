import tkinter as tk

root = tk.Tk()
root.geometry("300x250")

lb = tk.Listbox(root)
lb.pack(fill="both", expand=True, padx=10, pady=(0, 7))

ent = tk.Entry(root)
ent.pack(fill="x", padx=10, pady=10)

def add_item():
    text = ent.get().strip()
    if text:
        lb.insert(tk.END, text)
        ent.delete(0, tk.END)

btn = tk.Button(root, text="추가", command=add_item)
btn.pack(pady=(0, 10))

root.mainloop()

root = tk.Tk()
root.geometry("300x280")

lb = tk.Listbox(root)
lb.pack(fill="both", expand=True, padx=10, pady=(0, 7))

ent = tk.Entry(root)
ent.pack(fill="x", padx=10, pady=10)

def add_item():
    text = ent.get().strip()
    if text:
        lb.insert(tk.END, text)
        ent.delete(0, tk.END)

def delete_item():
    selected_indices = lb.curselection()
    if selected_indices:
        lb.delete(selected_indices[0])

add_btn = tk.Button(root, text="추가", command=add_item)
add_btn.pack(pady=(0, 5))

delete_btn = tk.Button(root, text="삭제", command=delete_item)
delete_btn.pack(pady=(0, 10))

root.mainloop()

root = tk.Tk()
root.geometry("300x400")

total_count = 0
done_count = 0

lb = tk.Listbox(root)
lb.pack(fill="both", expand=True, padx=10, pady=(0, 7))

ent = tk.Entry(root)
ent.pack(fill="x", padx=10, pady=10)

lbl = tk.Label(root, text="전체 0개 / 완료 0개")
lbl.pack()

def update_status():
    global total_count, done_count
    lbl.config(text=f"전체 {total_count}개 / 완료 {done_count}개")

def add_item():
    global total_count
    text = ent.get().strip()
    if text:
        lb.insert(tk.END, text)
        ent.delete(0, tk.END)
        total_count += 1
        update_status()

def delete_item():
    global total_count
    selected = lb.curselection()
    if selected:
        lb.delete(selected[0])
        total_count -= 1
        update_status()

def mark_done():
    global done_count
    selected = lb.curselection()
    if selected:
        text = lb.get(selected[0])
        lb.delete(selected[0])
        lb.insert(selected[0], "[완료] " + text)
        done_count += 1
        update_status()

def clear_all():
    global total_count, done_count
    lb.delete(0, tk.END)
    total_count = 0
    done_count = 0
    update_status()

add_btn = tk.Button(root, text="추가", command=add_item)
add_btn.pack()

done_btn = tk.Button(root, text="완료 처리", command=mark_done)
done_btn.pack()

delete_btn = tk.Button(root, text="삭제", command=delete_item)
delete_btn.pack()

clear_btn = tk.Button(root, text="전체 비우기", command=clear_all)
clear_btn.pack()

root.mainloop()