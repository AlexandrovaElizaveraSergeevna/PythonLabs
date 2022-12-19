import telebot
import requests
import shutil
bot = telebot.TeleBot('5894126239:AAHyb566MIlQh8o36Ki-FGsq18w0FGozoi4') 
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет, я бот, который может скинуть тебе ссылку на картинку с котами. Тебе нужен кот?")
@bot.message_handler(content_types=['text'])
def get_user_text(message):
    user_text=message.text
    if (user_text=="Да") or (user_text=="да"):
        r = requests.get('http://thecatapi.com/api/images/get?format=src')
        url = r.url
        bot.send_photo(message.chat.id, url,)
        bot.send_message(message.chat.id, "Тебе нужен ещё один кот?")
    elif (user_text=="Нет") or (user_text=="нет"):
        bot.send_message(message.chat.id, "Больше я ничего не умею, может быть тебе всё-таки нужен кот?")
    else:
        bot.send_message(message.chat.id, "Извини, я тебя не понимаю. Тебе нужен кот?")
bot.polling(non_stop=True)