import tkinter as tk

root = tk.Tk()
root.title("🌙 Luna Calc")
root.geometry("350x500")

expression = ""

entry = tk.Entry(
    root,
    font=("Arial", 24),
    justify="right"
)

entry.pack(fill="x", padx=10, pady=10)


def press(value):
    global expression
    expression += str(value)
    entry.delete(0, tk.END)
    entry.insert(0, expression)


def calculate():
    global expression

    try:
        result = str(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(0, result)
        expression = result

    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
        expression = ""


def clear():
    global expression
    expression = ""
    entry.delete(0, tk.END)


buttons = [
    "7","8","9","/",
    "4","5","6","*",
    "1","2","3","-",
    "0",".","=","+"
]

frame = tk.Frame(root)
frame.pack(expand=True, fill="both")

row = 0
col = 0

for button in buttons:

    if button == "=":
        cmd = calculate
    else:
        cmd = lambda x=button: press(x)

    b = tk.Button(
        frame,
        text=button,
        font=("Arial", 18),
        command=cmd
    )

    b.grid(
        row=row,
        column=col,
        sticky="nsew"
    )

    col += 1

    if col > 3:
        col = 0
        row += 1

for i in range(4):
    frame.columnconfigure(i, weight=1)

for i in range(4):
    frame.rowconfigure(i, weight=1)

clear_btn = tk.Button(
    root,
    text="Clear",
    font=("Arial", 18),
    command=clear
)

clear_btn.pack(fill="x")

root.mainloop()
