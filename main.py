"""

Main script, runs the exercises part of the application.

"""

import cards
import mode
from app_io import app_input, app_output
from sys import stderr
from message import helpmsg, enter_the_file


def main():
    app_output("Welcome to AndrewCards5.0! With this application You can learn and review foreign words and phrases!")

    while True:
        try:
            enter_the_file()
            inp = app_input().strip()
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
        except EOFError:
            break
        except Exception as e:
            stderr.write(str(e) + '\n')
            app_output("\n An error occurred somewhere, sorry about that. You can continue from MAIN MENU.")

    app_output("Thanks for using AndrewCards5.0! Stay tuned and keep learning:)")


if __name__ == '__main__':
    main()
