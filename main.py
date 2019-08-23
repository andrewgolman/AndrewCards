import train
from set_io import app_input, app_output
from message import helpmsg, menu_msg

import argparse


class Cardtype:
    separators = ["- ", "— ", "– "]

    def __init__(self, s):
        for sep in Cardtype.separators:
            s = s.replace(sep, '\t')

        s = s.split("\t", maxsplit=1)
        self.front = s[0].strip()
        if len(s) > 1:
            self.back = s[1].strip()
        else:
            self.back = ""

    def side(self, b):
        return self.front if b else self.back


def open_file(file_name):
    formats = ["", ".txt", ".doc"]
    for f in formats:
        try:
            return open(file_name + f, "r")
        except OSError:
            pass
    print(f"{file_name}: file not found")
    return None


def parse_file(file):
    lines = file.readlines()
    cards = []
    for l in lines:
        if l[0] == '!':
            break
        if l[0] != '/' and l.strip():
            cards.append(Cardtype(l))
    return cards


def cards_from_file(file):
    stream = open_file(file)
    if stream:
        return parse_file(stream)
    return []


def cards_from_files(files):
    cards = list()
    for f in files:
        cards.extend(cards_from_file(f))
    return cards


def range_by_splits(splits):
    # todo
    if splits[0]:
        n = splits[0]
        return 25 * (n - 1), 25 * n
    if splits[1]:
        n = splits[1]
        return 200 * (n - 1), 200 * n
    return None

def main(working_files=None, splits=None, begin=None, end=None):
    app_output("Welcome to AndrewCards6.1!")


    if begin or end:
        # todo check numbers
        if begin:
            begin -= 1
        else:
            begin = 0
        # end included, None runs list to the end
        cards_range = begin, end
    elif splits:
        cards_range = range_by_splits(splits)
    else:
        cards_range = None

    last_success_file = None
    while True:
        try:
            if working_files:
                cards = cards_from_files(working_files)
                if not cards:
                    return
            else:
                app_output(menu_msg)
                inp = app_input()

                if inp in ["-h", "-help"]:
                    app_output(helpmsg)
                    continue
                elif inp == ["-l", "-last"]:
                    app_output(last_success_file)
                    continue
                elif inp == ["-q", "-quit"]:
                    break
                else:
                    cards = cards_from_file(inp)
                    if not cards:
                        app_output("Can't read file {}".format(inp))
                        continue
                    last_success_file = inp

            if cards_range:
                cards = cards[cards_range[0]:cards_range[1]]
            if cards:
                train.run(cards)

            if working_files:
                break

        except EOFError:
            break

    app_output("Thanks for using AndrewCards! Stay tuned and keep learning:)")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    # todo
    parser.add_argument("file", nargs="*", help="one or several files with cards")
    parser.add_argument("-n", nargs="?", type=int, help="split by 25 cards")
    parser.add_argument("-nh", nargs="?", type=int, help="split by 200 cards")
    parser.add_argument("-b", nargs="?", type=int, help="begin index")
    parser.add_argument("-e", nargs="?", type=int, help="end index")
    args = parser.parse_args()
    main(working_files=args.file, splits=[args.n, args.nh], begin=args.b, end=args.e)
