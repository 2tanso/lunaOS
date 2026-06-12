import tkinter as tk
from tkinter import ttk
import os

current_path = os.path.expanduser("~")

root = tk.Tk()
root.title("🌙 Luna Files")
root.geometry("900x600")

path_label = tk.Label(
    root,
    text=current_path,
    anchor="w",
    font=("Arial", 12)
)

path_label.pack(fill="x", padx=10, pady=5)

file_list = tk.Listbox(
    root,
    font=("Arial", 12)
)

file_list.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=10
)

def load_directory(path):
    global current_path

    current_path = path

    path_label.config(text=current_path)

    file_list.delete(0, tk.END)

    try:
        items = os.listdir(path)

        items.sort()

        if path != "/":
            file_list.insert(tk.END, "..")

        for item in items:
            full_path = os.path.join(path, item)

            if os.path.isdir(full_path):
                file_list.insert(tk.END, f"📁 {item}")
            else:
                file_list.insert(tk.END, f"📄 {item}")

    except Exception as e:
        print(e)

def open_item(event):

    selection = file_list.curselection()

    if not selection:
        return

    item = file_list.get(selection[0])

    if item == "..":
        load_directory(
            os.path.dirname(current_path)
        )
        return

    name = item[2:]

    full_path = os.path.join(
        current_path,
        name
    )

    if os.path.isdir(full_path):
        load_directory(full_path)

file_list.bind(
    "<Double-Button-1>",
    open_item
)

load_directory(current_path)

root.mainloop()
