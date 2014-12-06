import sys
from cx_Freeze import setup, Executable

includefiles = [("data/test.db", "data/test.db"), ("data/test.csv", "data/test.csv"), ("readme.txt", "readme.txt"), ("db_icon.ico", "db_icon.ico")]
# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["sqlite3", "tkinter"], "include_files": includefiles}


# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "Database Program",
        version = "0.1",
        description = "Database Program",
        options = {"build_exe": build_exe_options},
        executables = [Executable("gui_main.py", base=base, targetName = "databaseprogram.exe", icon = "db_icon.ico")])