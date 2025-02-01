import tkinter as tk
from PIL import Image, ImageTk
import os
import sys

Variables = {
    "ImagePath": "res/fu.png",

    "WindowSizeX": 200,
    "WindowSizeY": 200,

    "ResizeX": 200,
    "ResizeY": 200,

    "ImagePlaceX": 0,
    "ImagePlaceY": 0,

    "AlwaysOnTop": True,
}

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
root.geometry(str(Variables["WindowSizeX"]) + "x" + str(Variables["WindowSizeY"]))
root.attributes("-topmost", Variables["AlwaysOnTop"])

root.geometry(f"{Variables['WindowSizeX']}x{Variables['WindowSizeY']}+{(root.winfo_screenwidth() - 200) // 2}+{(root.winfo_screenheight() - 200) // 2}")

canvas = tk.Canvas(root, width=Variables["WindowSizeX"], height=Variables["WindowSizeY"], bg="white", bd=0, highlightthickness=0)

image = Image.open(resource_path(Variables["ImagePath"])).resize((Variables["ResizeX"],Variables["ResizeY"]))
tk_image = ImageTk.PhotoImage(image)
image_references["icon_banner"] = tk_image
image_label = tk.Label(root, image=tk_image)
image_label.place(x=Variables["ImagePlaceX"],y=Variables["ImagePlaceY"])

root.mainloop()
