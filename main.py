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


def main(working_file=None):
    app_output("Welcome to AndrewCards5.0! With this application You can learn and review foreign words and phrases!")

    last_success_file = None
    while True:
        try:
            if working_file:
                file = open_file(working_file)
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
                    print(f"OPEN: .{inp}.")
                    file = open_file(inp)
                    if not file:
                        app_output("Can't read file {}".format(inp))
                        continue

            pack = parse_file(file)
            if pack:
                last_success_file = file
                train.run(pack)

            if working_file:
                break

        except EOFError:
            break

    app_output("Thanks for using AndrewCards5.0! Stay tuned and keep learning:)")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("file", default=None, nargs="?")
    args = parser.parse_args()
    print(args)
    main(working_file=args.file)
