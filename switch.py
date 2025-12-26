import platform

def get_path(*args, **kwargs):
    path = None
    
    if platform.system() == "Windows":
        path = r"C:\Windows\System32\drivers\etc\hosts"
    else: 
        path = None

    return path

def switch_on():
    pass

def switch_off():
    pass