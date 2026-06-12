import tkinter as tk
from PIL import Image, ImageTk
from datetime import datetime

# =========================
# Window
# =========================

root = tk.Tk()
root.title("Luna Desktop")
root.attributes("-fullscreen", True)

screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()

# =========================
# Wallpaper
# =========================

wallpaper = Image.open("/home/tanso/artwork/wallpaper.png")

img_w, img_h = wallpaper.size

scale = max(
    screen_w / img_w,
    screen_h / img_h
)

new_w = int(img_w * scale)
new_h = int(img_h * scale)

wallpaper = wallpaper.resize(
    (new_w, new_h),
    Image.Resampling.LANCZOS
)

left = (new_w - screen_w) // 2
top = (new_h - screen_h) // 2

wallpaper = wallpaper.crop(
    (left, top, left + screen_w, top + screen_h)
)

bg_img = ImageTk.PhotoImage(wallpaper)

bg_label = tk.Label(root, image=bg_img)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# =========================
# Top Bar
# =========================

topbar = tk.Frame(
    root,
    bg="#07142d",
    height=40
)

topbar.place(
    x=0,
    y=0,
    width=screen_w
)

logo = tk.Label(
    topbar,
    text="🌙 Luna OS",
    fg="white",
    bg="#07142d",
    font=("Segoe UI", 14, "bold")
)

logo.place(x=15, y=7)

clock_label = tk.Label(
    topbar,
    fg="white",
    bg="#07142d",
    font=("Segoe UI", 12)
)

clock_label.place(
    x=screen_w - 100,
    y=8
)

def update_clock():
    now = datetime.now().strftime("%H:%M")
    clock_label.config(text=now)
    root.after(1000, update_clock)

update_clock()

# =========================
# Todo Widget
# =========================

todo = tk.Frame(
    root,
    bg="#1d2b52",
    width=180,
    height=100
)

todo.place(x=20, y=60)

tk.Label(
    todo,
    text="오늘",
    fg="white",
    bg="#1d2b52",
    font=("Segoe UI", 11, "bold")
).pack(anchor="w", padx=10, pady=5)

tk.Label(
    todo,
    text="✓ Luna Desktop 제작",
    fg="white",
    bg="#1d2b52"
).pack(anchor="w", padx=10)

tk.Label(
    todo,
    text="✓ Notes 연결",
    fg="white",
    bg="#1d2b52"
).pack(anchor="w", padx=10)

# =========================
# Weather Widget
# =========================

weather = tk.Frame(
    root,
    bg="#1d2b52",
    width=120,
    height=120
)

weather.place(x=20, y=180)

tk.Label(
    weather,
    text="날씨",
    fg="white",
    bg="#1d2b52"
).pack()

tk.Label(
    weather,
    text="22°",
    fg="white",
    bg="#1d2b52",
    font=("Segoe UI", 36)
).pack()

tk.Label(
    weather,
    text="맑음",
    fg="white",
    bg="#1d2b52"
).pack()

# =========================
# Right Icons
# =========================

icons = tk.Frame(
    root,
    bg="#07142d"
)

icons.place(
    x=screen_w - 90,
    y=140
)

for icon, text in [
    ("📁", "파일"),
    ("📝", "메모"),
    ("⚙", "설정")
]:
    tk.Label(
        icons,
        text=icon,
        font=("Segoe UI", 26),
        fg="white",
        bg="#07142d"
    ).pack(pady=10)

    tk.Label(
        icons,
        text=text,
        fg="white",
        bg="#07142d"
    ).pack()

# =========================
# Dock
# =========================

dock = tk.Frame(
    root,
    bg="#24355f"
)

dock.place(
    relx=0.5,
    rely=0.95,
    anchor="s"
)

dock_icons = [
    "🌙",
    "📅",
    "🌐",
    "✉",
    "📝",
    "⚙"
]

for icon in dock_icons:
    tk.Button(
        dock,
        text=icon,
        width=4,
        height=2,
        font=("Segoe UI", 18),
        bg="#2f4375",
        fg="white",
        relief="flat"
    ).pack(side="left", padx=5, pady=5)

# =========================
# ESC 종료
# =========================

root.bind(
    "<Escape>",
    lambda e: root.destroy()
)

root.mainloop()
