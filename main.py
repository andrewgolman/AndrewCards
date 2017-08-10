import cards
import mode

def main():
    print("Welcome to AndrewCards5.0! With this application You can learn and review foreign words and phrases!")
    while True:
        pack = cards.open_file()
        if not pack:
            break
        mode.setmode(pack)

    print("Thanks for using AndrewCards5.0! Stay tuned and keep learning:)")


if __name__ == '__main__':
    main()
