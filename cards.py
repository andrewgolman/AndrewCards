import message
from config import path

formats = ["", ".txt", ".doc"]
last_pack = "No pack chosen"

# TODO ответ появляется при incorrect instruction

class Cardtype:
    def __init__(self, s):
        s = s.replace("- ", "\t")
        s = s.replace("— ", "\t")
        s = s.replace("– ", "\t")
        self.front = s.split("\t")[0].strip()
        try:
            self.back = s.split("\t")[1].strip()
        except IndexError:
            self.back = ""

    def side(self, b):
        return self.front if b else self.back


def miss_line(s):
    if s[0] == "/":
        return True
    for c in s:
        if not c.isspace():
            return False
    return True


def open_file():
    message.enter_the_file()
    inp = input()
    if inp in ["exit", "quit"]:
        return None
    
    global last_pack
    if inp in ["last"]:
        print("Your last pack: ", last_pack)
        inp = input()
    file = path + inp
    while True:
        try:
            cards = scan_file(file)
            if not cards:
                raise RuntimeError
        except OSError:
            message.file_not_found(file)
            file = path + input()
        except UnicodeDecodeError:
            message.incorrect_encoding()
            file = path + input()
        except RuntimeError:
            message.file_is_empty(file)
        else:
            break
    last_pack = inp
    return cards


def scan_file(file):
    lines = None
    for f in formats:
        try:
            lines = open(file+f, "r")
        except OSError:
            pass
        else:
            break
    else:
        raise OSError

    cards = []
    for l in lines:
        if l[0] == '!':
            break
        if not miss_line(l):
            cards.append(Cardtype(l))
    return cards
