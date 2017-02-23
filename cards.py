import message
import mode

formats = ["", ".txt", ".doc"]


class Cardtype:
    def __init__(self, s):
        self.front = s.split("- ", "\t")[0]
        try:
            self.back = s.split("- ", "\t")[1:].join()
        except IndexError:
            self.back = ""

    def side(self, b):
        return self.front if b else self.back


def miss_line(s):
    if s[0] == '/':
        return True
    for c in s:
        if not c.isspace():
            return False
    return True


def menu():
    message.menu()
    while True:  # for i in range(10)
        message.enter_the_file()
        file = input().strip()
        if file in ["0", "exit", "quit"]:
            message.goodbye()
            return
        elif file in ["f1", "info"]:
            message.helpmsg()
        else:
            cards = get_pack(file)
            if cards:
                if len(cards):
                    message.scanned_successfully(len(cards), file)
                    mode.setmode(cards)
                else:
                    message.file_is_empty(file)


def get_pack(file):
    cards = []
    try:
        for s in open(file):
            if not miss_line(s):
                cards.append(Cardtype(s))
            if s[0] == '!':
                break
    except OSError:
        message.file_not_found(file)
        return None
    return cards
