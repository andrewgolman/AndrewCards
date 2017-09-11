"""

Exercise library for the project.

Review, learn and no-answer mode are implemented. This file also contains a function that logs cards reviewed
into a certain file.

Functions: setmode, takes 1 argument with list of CardType objects (defined in cards.py).

"""


import message
import random
from config import path
from app_io import app_input

quits = ["-9", "exit", "quit"]
helps = ["h", "help", "-help", "/help"]


def setmode(cards):
    message.number_of_cards(len(cards))
    message.choose_mode()
    while True:
        mode = app_input().strip()
        if mode in ["1", "r", "review"]:
            review(cards)
        elif mode in ["2", "l", "learn"]:
            learn(cards)
        elif mode in ["3", "t", "test"]:
            test(cards)
        elif mode in ["4", "c", "constructing", "na", "noans"]:
            noans(cards)
        elif mode in helps:
            message.help_choose_mode()
            message.choose_mode()
            continue
        elif mode in quits:
            return
        else:
            message.incorrect_command()
            continue
        message.mode_finished()
        return


def choose_range(cards):
    message.choose_range(1, len(cards))
    while True:
        try:
            range = app_input()
            begin = range.split(" ")[0]
            if not begin:
                break
            if begin in quits:
                return None
            begin = int(begin)
            if begin < 0:
                raise ValueError
            if begin:
                end = int(range.split(" ")[1])
            else:
                end = len(cards)
            if end < begin:
                raise ValueError
        except (ValueError, IndexError):
            message.incorrect_command()
        else:
            break
    if begin:
        ch_cards = cards[begin-1:end]
    else:
        ch_cards = cards
    return ch_cards


def choose_lang(card):
    message.choose_language(card.front, card.back)
    while True:
        lang = app_input().split(" ")[0].strip()
        if lang in ["1", "9", "first"]:
            lang = False
        elif lang in ["2", "0", "second"]:
            lang = True
        elif lang in helps:
            message.help_not_available()
            continue
        elif lang in quits:
            return None
        else:
            continue
        return lang


def review(cards):
    message.review_mode_intro()
    lang = choose_lang(cards[0])
    if lang is None:
        return
    message.review_mode_legend()

    i = 1
    right_answers = 0
    prev_card = None
    packsz = len(cards)
    random.shuffle(cards)

    for card in cards:
        message.card_front(i, card.side(lang))
        message.previous_answer()
        user = app_input()
        while True:
            try:
                if user in quits:
                    return

                if user in helps:
                    message.help_review_mode()
                    message.card_front(i, card.side(lang))
                    message.previous_answer()
                    user = app_input()
                    continue
                elif user in ["-1", "lang", "change language"]:
                    lang = not lang
                    cards.append(card)
                elif not prev_card:
                    pass
                elif user in ["right", ""] or int(user) % 2:
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
                user = app_input()
            else:
                message.card_shifted(card.side(not lang))
                break


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

        user = app_input()
        try:
            if user in quits:
                break
            elif user in helps:
                message.help_learn_mode()
            elif user in ["-1", "lang"]:
                lang = not lang
                show = []
            elif user in ["-2", "rand", "mix"]:
                random.shuffle(ch_cards)
                show = []
            elif user in ["-3", "all"]:
                show = list(range(len(ch_cards)))
            elif user in ["-4", "range"]:
                lang = True
                ch_cards = choose_range(cards)
                if not ch_cards:
                    return
                show = []
            elif user in ["+", "n", "]", "next"]:
                if len(show) == 1:
                    show[0] += 1
                    show[0] %= len(cards)
                elif not show:
                    show = [0]
            elif user in ["-", "p", "[", "prev"]:
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
        lang = choose_lang(cards[0])
        if lang is None:
            return
        random.shuffle(cards)
        message.noans_mode_intro()
        i = 1
        for card in cards:
            message.card_front(i, card.side(lang))
            user = app_input()
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
        user = app_input()
        if user[0] not in ["y", "1", "9"]:
            break


def log_mistake(card):
    try:
        file = open(path + "verbessern.txt", "r")
    except Exception:
        file = None
    if not file or card not in file:
        file = open(path + "verbessern.txt", "a")
        file.write(card.front + " - " + card.back + "\n")
