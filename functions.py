import config as cfg

def main():
    pass

def switch():
    pass

def info():
    # Вводим переменные
    name = cfg.NAME
    version = cfg.VERSION
    creator = cfg.CREATOR
    root = cfg.ROOT
    git_connect = cfg.GIT_CONNECT
    date_create = cfg.DATE_CREATE
    last_update = cfg.LAST_DATE_UPDATE
    console = cfg.CONSOLE_SUPPORTIVE
    gui = cfg.GUI_SUPPORTIVE
    # Текст
    text = f"""--------{name}--------\n     Name: {name}\n     Versions: {version}\n     Creator: {creator}\n     Root: {root}\n     Git-connect: {git_connect}\n     Date create: {date_create}\n     Last date update: {last_update}\n Console: {console}      |      Gui: {gui}\n-------------<INFO  MENU>-------------"""

    return text

def help():
    # Вводим переменные
    name = cfg.NAME

    text = f"""--------{name}--------\n <1> - Main menu\n <2> - Switch menu\n <8> - Info menu\n <9> - Help menu  \n-------------<HELP  MENU>-------------"""

    return text
