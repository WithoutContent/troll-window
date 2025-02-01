In short, main.py creates a window with a resized image that is always on top and can be disabled by killing it in the task manager or closing the cmd that is running the project.

Troll.exe simply compiles main.py and res folder into an exe file with this command:
```
python -m PyInstaller --onefile --noconsole --clean --add-data "res;res" --exclude-module "pywin32" main.py
```
