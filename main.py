import tkinter as tk
from PIL import Image, ImageTk
import os
import sys

image_references = {}

def resource_path(relative_path):
    try:
        if getattr(sys, 'frozen', False):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.dirname(os.path.abspath(__file__))
        
        return os.path.join(base_path, relative_path)
    except Exception as e:
        print(f"Error in resource_path: {e}")
        return None

root = tk.Tk()

root.overrideredirect(True)
root.geometry("200x200")
root.attributes("-topmost", True)

root.geometry(f"200x200+{(root.winfo_screenwidth() - 200) // 2}+{(root.winfo_screenheight() - 200) // 2}")

canvas = tk.Canvas(root, width=200, height=200, bg="white", bd=0, highlightthickness=0)

image = Image.open(resource_path("res/fu.png")).resize((200,200))
tk_image = ImageTk.PhotoImage(image)
image_references["icon_banner"] = tk_image
image_label = tk.Label(root, image=tk_image)
image_label.place(x=0,y=0)

root.mainloop()