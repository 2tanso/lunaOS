import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title("🌙 Luna Notes")
root.geometry("900x600")

text = tk.Text(
    root,
    font=("Segoe UI", 12),
    wrap="word"
)

text.pack(fill="both", expand=True)

def save_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )

    if file_path:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(text.get("1.0", tk.END))

menu = tk.Menu(root)

file_menu = tk.Menu(menu, tearoff=0)
file_menu.add_command(label="Save", command=save_file)

menu.add_cascade(label="File", menu=file_menu)

root.config(menu=menu)

root.mainloop()
