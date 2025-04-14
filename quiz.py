from time import sleep
import schedule
import time
import threading
import telebot
from telebot.types import *
import s_taper
from s_taper.consts import *
                                                                                                     # @quiz_Patriot_bot
token1 = '7639501496:AAH5a4nDd3ifMRpPS-c0GZ_PKkhmsq09I4Y'
bot1 = telebot.TeleBot(token1)
data1 = {'id': INT+KEY, 'name': TEXT, 'score': INT, 'number_of_question': INT}  # FLT, TEXT, BLN
data2 = s_taper.Taper('users', 'data_quiz.db').create_table(data1)

def send_message():
    bot1.send_message(5907049975, "Я в сети!")

# Настройка расписания
schedule.every(4).hour.at(":00").do(send_message)

def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)

threading.Thread(target=run_schedule).start()

@bot1.message_handler(['start'])
def questions1(message1: Message):
    data3 = data2.read_all()
    for i in data3:
        if i[0] == message1.chat.id:
            bot1.send_message(message1.chat.id, 'вы уже начали!')
            break
    else:
        kb1 = InlineKeyboardMarkup()
        kb1.row(InlineKeyboardButton('Начать игру!', callback_data='yes1'))
        photo1 = open('{A6E98B04-6D95-4222-9851-4EC25FD035B4}.png', 'rb')
        bot1.send_photo(message1.chat.id, photo1, reply_markup=kb1)
        data2.write([message1.chat.id, message1.from_user.username, 0, 0])
