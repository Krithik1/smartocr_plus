from tkinter import Tk, Canvas
import ctypes

def select_region():
    # Get screen size using ctypes for accurate dimensions
    user32 = ctypes.windll.user32
    screen_width = user32.GetSystemMetrics(0)
    screen_height = user32.GetSystemMetrics(1)

    root = Tk()
    root.overrideredirect(True)  # Remove window decorations
    root.geometry(f"{screen_width}x{screen_height}+0+0")  # Force fullscreen manually
    root.lift()
    root.attributes("-topmost", True)
    root.attributes('-alpha', 0.3)
    root.config(bg='black')

    canvas = Canvas(root, cursor="cross", bg='black')
    canvas.pack(fill="both", expand=True)

    rect = None
    start_x = start_y = 0

    def on_mouse_down(event):
        nonlocal start_x, start_y, rect
        start_x, start_y = event.x, event.y
        rect = canvas.create_rectangle(start_x, start_y, start_x, start_y, outline='red')

    def on_mouse_drag(event):
        canvas.coords(rect, start_x, start_y, event.x, event.y)

    def on_mouse_up(event):
        end_x, end_y = event.x, event.y
        root.destroy()
        x1, y1 = min(start_x, end_x), min(start_y, end_y)
        x2, y2 = max(start_x, end_x), max(start_y, end_y)
        return (x1, y1, x2, y2)

    canvas.bind("<ButtonPress-1>", on_mouse_down)
    canvas.bind("<B1-Motion>", on_mouse_drag)

    result = []

    def finish(event):
        result.append(on_mouse_up(event))

    canvas.bind("<ButtonRelease-1>", finish)
    root.focus_force()
    root.mainloop()

    return result[0] if result else None
