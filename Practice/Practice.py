import telebot
from telebot import types
TOKEN = telebot.TeleBot('5447587625:AAGDRTk_TtwihLhepN5qpzz-EjnhxzQXkUk')


@TOKEN.message_handler(commands=['start'])
def start (message):
    mess = f'Hello, <b>{message.from_user.first_name}</b>!'
    TOKEN.send_message(message.chat.id,mess,parse_mode='html')

@TOKEN.message_handler(content_types=['sticker'])
def user_sth_stiker(message):
    TOKEN.send_message(message.chat.id,"<b>XD</b>",parse_mode='html')


@TOKEN.message_handler(content_types=['text'])
def user_sth_text(message):
    if message.text == "Hello":
        TOKEN.send_message(message.chat.id,"Hello to you too",parse_mode='html')
    elif message.text == "ID":
        TOKEN.send_message(message.chat.id,f"Your ID: {message.from_user.id}",parse_mode='html')
    elif message.text == "Photo":
        photo = open('YGZlZ_vHb5k.jpg', 'rb')
        TOKEN.send_photo(message.chat.id, photo)
    elif message.text == "Carefully" :
        audio = open('Carefully.mp3', 'rb')
        TOKEN.send_audio(message.chat.id, audio)
    elif message.text == "Tchh" :
        audio = open('Tchh.mp3', 'rb')
        TOKEN.send_audio(message.chat.id, audio)
    elif message.text == "/help":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        Weather = types.KeyboardButton('Wether')
        VK = types.KeyboardButton('VK')
        markup.add(Weather,VK)
        TOKEN.send_message(message.chat.id,"Choose your destiny",reply_markup=markup)
    elif message.text == "Wether":
        TOKEN.send_message(message.chat.id,"https://yandex.ru/pogoda/dokuchaievsk")
    elif message.text == "VK":
        TOKEN.send_message(message.chat.id,"https://vk.com/dimableidd")
    else:
        TOKEN.send_message(message.chat.id,f"I dunno",parse_mode='html')

TOKEN.polling(none_stop=True)