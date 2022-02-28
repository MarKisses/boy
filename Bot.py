#! /usr/bin/env python
# -*- coding: utf-8 -*-
import telebot
import config

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start', 'help'])
def gandon(message):
    bot.send_message(message.chat.id, 'Пошёл нахуй')


@bot.message_handler(content_types=['text'])
def ohfuck(message):
    if message.chat.type == "group":
        bot.reply_to(message, 'Соси хуй и не психуй, дебил')


# Run
bot.polling(none_stop=True)
