import message
import mode

formats = ["", ".txt", ".doc"]

class cardtype:

    def __itit__ (self, s):
        self.word = self.dash_separate(s)

    def front(self):
        return self.word[0]
    
    def back(self):
        return self.word[1]
    
    def side(self, b):
        if b:
            return self.front()
        return self.back()
    
    def dash_separate(s):
        a = s.split("- ", "\t")[0]
        b = s.split("- ", "\t")[1:].join()
        return [a, b]


def miss_line(s):
    if s[0] == '/':
        return True
    for c in s:
        if c.isspace():
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
                    mode.set(cards)
                else:
                    message.file_is_empty(file)


def get_pack(file):
    cards = []
    try:
        for s in open(file):
            if not miss_line(s):
                cards.append().s()
            if s[0] == '!':
                break
    except OSError:
        message.file_not_found()
        return None
    return cards
