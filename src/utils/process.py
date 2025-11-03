import os
import psutil

def kill_proc_tree():
    try:
        pid = os.getpid()    
        parent = psutil.Process(pid)
        for child in parent.children(recursive=True):
            child.kill()
    except:
        pass