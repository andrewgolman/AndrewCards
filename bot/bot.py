from telegram.ext import Updater
import logging
import traceback
from random import randint
import time

from telegram import TelegramError
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

token = open("token", "r").read().strip()


def telegram_error_handler(bot, update, err):
    traceback.print_exception(TelegramError, err, None)


def start(bot, update):
    update.message.reply_text("Welcome! I'm NEVERSTOPPRACTICING bot and I want you to practice English every few hours every day:)")
    help(bot, update)


def go(bot, update):
    # id = update.message.from_user.id
    sending(update)
    # for u in updates:
    #     if u.message.from_user.id == id:
    #         return
    # updates.append(update)


def help(bot, update):
    update.message.reply_text("""
Few times a day I'll send you various words and expressions \
so you can make up sentences using them and practice. You can contact \
the developers on andrewsgolman@gmail.com. Have a nice day!

1.0 - expressions from 'Harry Potter And The Chamber Of Secrets' are available

Available commands for the bot:
/get - get 3 words
/help - see this message once again
""")


def stop(bot, update):
    for u in updates:
        if update.message.from_user.id == u.message.from_user.id:
            updates.remove(u)


handlers = [
    CommandHandler("start", start),
    CommandHandler("get", go),
    # CommandHandler("stop", stop),
    CommandHandler("help", help),
]

updates = []


def main():
    updater = Updater(token=token)
    dp = updater.dispatcher

    for handler in handlers:
        dp.add_handler(handler)

    updater.start_polling(timeout=100000)
    # updater.idle()


if __name__ == '__main__':
    main()


def manager():
    times = ["10:45", "12:10"]
    while True:
        if time.strftime("%H:%M") in times:
            sending()


def sending(update):
    data = open("./cards/hp_bot.txt", "r").readlines()
    for i in range(3):
        n = randint(0, len(data))
        #for u in updates:
        u = update
        u.message.reply_text(data[n], reply_markup=ReplyKeyboardMarkup([["/get"]]))
