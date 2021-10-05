import telebot
from telebot import TeleBot
import random

import constants


bot = TeleBot(constants.token)



# Метод, который получает сообщения и обрабатывает их


@bot.message_handler(commands=['start'])
def handle_message(message):
    bot.reply_to(message, "hi")

@bot.message_handler(content_types=['text'])
def handle_message(message):
    bot.reply_to(message, message.text)

bot.polling()







#bot.polling(none_stop=True, interval=0)
