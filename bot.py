

import random
import os
import telebot
from telebot import types

bot = telebot.TeleBot('5402030415:AAHxwuXe-G02_vUczSBAm4cuuV_ImuZ-cK8')





@bot.message_handler(commands=['start'])
def start(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
	btn1 = types.KeyboardButton('Развлечение')
	btn2 = types.KeyboardButton('Обои')
	
	markup.add(btn1, btn2)
	send_mess = f"<b>Привет {message.from_user.first_name} {message.from_user.last_name}</b>!\nЧто тебя интересует?"
	bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)
    
@bot.message_handler(content_types=['text'])
def send_message(message):
    chatId = message.chat.id
    text = message.text.lower()
    print(text)
    if text == "развлечение":
    
         markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
         btn1 = types.KeyboardButton('Мем')
         btn2 = types.KeyboardButton('Демотиватор')
         btn3 = types.KeyboardButton('Комикс')
         btn4 = types.KeyboardButton('Меню')
	
         markup.add(btn1, btn2, btn3, btn4)
         
         send_mess = f"\nКакие мемы тебя интересуют?"
         bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)
    
    elif text =="меню":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Развлечение')
        btn2 = types.KeyboardButton('Обои')
       
        
        markup.add(btn1, btn2)
        send_mess = f"\nЧто тебя интересует?"
        bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)
    
    elif text =="мем":
        photo = open('mem/' + random.choice(os.listdir('mem')), 'rb')
        bot.send_photo(chatId, photo)
    
    elif text =="демотиватор":
        photo = open('demo/' + random.choice(os.listdir('demo')), 'rb')
        bot.send_photo(chatId, photo)
    
    elif text =="комикс":
        photo = open('comix/' + random.choice(os.listdir('comix')), 'rb')
        bot.send_photo(chatId, photo)
    
    
    
    
    elif text =="обои":
         markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
         btn1 = types.KeyboardButton('Авто')
         btn2 = types.KeyboardButton('Девушки')
         btn3 = types.KeyboardButton('Природа')
         btn4 = types.KeyboardButton('Абстракция')
         btn5 = types.KeyboardButton('Животные')
         btn6 = types.KeyboardButton('Разное')
         btn7 = types.KeyboardButton('Меню')
	
         markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
         
         send_mess = f"\nКакие обои тебя интересуют?"
         bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)
    
    
    elif text =="авто":
        photo = open('auto/' + random.choice(os.listdir('auto')), 'rb')
        bot.send_photo(chatId, photo)
    elif text =="девушки":
        photo = open('girls/' + random.choice(os.listdir('girls')), 'rb')
        bot.send_photo(chatId, photo)
    elif text =="природа":
        photo = open('nature/' + random.choice(os.listdir('nature')), 'rb')
        bot.send_photo(chatId, photo)
    elif text =="абстракция":
        photo = open('abstr/' + random.choice(os.listdir('abstr')), 'rb')
        bot.send_photo(chatId, photo)
    elif text =="животные":
        photo = open('animal/' + random.choice(os.listdir('animal')), 'rb')
        bot.send_photo(chatId, photo)
    elif text =="разное":
        photo = open('other/' + random.choice(os.listdir('other')), 'rb')
        bot.send_photo(chatId, photo)




bot.polling()