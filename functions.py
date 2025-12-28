import config as cfg
import requests
from bs4 import BeautifulSoup as bs

def get_version() -> str:
    URL_TEMPLATE = "https://github.com/Sk1lizz/switch_site/blob/main/files/config/config.json"
    r = requests.get(URL_TEMPLATE)

    soup = bs(r.text, "html.parser")
    versions_text = soup.find_all('div', class_='repository-content')
    version_and_all_text = (str(versions_text).split("version"))[1]
    version = version_and_all_text[6::]
    version_split = version.split('",')

    version = (version_split[0])[:-1]

    return version


def chech_version() -> bool:
    version_program = cfg.VERSION
    version_online = get_version()
    
    result = lambda v1, v2: str(v1) == str(v2) 
    return result(version_program, version_online)


def main():
    version = cfg.VERSION
    new_version = get_version()
    if not chech_version(): print(f"Your version ({version}) is outdated, download the latest version ({new_version}) from the link. (https://github.com/Sk1lizz/switch_site/)") 
    pass


def switch():
    pass


def info() -> str:

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
    debug = cfg.DEBUG

    # Текст
    text = f"""--------{name}--------\n     Name: {name}\n     Versions: {version}\n     Creator: {creator}\n     Root: {root}\n     Git-connect: {git_connect}\n     Date create: {date_create}\n     Last date update: {last_update}\n     Debug: {debug}\n Console: {console}      |      Gui: {gui}\n-------------<INFO  MENU>-------------"""

    return text


def help() -> str:

    # Вводим переменные
    name = cfg.NAME
    
    # Текст
    text = f"""--------{name}--------\n <1> - Main menu\n <2> - Switch menu\n <8> - Info menu\n <9> - Help menu  \n-------------<HELP  MENU>-------------"""

    return text

