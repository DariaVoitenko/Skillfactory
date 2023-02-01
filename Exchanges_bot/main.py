import telebot
from config import *
from extensions import Converter, APIException
import traceback

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def command_start(message: telebot.types.Message):
    bot.reply_to(message, f"Здравствуйте, {message.chat.username}, этот бот поможет  узнать тебе  курс выбранных валют, напишите /help для ознакомления с валютами")


@bot.message_handler(commands=['help'])
def command_help(message: telebot.types.Message):
    bot.reply_to(message, f"Чтобы начать работу введите команду боту в следующем формате:\n<имя валюты, цену которой хотите узнать> \
<имя валюты, в которой надо узнать цену первой валюты>\
<количество первой валюты>\nУвидеть список всех доступных валют: /values")


@bot.message_handler(commands=['values'])
def command_values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in exchanges.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def converter(message: telebot.types.Message):
    commands = message.text.split()
    try:
        if len(commands) != 3:
            raise APIException('Введите три параметра, пожалуйста!')

        answer = Converter.get_price(*commands)
    except APIException as e:
        bot.reply_to(message, f"Ошибка в команде:\n{e}")
    except Exception as e:
        traceback.print_tb(e.__traceback__)
        bot.reply_to(message, f"Неизвестная ошибка:\n{e}")
    else:
        bot.reply_to(message, answer)


bot.polling(none_stop=True)
