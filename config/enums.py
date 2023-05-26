from enum import Enum


class LanguageEnum(str, Enum):
    uz = "uz"
    rus = "rus"

class BotStatus(str, Enum):
    START = "start"
    MENU = "menu"
