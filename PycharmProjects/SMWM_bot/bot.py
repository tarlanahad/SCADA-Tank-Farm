import telebot
from flask import Flask, request
import os
import numpy as np

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

    s = ''
    d = np.genfromtxt('prayer_times.csv', delimiter=',', dtype=str)

    for i in range(len(d)):
        for j in range(len(d[0])):
            d[i, j] = d[i, j].replace("'", "").replace('"', '')

    head = d[0, :]
    d = d[1:]

    for row in d:
        s += row[0]
        s += '</br>'

        for j in [2, 3, 5, 6, 7, 8]:
            s += (head[j][:3] + ": " + row[j])
            s += '</br>'

        s += '------</br>'

    return s, 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
