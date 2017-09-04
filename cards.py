"""

Data reading library for the project.

Implements class Cardtype - for double-sided cards with words/phrases.

Functions: parse_file, takes 1 string argument with file path

"""


import message
from config import path

formats = ["", ".txt", ".doc"]
last_pack = "No pack chosen"
separators = ["- ", "— ", "– "]


class Cardtype:
    def __init__(self, s):
        for sep in separators:
            s = s.replace(sep, '\t')
        self.front = s.split("\t")[0].strip()
        s_split = s.split("\t")
        self.front = s_split[0].strip()
        self.back = "- ".join(s_split[1:]).strip() if len(s_split) > 1 else ""

    def side(self, b):
        return self.front if b else self.back


def get_file(file_name):
    file = None
    for f in formats:
        try:
            file = open(path + file_name + f, "r")
        except OSError:
            pass
        else:
            break
    return file


def parse_file(file_name):
    file = get_file(file_name)
    if not file:
        message.file_not_found(file_name)
        return None
    lines = file.readlines()
    cards = []
    for l in lines:
        if l[0] == '!':
            break
        if l[0] != '/' and l.strip():
            cards.append(Cardtype(l))
    global last_pack
    last_pack = file_name
    return cards


def get_last():
    print(last_pack)
