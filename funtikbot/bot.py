import telebot
from telebot import  types

bot = telebot.TeleBot('6072374525:AAFuKNIZz0rBSjc2Z-We8KWIyCbkycrGKvc')

# @bot.message_handler(commands=['start'])
# def start(message):
#     mess = f'Здравствуйте, <b>{message.from_user.first_name}</b>, я чат бот фунтик и помогаю людям, делать заказы' #ИСПРАВИТЬ ЕПТА НА ПРОСТО ПРИВЕТСТВИЕ
#     bot.send_message(message.chat.id, mess, parse_mode='html')


# @bot.message_handler()
# def get_user_text(message):
#     if message.text == "Hello":
#         bot.send_message(message.chat.id, "И ты пидорас!!!", parse_mode='html')
#     elif message.text == "ID":
#         bot.send_message(message.chat.id, f"Твой ID: {message.from_user.id}", parse_mode='html')
#     else:
#         bot.send_message(message.chat.id, f"<b>Иди ты в жопу, БЛЯТЬ!!!</b>", parse_mode='html')



@bot.message_handler(commands=['start'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    zakazz = types.KeyboardButton('Сделать заказ')
    markup.add(zakazz)
    bot.send_message(message.chat.id, f'Здравствуйте, <b>{message.from_user.first_name}</b>, я чат бот фунтик и помогаю людям, делать заказы', parse_mode='html', reply_markup=markup)

adm = 647232633

@bot.message_handler(content_types=['text'])
def send_welcome(message):
    if (message.text == "Сделать заказ"):
        msg = bot.send_message(message.chat.id, 'Отправь фотографию или ссылку')
        bot.register_next_step_handler(msg, forward_adm)


def forward_adm(message):
    print('forward_adm')
    print(message.chat.id)
    if message.content_type == 'photo':
        print(message.photo[-1].file_id)
        bot.send_photo(adm, message.photo[-1].file_id)
    else:
        bot.send_message(adm, message.text)
    forward_usr(message)


def forward_usr(message):
    print('forward_usr')
    print(message.chat.id)
    global usr_id
    usr_id = message.chat.id

    msg = bot.send_message(adm, 'введи ответ')
    bot.register_next_step_handler(msg, forward_usr_1)


def forward_usr_1(message):
    print('forward_usr_1')
    print(message.chat.id)
    bot.send_message(usr_id, '{}'.format(message.text))


bot.polling(none_stop=True)