import telebot
from flask import Flask, request
import os

TOKEN = '1271177952:AAFU_oRrTCWJMstUEP5rGB69UGqnpVaFnDY'

bot = telebot.TeleBot(token=TOKEN)
server = Flask(__name__)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'meow')


@bot.message_handler(commands=['Salam', 'salam'])
def send_salam(message):
    bot.reply_to(message, 'Salam, bəbiş hanımım')


@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://smwmbot.herokuapp.com/' + TOKEN)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
