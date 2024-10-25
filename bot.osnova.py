import telebot
import buttons as bt
import database as db
from geopy import Photon

geolocator = Photon(user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36")
bot = telebot.TeleBot(token="7544507295:AAHcVFQ08sRzPTTjTA4Auqw9AiPENwxnDO8")

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    bot.send_message(user_id,"Добро пожаловать в бот донеров")
    checker = db.check_user(user_id)
    if checker == True:
        bot.send_message(user_id, "Главное меню: ")
    elif checker == False:
        bot.send_message(user_id, "Enter your name for register")
        print(message.text)
        bot.register_next_step_handler(message, get_name)

def get_name(message):
    user_id = message.from_user.id
    name = message.text
    print(message.text)
    bot.send_message(user_id,"Теперь скажите номер ", reply_markup=bt.phone_button())
    bot.register_next_step_handler(message, get_phone_number, name)

def get_phone_number(message, name):
    user_id = message.from_user.id
    if message.contact:
        phone_number = message.contact.phone_number
        print(phone_number)
        bot.send_message(user_id, "Отправьте свою локацию", reply_markup=bt.location_button())
        bot.register_next_step_handler(message, get_location, name, phone_number)
    else:
        bot.send_message(user_id, 'ОТПРАВЬТЕ СВОЙ НОМЕР ЧЕРЕЗ КНОПКУУ')
        bot.register_next_step_handler(message, get_phone_number, name)

def get_location(message, name, phone_number):
    user_id = message.from_user.id
    if message.location:
        latitude = message.location.latitude
        longitude = message.location.longitude
        address = geolocator.reverse((latitude, longitude)).address
        print(name, phone_number, address)
        db.add_user(name=name, phone_number=phone_number, user_id=user_id)
        bot.send_message(user_id,"Вы успешно прошли регистрацию")
        bot.send_message(user_id, "Главное меню: ")

bot.infinity_polling()
