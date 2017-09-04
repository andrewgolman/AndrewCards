"""

Main script, runs the exercises part of the application.

"""

import cards
import mode
from sys import stderr
from message import helpmsg, enter_the_file


def main():
    print("Welcome to AndrewCards5.0! With this application You can learn and review foreign words and phrases!")

    try:
        while True:
            enter_the_file()
            inp = input()
            if inp == "-help":
                helpmsg()
            elif inp == "-last":
                cards.get_last()
            elif inp == "-quit":
                break
            else:
                pack = cards.parse_file(inp)
                if pack:
                    mode.setmode(pack)
    except Exception as e:
        stderr.write(str(e))
        print("\n An error occurred somewhere, sorry about that. You can continue from MAIN MENU.")

    print("Thanks for using AndrewCards5.0! Stay tuned and keep learning:)")


if __name__ == '__main__':
    main()
