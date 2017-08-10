import message
import random

quits = ["-9", "exit", "quit"]


def setmode(cards):
    print("The pack contains ", len(cards), "cards")
    message.choose_mode()
    while True:
        mode = input().strip()
        if mode in ["1", "r", "review"]:
            review(cards)
        elif mode in ["2", "l", "learn"]:
            learn(cards)
        elif mode in ["3", "t", "test"]:
            test(cards)
        elif mode in ["4", "c", "constructing", "na", "noans"]:
            noans(cards)
        else:
            message.incorrect_command()
            continue
        message.mode_finished()
        break


def review(cards):
    message.review_mode_intro()
    message.choose_language(cards[0].back, cards[0].front)
    while True:
        lang = input().split(" ")[0].strip()
        if lang in ["1", "9", "first"]:
            lang = True
        elif lang in ["2", "0", "second"]:
            lang = False
        elif lang in quits:
            return
        else:
            continue
        break
    message.review_mode_legend()

    i = 1
    right_answers = 0
    prev_card = None
    packsz = len(cards)
    random.shuffle(cards)

    for card in cards:
        message.card_front(i, card.side(lang))
        message.previous_answer()
        user = input().strip()
        message.card_shifted(card.side(not lang))
        while True:
            try:
                if user in quits:
                    return
                elif user in ["-2", "lang", "change language"]:
                    lang = not lang
                    cards.append(card)
                elif not prev_card:
                    pass
                elif (user in ["right", ""] or int(user) % 2):
                    right_answers += 1
                elif not (int(user) % 2):
                    cards.append(prev_card)
                    log_mistake(prev_card)
                if i == packsz:
                    message.right_answers_number(right_answers, packsz-1)
                i += 1
                prev_card = card
            except ValueError:
                message.incorrect_command()
                message.review_mode_legend()
                user = input().strip()
            else:
                break


def choose_range(cards):
    message.choose_range(1, len(cards))
    begin, end = 0, 0
    while True:
        try:
            begin = input().strip()
            if not begin:
                break
            if begin in quits:
                break
            begin = int(begin)
            if begin < 0:
                raise ValueError
            if begin:
                end = int(input().strip())
        except ValueError:
            message.incorrect_command()
            for card in cards:
                print(card.front, "-", card.back)
        else:
            break
    if begin:
        ch_cards = cards[begin-1:end]
    else:
        ch_cards = cards
    return ch_cards


def learn(cards):
    message.learn_mode_intro()
    ch_cards = choose_range(cards)
    if not ch_cards:
        return

    message.learn_mode_legend()
    show = []
    lang = True
    while True:
        for i in enumerate(ch_cards):
            message.card_front(i[0]+1, i[1].side(lang))
            if i[0] in show:
                message.card_back(i[1].side(not lang))
            else:
                print()

        user = input().strip()
        try:
            if user in quits:
                break
            elif user in ["-1", "lang"]:
                lang = not lang
            elif user in ["-2", "rand"]:
                random.shuffle(ch_cards)
                show = []
            elif user in ["-3", "all"]:
                show = list(range(len(ch_cards)))
            elif user in ["-4", "range"]:
                ch_cards = choose_range(cards)
                show = []
            elif user in ["+", "n", "next"]:
                if len(show) == 1:
                    show[0] += 1
                elif not show:
                    show = [0]
            elif user in ["-", "p", "prev"]:
                if len(show) == 1:
                    show[0] -= 1
                elif not show:
                    show = [len(cards)-1]
            else:
                show = [int(user)-1]
        except ValueError:
            message.incorrect_command()


def test(cards):
    message.test_mode()


def noans(cards):
    while True:
        message.choose_language(cards[0].front, cards[0].back)
        while True:
            lang = input().split(" ")[0].strip()
            if lang in ["1", "9", "first"]:
                lang = False
            elif lang in ["2", "0", "second"]:
                lang = True
            else:
                continue
            break
        random.shuffle(cards)
        message.noans_mode_intro()
        i = 1
        for card in cards:
            message.card_front(i, card.side(lang))
            user = input().strip()
            if user in ["lang"]:
                lang = not lang
            elif user in ["answer"]:
                message.card_shifted(card.side(not lang))
            elif user in ["quit"]:
                break
            i += 1
        i = 1
        for card in cards:
            print()
            message.card_front(i, card.front)
            message.card_back(card.back)
            i += 1
        message.try_again()
        user = input().strip()
        if user[0] not in ["y", "1", "9"]:
            break


def log_mistake(card):
    try:
        file = open("cards/verbessern.txt", "r")
    except Exception:
        file = None
    if not file or card not in file:
        file = open("cards/verbessern.txt", "a")
        file.write(card.front + " - " + card.back + "\n")