@bot1.callback_query_handler(func=lambda call:True)
def quiz_hub1(call:telebot.types.CallbackQuery):
    player = data2.read('id', call.message.chat.id)
    if call.data == 'yes1':
        kb2 = InlineKeyboardMarkup()
        bot1.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=kb2)
        photo1 = open('{7822EA5A-39BA-41E4-9ADC-C8D1DBD74CE9}.png', 'rb')
        bot1.send_photo(call.message.chat.id, photo1)
    if call.data == 'yes2':
        kb2 = InlineKeyboardMarkup()
        bot1.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=kb2)
        player[2] += 1
        player[3] += 1
        data2.write(player)
    elif call.data == 'not2':
        kb2 = InlineKeyboardMarkup()
        bot1.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=kb2)
        player[3] += 1
        data2.write(player)
    if player[3] == 0:
        kb1 = InlineKeyboardMarkup()
        kb1.row(InlineKeyboardButton('Волонтерство и добровольчество', callback_data='not2'))
        kb1.row(InlineKeyboardButton('Патриотизм и историческая память', callback_data='yes2'))
        kb1.row(InlineKeyboardButton('Медиа и коммуникации', callback_data='not2'))
        photo1 = open('{3C208067-623C-4E72-845D-F827FF438C7D}.png', 'rb')
        bot1.send_photo(call.message.chat.id, photo1, reply_markup=kb1)
    elif player[3] == 1:
        kb1 = InlineKeyboardMarkup()
        kb1.row(InlineKeyboardButton('для командной работы', callback_data='yes2'))
        kb1.row(InlineKeyboardButton('для достижения личных результатов', callback_data='not2'))
        kb1.row(InlineKeyboardButton('для учета волонтерских часов', callback_data='not2'))
        photo1 = open('{DFBFFF11-2FB4-45A7-88EE-86CAFD0C4DF7}.png', 'rb')
        bot1.send_photo(call.message.chat.id, photo1, reply_markup=kb1)
    elif player[3] == 2:
        kb1 = InlineKeyboardMarkup()
        kb1.row(InlineKeyboardButton('обучающиеся образовательных учреждений и студенты СПО', callback_data='yes2'))
        kb1.row(InlineKeyboardButton('только студенты СПО', callback_data='not2'))
        kb1.row(InlineKeyboardButton('«Орлята России»', callback_data='not2'))
        photo1 = open('{340E64AF-7F90-4345-9D11-0A8446813B33}.png', 'rb')
        bot1.send_photo(call.message.chat.id, photo1, reply_markup=kb1)
    elif player[3] == 3:
        kb1 = InlineKeyboardMarkup()
        kb1.row(InlineKeyboardButton('президент школьного самоуправления', callback_data='not2'))
        kb1.row(InlineKeyboardButton('родитель', callback_data='yes2'))
        kb1.row(InlineKeyboardButton('куратор муниципального отделения «Движения Первых»', callback_data='not2'))
        photo1 = open('{E9528687-A049-48E5-9EF8-911D71BB373F}.png', 'rb')
        bot1.send_photo(call.message.chat.id, photo1, reply_markup=kb1)
    elif player[3] == 4:
        kb1 = InlineKeyboardMarkup()
        kb1.row(InlineKeyboardButton('Навигаторы Детства', callback_data='not2'))
        kb1.row(InlineKeyboardButton('Российское движение детей и молодёжи ', callback_data='yes2'))
        kb1.row(InlineKeyboardButton('Министерство образования Российской Федерации', callback_data='not2'))
        photo1 = open('{E33DB7E8-9C39-4D71-BF65-887025ED287A}.png', 'rb')
        bot1.send_photo(call.message.chat.id, photo1, reply_markup=kb1)
    elif player[3] == 5:
        kb1 = InlineKeyboardMarkup()
        kb1.row(InlineKeyboardButton('4', callback_data='not2'))
        kb1.row(InlineKeyboardButton('6', callback_data='not2'))
        kb1.row(InlineKeyboardButton('4 + финал', callback_data='yes2'))
        photo1 = open('{D4A4EED9-5837-41FE-A416-79E3473706C4}.png', 'rb')
        bot1.send_photo(call.message.chat.id, photo1)
        sleep(3)
        photo1 = open('{327F70AD-9C1B-45CC-BB0C-83B5172D417A}.png', 'rb')
        bot1.send_photo(call.message.chat.id, photo1, reply_markup=kb1)
    elif player[3] == 6:
        kb1 = InlineKeyboardMarkup()
        kb1.row(InlineKeyboardButton('20-22 лет', callback_data='yes2'))
        kb1.row(InlineKeyboardButton('14-17 лет', callback_data='not2'))
        kb1.row(InlineKeyboardButton('11-13 лет', callback_data='not2'))
        kb1.row(InlineKeyboardButton('7-10 лет', callback_data='not2'))
        photo1 = open('{D393E18C-CD89-4AFE-B2BE-6350702DE665}.png', 'rb')
        bot1.send_photo(call.message.chat.id, photo1, reply_markup=kb1)
    elif player[3] == 7:
        kb1 = InlineKeyboardMarkup()
        kb1.row(InlineKeyboardButton('рейтинг бойца', callback_data='not2'))
        kb1.row(InlineKeyboardButton('рейтинг отряда', callback_data='not2'))
        kb1.row(InlineKeyboardButton('рейтинг взвода', callback_data='yes2'))
        photo1 = open('{8618AE5D-8C47-4468-B90A-F3A13A74D35B}.png', 'rb')
        bot1.send_photo(call.message.chat.id, photo1, reply_markup=kb1)
    elif player[3] == 8:
        kb1 = InlineKeyboardMarkup()
        kb1.row(InlineKeyboardButton('8 человек', callback_data='not2'))
        kb1.row(InlineKeyboardButton('6 человек', callback_data='not2'))
        kb1.row(InlineKeyboardButton('10 человек', callback_data='yes2'))
        photo1 = open('{49214FA4-575E-4743-AC9A-C41472D1BB0A}.png', 'rb')
        bot1.send_photo(call.message.chat.id, photo1, reply_markup=kb1)
    elif player[3] == 9:
        kb1 = InlineKeyboardMarkup()
        kb1.row(InlineKeyboardButton('командир', callback_data='not2'))
        kb1.row(InlineKeyboardButton('сапёр', callback_data='not2'))
        kb1.row(InlineKeyboardButton('артиллерист', callback_data='yes2'))
        kb1.row(InlineKeyboardButton('медик', callback_data='not2'))
        photo1 = open('{D6854542-BE8E-4477-A461-3764009FCFFB}.png', 'rb')
        bot1.send_photo(call.message.chat.id, photo1, reply_markup=kb1)
    elif player[3] == 10:
        photo1 = open('{23F71189-9FA5-4DC9-8FF1-27E372A098DB}.png', 'rb')
        bot1.send_photo(call.message.chat.id, photo1)
        bot1.send_message(call.message.chat.id, f'''вы ответили на все вопросы и ваш счет составил - {player[2]},
спасибо за участие!''')






bot1.infinity_polling()





