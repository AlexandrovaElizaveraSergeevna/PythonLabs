import telebot
import requests
import shutil
bot = telebot.TeleBot('5894126239:AAHyb566MIlQh8o36Ki-FGsq18w0FGozoi4') 
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет, я бот, который может скинуть тебе ссылку на картинку с лисами. Тебе нужна лиса?")
@bot.message_handler(content_types=['text'])
def get_user_text(message):
    user_text=message.text
    if (user_text=="Да") or (user_text=="да"):
        img = requests.get('https://randomfox.ca/floof/')
        bot.send_message(message.chat.id, img)
        bot.send_message(message.chat.id, "Тебе нужна ещё одна лиса?")
    elif (user_text=="Нет") or (user_text=="нет"):
        bot.send_message(message.chat.id, "Больше я ничего не умею, может быть тебе всё-таки нужна лиса?")
    else:
        bot.send_message(message.chat.id, "Извини, я тебя не понимаю. Тебе нужна лиса?")
bot.polling(non_stop=True)