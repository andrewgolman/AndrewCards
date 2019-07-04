import message
import random
from set_io import app_input, app_output
from ReturnGenerator import ReturnGenerator


class Mode:
    REVIEW = 1
    LEARN = 2
    RANDOM = 3
    NOANS = 4


quits = ["-9", "-q", "exit", "quit", "/quit"]
helps = ["h", "-h", "help", "-help", "/help"]


def choose_mode():
    while True:
        message.choose_mode()
        inp = app_input()
        if inp in ["1", "r", "review"]:
            return Mode.REVIEW
        elif inp in ["2", "l", "learn"]:
            return Mode.LEARN
        elif inp in ["3", "g", "random"]:
            return Mode.RANDOM
        elif inp in ["4", "n", "na", "noans"]:
            return Mode.NOANS
        elif inp in helps:
            message.help_choose_mode()
            continue
        elif inp in quits:
            return None
        else:
            message.incorrect_command()
            continue


def choose_range(n):
    message.choose_range(1, n)
    while True:
        inp = app_input()
        if inp in quits:
            return None

        try:
            if inp == "0":
                begin, end = 0, n
            else:
                begin, end = inp.split(maxsplit=1)
                begin = max(0, int(begin) - 1)
                end = min(n, int(end) - 1)
                if end < begin:
                    raise ValueError
            return begin, end

        except (ValueError, IndexError):
            message.incorrect_command()


def choose_lang(card):
    message.choose_language(card.front, card.back)
    while True:
        lang = app_input()
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


def run_review(cards, mode=Mode.REVIEW):
    message.review_mode_intro()
    message.review_mode_legend()

    size = len(cards)
    right_answers_count = 0

    ask_count = 1
    prev_card = None

    lang = choose_lang(cards[0])
    if lang is None:
        return

    if mode == Mode.RANDOM:  # create bootstrap generator, otherwise just shuffle
        cards = ReturnGenerator(cards)
    else:
        random.shuffle(cards)

    for card in cards:
        message.card_front(ask_count, card.side(lang))
        if mode == Mode.REVIEW:
            message.previous_answer()
        user = app_input()

        while True:
            try:
                if user in quits:
                    return

                if user in helps:
                    message.help_review_mode()
                    message.card_front(ask_count, card.side(lang))
                    if mode == Mode.REVIEW:
                        message.previous_answer()
                    user = app_input()
                    continue

                elif user in ["-1", "lang", "change language"]:
                    lang = not lang
                    if mode in [Mode.REVIEW, Mode.NOANS]:
                        cards.append(card)

                elif not prev_card or mode == Mode.NOANS:  # show answer for previous card otherwise
                    pass

                elif user in ["right", ""] or int(user) % 2:
                    right_answers_count += 1

                elif not (int(user) % 2):
                    cards.append(prev_card)  # add wrong answer to the end (ignore the only remaining last wrong answer)

                if ask_count == size:
                    message.right_answers_number(right_answers_count, size-1)

                ask_count += 1
                prev_card = card

            except ValueError:
                message.incorrect_command()
                message.review_mode_legend()
                user = app_input()
            else:
                if mode != Mode.NOANS:
                    message.card_shifted(card.side(not lang))
                break


def run_learn(cards):
    message.learn_mode_intro()
    chosen_ind = choose_range(len(cards))
    if chosen_ind is None:
        return

    chosen_cards = cards[chosen_ind[0]:chosen_ind[1]]

    message.learn_mode_legend()
    show = []
    lang = True
    while True:
        for i, card in enumerate(chosen_cards):
            message.card_front(i+1, card.side(lang))
            if i in show:
                message.card_back(card.side(not lang))
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
                random.shuffle(chosen_cards)
                show = []
            elif user in ["-3", "all"]:
                show = list(range(len(chosen_cards)))
            elif user in ["-4", "range"]:
                lang = True
                chosen_ind = choose_range(len(cards))
                if chosen_ind is None:
                    return
                chosen_cards = cards[chosen_ind[0]:chosen_ind[1]]
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


def run(pack):
    if not pack:
        app_output("Pack is empty")

    message.number_of_cards(len(pack))
    mode = choose_mode()
    if mode is None:
        return

    if mode in [Mode.REVIEW, Mode.NOANS, Mode.RANDOM]:
        run_review(pack, mode)

    if mode == Mode.LEARN:
        run_learn(pack)
