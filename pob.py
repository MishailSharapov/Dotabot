Ыimport telebot
from heroes import *

bot = telebot.TeleBot("6251503082:AAFhJ6awdy-9P_cGrimMRgzvkDrwilD9ogs")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Введите в название героя и вашу позицию от 1-4(название героя должно соответсвовать его названию в игре) для получения предметов напишите цифру 6")

@bot.message_handler(content_types=['text'])
def func(message):   
    try:
        text=message.text
        text=text.replace(' ','_')
        index=len(text)-text[::-1].index('_')
        name, pos=text[:index-1],text[index:]
        name=name.replace(' ','_')
        print(name,pos)
        bot.send_message(message.chat.id, names[name][pos])
    except:
        bot.send_message(message.chat.id, 'Несооответствие формату ввода')
bot.polling()