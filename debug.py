import os
import datetime



path_debug = r"debug"
time = (((datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")).replace(" ", "-")).replace(".", "-")).replace(":", "-")
path = f"{path_debug}\{time}.txt"

text = f"[LOGS: {datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")}]"

def add_file():
    with open(path, "w+", encoding='utf-8') as file:
        file.write(text)

def add_action():
    pass
