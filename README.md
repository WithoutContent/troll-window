## What this code do?
In short, main.py creates a window with a resized image that is always on top and can be disabled by killing it in the task manager or closing the cmd that is running the project.

## Troll.exe
Troll.exe simply compiles main.py and res folder into an exe file with this command:
```
python -m PyInstaller --onefile --noconsole --clean --add-data "res;res" --exclude-module "pywin32" main.py
```
## Variables
In the main.py file there is a table of variables where you can change values ​​to adapt the code to your project
```
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
```
## What each variable do?
`ImagePath` means the path where the image is located\
`WindowSizeX` and `WindowSizeY` is for the size of the invisble window\
`ResizeX` and `ResizeY` indicate what size should image be changed\
`ImagePlaceX` and `ImagePlaceY` indicate in what location the image sould be place in the window\
`AlwaysOnTop` is a bool that indicate do you want the window to be always on top
