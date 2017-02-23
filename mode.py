import message
import random


def setmode(cards):
    while True:
        message.choose_mode()
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
        break
    message.pack_completed()


def review(cards):
    message.review_mode_intro()
    message.choose_language(cards[0].front(), cards[0].back())
    lang = int(input().sptit(" ")[0]) % 2
    message.review_mode_legend()

    i = 1
    right_answers = 0
    packsz = len(cards)
    random.shuffle(cards)

    for card in cards:
        message.card_front(i, card.side(lang))
        message.previous_answer()
        user = input().strip()
        message.card_back(card.side(not lang))
        while True:
            try:
                if user in ["-1", "exit", "end"]:
                    break
                elif user in ["-2", "lang"]:
                    lang = not lang
                    cards.append(card)
                elif int(user) % 2:
                    right_answers += 1
                elif not (int(user) % 2):
                    cards.append(card)
                i += 1
                if i == packsz:
                    message.right_answers_number(right_answers, packsz)
            except ValueError:
                message.incorrect_command()
                message.review_mode_legend()
            else:
                break


def learn(cards):
    message.learn_mode_intro()
    message.choose_language(1, len(cards))
    while True:
        try:
            begin = int(input())
            if begin:
                end = int(input())
        except ValueError:
            message.incorrect_command()
            for card in cards:
                print(card.front, " - ", card.back)
        else:
            break
    if begin:
        cards = cards[begin-1:end-1]
    show = []
    message.learn_mode_legend()
    lang = True
    while True:
        for i in enumerate(cards):
            message.card_front(i[0], i[1].side(lang))
            if i[0] in show:
                message.card_back(i[1].side(not lang))
        while True:
            user = input().strip()
            try:
                if user in ["-9", "exit", "quit"]:
                    break
                elif user in ["-1", "lang"]:
                    lang = not lang
                elif user in ["-2", "rand"]:
                    random.shuffle(cards)
                elif user in ["-3", "all"]:
                    show = list(range(1, len(cards)))
                else:
                    show = [int(user)]
            except ValueError:
                message.incorrect_command()
            else:
                break


def test(cards):
    message.test_mode()


def noans(cards):
    message.noans_mode_intro()
    lang = True
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
    for card in cards:
        message.card_front(0, card.front)
        message.card_back(card.back)
