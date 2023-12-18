import telebot

from main import search_n3ws, search_company3, push_kitt3ns

bot = telebot.TeleBot('6870489255:AAFpdAONLSKjTq4CKc61QjfLIb01snH4LF8')

@bot.message_handler(commands=['n3ws'])
def n3ws_message(message):
    bot.send_message(message.chat.id, "Сейчас будет выведено 10 последних статей на Хабр!")
    lis = search_n3ws()
    for title in lis:
        bot.send_message(message.chat.id, title)

@bot.message_handler(commands=['company3'])
def company3_message(message):
    bot.send_message(message.chat.id, "Сейчас будет выведено 10 компаний из Хабра")
    lis = search_company3()  # Передаем значение в search_n3ws
    for title in lis:
        bot.send_message(message.chat.id, title)

@bot.message_handler(commands=['kitt3ns'])
def company3_message(message):
    bot.send_message(message.chat.id, "Сейчас будут котики!")
    lis = push_kitt3ns()  # Передаем значение в search_n3ws
    for title in lis:
        bot.send_photo(message.chat.id, title)

bot.polling(none_stop=True)

