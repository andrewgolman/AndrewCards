from set_io import app_output
from config import mode

dot_string = "." * 40 if mode == 'console' else "Answer: "


def card_back(s):
    app_output(f" - {s}")


def card_front(n, s):
    app_output(f"{n}. {s}", end=" ")


def card_shifted(s):
    app_output(dot_string + s)


def choose_language(a,  b):
    app_output("Type '1' or '2' to choose the language to be used to ask questions")
    app_output(f"1. as {b}")
    app_output(f"2. as {a}")


def choose_mode():
    app_output("Choose the mode.")
    app_output("1. Reviewing")
    app_output("2. Learning")
    app_output("3. Random picking")
    app_output("4. No-answer reviewing")
    app_output("5. Pack reordering")


def choose_range(a, b):
    app_output(f"Choose range within {a} - {b}")
    app_output("Enter two numbers in the same line, separated with space.")
    app_output("Enter '0' to choose all the cards.")


def incorrect_command():
    app_output("Incorrect instruction. Please, try again.")


def help_not_available():
    app_output("No further help available")


def learn_mode_intro():
    app_output("Learn mode selected")


def learn_mode_legend():
    app_output()
    app_output("-1. Switch the language.")
    app_output("-2. Mix the cards.")
    app_output("-3. Show all translations.")
    app_output("-9. Quit.\n")


def menu():
    app_output()
    app_output("MENU")


def noans_mode_intro():
    app_output("Constructing mode selected")


def number_of_cards(n):
    app_output(f"The pack contains {n} cards")


def pack_completed():
    app_output("The pack is completed!")


def previous_answer():
    app_output("\n prev:", end=" ")


def review_mode_intro():
    app_output("Review mode selected")


def review_mode_legend():
    app_output()
    app_output("1. Right answer")
    app_output("2. Wrong answer")
    app_output("-2. Change the language")
    app_output("-9. Quit")


def right():
    app_output("Right")


def right_answers_number(a, b):
    app_output(f"Right answers: {a}/{b}")


def test_mode():
    app_output()
    app_output("-1. Quit")
    app_output("-2. Switch the language")
    app_output("Enter Your answer")


def try_again():
    app_output("Do it once again?")


def wrong(s):
    app_output(f"Wrong. Right answer - {s}")


helpmsg = """
Available commands:
    -last: see the path of the last chosen file
    -help: see this message
    -quit: leave the app

WHICH FILES TO USE?

This app requires a special format for its input files.
 Only plain text files are supported. If you use a file in '.txt' format, you can enter its path without '.txt'.
 Every line will be transformed into a card. You can separate two sides of the card by tabulation or a dash ('-').
 Lines beginning with a slash ('/') will be ignored.
 If a line begins with a '!' sign, all the remaining lines will be ignored (so you can write comments underneath).

Example of a correct input file:

  Hello - hallo
  world - Welt
  /I don't want you to scan this line
  card    Karte
  !
  I can write here whatever I want.

3 cards will be scanned here:
Hello   hallo
world   Welt
card    Karte

Please, make sure that encoding of your file is Unicode - otherwise they may be displayed incorrectly
 or you may get a file-reading error.

WHERE TO SAVE THESE FILES?

In the file config.py you can change the search path for the app. The directory containing the directory named '__app'
  is set by default. Anyway, the app asks your OS to open the file named 'config.path'+your_input
  (string concatenation), so you can make your own file systems.

WHAT TO DO NEXT?

After entering the file name you will be ask to choose a mode. Try some, type 'help' when you need and work out your
 own system of learning cards!

 The author of this app recommends making packs with no more than 30 cards. At first, you can remember 10-15 cards
 using the LEARN MODE. When you feel that you can keep all the cards in the pack in mind, try REVIEW MODE.
 Don't forget to get back to the cards you've learned and review them!

IT'S NOT VERY USER-FRIENDLY!

Please, follow the given instructions carefully so the app is able to parse your inputs. Most commands are simple,
 you will get used to the format soon and won't get many "Incorrect input" messages.

"""


def help_choose_mode():
    app_output("""
4 modes are ready now:

REVIEW MODE:
    You are holding a pile of cards. Shuffle them, take the topmost card and try to remember, what is written
     on the other side!

    We are not asking you to type the answers: that takes a huge amount of time and energy. But you can
     mark the cards as wrong-answered and it will appear by the end of the mode once again and will be logged to
     your mistakes file.

LEARN MODE:
    You have put a few cards on the table. You can take any of them and see, what's written on the other side. Try
     to remember all the cards!
     
RANDOM MODE:
    Random card on each step
    
NO ANSWER REVIEW:
    Same as review, but no answers are shown

""")


def help_review_mode():
    app_output("""
Available commands:
    ENTER or any odd number or 'right'
    ...................... My last answer was right (simply proceed to the next card)
    Any even number or 'wrong'
    ...................... My last answer was wrong (proceed to the next card and save my wrong answer)
    '-1' or 'lang'
    ...................... Change language
    '-9' or 'quit'
    ...................... Return to main MENU
    'h' or 'help'
    ...................... See this message
""")


def help_learn_mode():
    app_output("""
Available commands:
    Any number n
    ...................... See the back side of the card #n
    '-1' or 'lang'
    ...................... Change language
    '-2' or 'mix'
    ...................... Shuffle the cards
    '-3' or 'all'
    ...................... See all the back sides
    '-9' or 'quit'
    ...................... Return to main MENU
    'n' or ']' or 'next'
    ...................... See the back side of the next card
    'p' or '[' or 'prev'
    ...................... See the back side of the previous card
    'h' or 'help'
    ...................... See this message
""")


menu_msg = """

MAIN MENU
Enter the path to the file.
[-quit, -q]: quit
[-last, -l]: last opened file
[-help, -h]: help
"""
