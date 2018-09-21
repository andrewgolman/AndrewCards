from telegram.ext import Updater
import logging
import traceback
from socket import socket
from config import port
import subprocess
from time import sleep

from telegram import TelegramError
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)

try:

    token = open("main_bot_token", "r").read().strip()

    sock = socket()

    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        filename="logs",
        filemode='a'
    )


    def telegram_error_handler(bot, update, err):
        traceback.print_exception(TelegramError, err, None)


    def check_access(update):
        if update.message.from_user.id != 300113793:
            update.message.reply_text("Access denied")
            return False
        return True


    def start(bot, update):
        if not check_access(update):
            return
        global sock
        subprocess.Popen(["python3", "main.py"])
        sleep(1)
        sock.connect(('localhost', port))
        s = sock.recv(1024)
        update.message.reply_text(s.decode())


    def help(bot, update):
        if not check_access(update):
            return
        global sock
        sock.send("-help".encode())
        s = sock.recv(1024)
        update.message.reply_text(s.decode())


    def app_get(bot, update):
        if not check_access(update):
            return
        s = update.message.text
        global sock
        sock.send(s.encode())
        s = sock.recv(1024)
        update.message.reply_text(s.decode(), reply_markup=ReplyKeyboardMarkup([['1', '2', '-1', '-9', '[', ']']]))

    handlers = [
        CommandHandler("start", start),
        CommandHandler("help", start),
        MessageHandler(Filters.text, app_get),
    ]

    updates = []


    def main():

        updater = Updater(token=token)
        dp = updater.dispatcher

        for handler in handlers:
            dp.add_handler(handler)

        try:
            updater.start_polling()
            updater.idle()
        except Exception as e:
            open("error.log", "a").write(str(e))

        sock.close()

    if __name__ == '__main__':
        main()

    open("error.log", "a").write("Completed")

except Exception as e:
    open("error.log", "a").write(str(e))


    
