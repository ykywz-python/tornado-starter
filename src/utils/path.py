import os.path
import sys

from src.utils.pyinstaller_ import is_frozen

def exe_path(*args):
    if is_frozen():
        dir = os.path.dirname(sys.executable)
    elif __file__:
        dir = os.path.abspath(".")
    return os.path.join(dir, *args)

def resource_path(*args):
    if is_frozen():
        dir = sys._MEIPASS
    elif __file__:
        dir = os.path.abspath(".")
    return os.path.join(dir, *args)

if __name__ == '__main__':
    APPEXE = 'Application Name'
    print(exe_path(APPEXE, 'test', 'test2'))
    print(resource_path(APPEXE, 'test', 'test2'))