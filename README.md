In short form, main.py creates a window with resized image that is always on top and can be turned off by killing it in task manager or by closing cmd that the project is running on.

The troll.exe is just compile main.py and res foulder into exe file by using this command:
```
python -m PyInstaller --onefile --noconsole --clean --add-data "res;res" --exclude-module "pywin32" main.py
```
