import json

with open(r"files\config\config.json", "r", encoding='utf-8') as file:
    config_file = json.load(file)

NAME = config_file["name"]
VERSION = config_file["version"]
CREATOR = config_file["creator"]
ROOT = config_file["root"]
PLATFORMS = config_file["support_platforms"]
PLATFORMS_WINDOWS = PLATFORMS["Windows"]
PLATFORMS_LINUX = PLATFORMS["Linux"]
PLATFORMS_MACOS = PLATFORMS["MacOS"]
PLATFORMS_ANDROIS = PLATFORMS["Android"]
PLATFORMS_IOS = PLATFORMS["IOS"]
GIT_CONNECT = config_file["git-connect"]
DATE_CREATE = config_file["date-create"]
LAST_DATE_UPDATE = config_file["last-date-update"]
CONSOLE_SUPPORTIVE = config_file["console"]
GUI_SUPPORTIVE = config_file["gui"]
