import telebot
import buttons as bt
import database as db
from geopy import Photon

geolocator = Photon(user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36")
bot = telebot.TeleBot(token="7544507295:AAHcVFQ08sRzPTTjTA4Auqw9AiPENwxnDO8")
db.add_product("Бургер", 20000, "лучший бургер", 10, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSf2535-40OVw2m6L8Auogu_w8LFXJfvV_XNw&s")
db.add_product("Хотдог", 15000, "лучший хотдог", 0, "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/4QC+RXhpZgAASUkqAAgAAAAEAA4BAgBZAAAAPgAAAJiCAgAPAAAAlwAAABoBBQABAAAApgAAABsBBQABAAAArgAAAAAAAABIb3QgRG9nIHdpdGggS2V0Y2h1cCxNdXN0YXJkLFJlbGlzaCBhbmQgT25pb25zIC0gUGhvdG9ncmFwaGVkIG9uIEhhc3NlbGJsYWQgQ2FtZXJhIFN5c3RlbUxhdXJpIFBhdHRlcnNvbiwBAAABAAAALAEAAAEAAAD/7QCyUGhvdG9zaG9wIDMuMAA4QklNBAQAAAAAAJYcAlAADkxhdXJpUGF0dGVyc29uHAJ4AFlIb3QgRG9nIHdpdGggS2V0Y2h1cCxNdXN0YXJkLFJlbGlzaCBhbmQgT25pb25zIC0gUGhvdG9ncmFwaGVkIG9uIEhhc3NlbGJsYWQgQ2FtZXJhIFN5c3RlbRwCdAAPTGF1cmkgUGF0dGVyc29uHAJuAAxHZXR0eSBJbWFnZXP/4QXMaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLwA8P3hwYWNrZXQgYmVnaW49Iu+7vyIgaWQ9Ilc1TTBNcENlaGlIenJlU3pOVGN6a2M5ZCI/Pgo8eDp4bXBtZXRhIHhtbG5zOng9ImFkb2JlOm5zOm1ldGEvIj4KCTxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+CgkJPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6cGhvdG9zaG9wPSJodHRwOi8vbnMuYWRvYmUuY29tL3Bob3Rvc2hvcC8xLjAvIiB4bWxuczpJcHRjNHhtcENvcmU9Imh0dHA6Ly9pcHRjLm9yZy9zdGQvSXB0YzR4bXBDb3JlLzEuMC94bWxucy8iICAgeG1sbnM6R2V0dHlJbWFnZXNHSUZUPSJodHRwOi8veG1wLmdldHR5aW1hZ2VzLmNvbS9naWZ0LzEuMC8iIHhtbG5zOmRjPSJodHRwOi8vcHVybC5vcmcvZGMvZWxlbWVudHMvMS4xLyIgeG1sbnM6cGx1cz0iaHR0cDovL25zLnVzZXBsdXMub3JnL2xkZi94bXAvMS4wLyIgIHhtbG5zOmlwdGNFeHQ9Imh0dHA6Ly9pcHRjLm9yZy9zdGQvSXB0YzR4bXBFeHQvMjAwOC0wMi0yOS8iIHhtbG5zOnhtcFJpZ2h0cz0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL3JpZ2h0cy8iIGRjOlJpZ2h0cz0iTGF1cmkgUGF0dGVyc29uIiBwaG90b3Nob3A6Q3JlZGl0PSJHZXR0eSBJbWFnZXMiIEdldHR5SW1hZ2VzR0lGVDpBc3NldElEPSIxNTc0ODM0MjUiIHhtcFJpZ2h0czpXZWJTdGF0ZW1lbnQ9Imh0dHBzOi8vd3d3LmdldHR5aW1hZ2VzLmNvbS9ldWxhP3V0bV9tZWRpdW09b3JnYW5pYyZhbXA7dXRtX3NvdXJjZT1nb29nbGUmYW1wO3V0bV9jYW1wYWlnbj1pcHRjdXJsIiBwbHVzOkRhdGFNaW5pbmc9Imh0dHA6Ly9ucy51c2VwbHVzLm9yZy9sZGYvdm9jYWIvRE1JLVBST0hJQklURUQtRVhDRVBUU0VBUkNIRU5HSU5FSU5ERVhJTkciID4KPGRjOmNyZWF0b3I+PHJkZjpTZXE+PHJkZjpsaT5MYXVyaVBhdHRlcnNvbjwvcmRmOmxpPjwvcmRmOlNlcT48L2RjOmNyZWF0b3I+PGRjOmRlc2NyaXB0aW9uPjxyZGY6QWx0PjxyZGY6bGkgeG1sOmxhbmc9IngtZGVmYXVsdCI+SG90IERvZyB3aXRoIEtldGNodXAsTXVzdGFyZCxSZWxpc2ggYW5kIE9uaW9ucyAtIFBob3RvZ3JhcGhlZCBvbiBIYXNzZWxibGFkIENhbWVyYSBTeXN0ZW08L3JkZjpsaT48L3JkZjpBbHQ+PC9kYzpkZXNjcmlwdGlvbj4KPHBsdXM6TGljZW5zb3I+PHJkZjpTZXE+PHJkZjpsaSByZGY6cGFyc2VUeXBlPSdSZXNvdXJjZSc+PHBsdXM6TGljZW5zb3JVUkw+aHR0cHM6Ly93d3cuZ2V0dHlpbWFnZXMuY29tL2RldGFpbC8xNTc0ODM0MjU/dXRtX21lZGl1bT1vcmdhbmljJmFtcDt1dG1fc291cmNlPWdvb2dsZSZhbXA7dXRtX2NhbXBhaWduPWlwdGN1cmw8L3BsdXM6TGljZW5zb3JVUkw+PC9yZGY6bGk+PC9yZGY6U2VxPjwvcGx1czpMaWNlbnNvcj4KCQk8L3JkZjpEZXNjcmlwdGlvbj4KCTwvcmRmOlJERj4KPC94OnhtcG1ldGE+Cjw/eHBhY2tldCBlbmQ9InciPz4K/9sAhAAJBgcIBwYJCAcICgoJCw0WDw0MDA0bFBUQFiAdIiIgHR8fJCg0LCQmMScfHy09LTE1Nzo6OiMrP0Q/OEM0OTo3AQoKCg0MDRoPDxo3JR8lNzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzf/wAARCACWAMgDASIAAhEBAxEB/8QAGwABAAMAAwEAAAAAAAAAAAAAAAQFBgECBwP/xAA5EAABBAECBAQEBAMIAwAAAAABAAIDBBEFIQYSMUETUWFxFCKBkQcyocFCUrEjQ2KC0eHw8SQlNf/EABkBAQADAQEAAAAAAAAAAAAAAAADBAUCAf/EACsRAAICAgECBAUFAQAAAAAAAAABAgMEESESMRNBYaEiUYGRwQUUcbHRMv/aAAwDAQACEQMRAD8A9xREQBERAEREAREQBERAEREAREQBERAEREAREQHGEwuUQHXC64X0XGEB0wuF3IRAdkREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAERdJZY4YnySuDWMGXOPYIDuiyOo/iFo1UPbW8a09vTlYWNcQdwC77qtrfibDdiZ8LQ/8AIaCZYpJcDA/lcAc/UBVpZdEe8iRVTfka7W9Wi0ys55I8XGWtKxVfjyZmpMjE4txvJHJyNZgef/CRuuus6hHqbfF1DHJKABG05DR5bdSqu1wBqErzqVaWs1zh8lZ+W4G/8Q79/osn91dk2y8J8Ltr8/MsKuEI/EaCfjW7VkDpI4nslfhjS0/LnYAYV2OI316gnuV+cBvM9sJHOwerSf3VLpvDdGhWZZlnls22AEc0vyNPo0bffKyepcVS8OcS6gx0DbUVhkZILvmY0A7D67rmnIyK8lVWz7rfuWKsWN6fQuUaYfi1ovxvhOqXPhubl+IAaR168oOcfr6L0CORksbZI3BzHAFrh0IXiurW4rT69uPSX0oZ48seWgCT1wOh3W1/DLVX2KljTZTn4c88R/wHqPof6rUpyZSs6JDLxK41Kyta1352bdERXTLCIiAIiIAiIgCIiAIiIAiLgkAZJwAgOUUCXWdNieGPuw8x6AOyT9lSahrfxlhlWBzvDLiZY2Hd7G7kbb74xhVLc2mvS3tvyRJGuTNBc1GnSc1tuzFC5wy0Pdgu9vNYvjPUYrkDvDOIg3c8xw7HTP3VJxBXN1hfLYkZNG3LGSZP/X2x6KvtyfDaZBYmd8QwNDTGT3Iz38uiw8r9Qlkx6I8Lf1LddKhyyv1me6YnSyUZcOHOJjGTzDzVlwXw9Y1CaexqUbmVzC012cnhguJORjrsAPuuOHa+r8WVzfF2Opp/OQPDBfJJynBGdgBt6q71zUJdKtaYytPg+Lh3OM87Q0/vjdU3a67o0SXL7+i/0s11+J27lXqFvQuF4IW3vFuWmuLmMcectwcjbYbbblW1DibU+IJRHX0i66l2leWxtO3rgn6ZWb1COnanms2qsJllkLs45sb7DJCsrnHU1HTo6tOuwzsYGmWR3ybd8Dc/cK1jYtK2pzl92t/RFyyjpgumKb9fI10VWV2mOfEYmhjf7OGNwxkdttl4ZqV517VZ7dyMsl8TDoid2YPT9P6rR8JWuJtU1iy6rA+eCWR0szmkRwtcT5/sMn0K3NPg/R6l+XU70LLV2VweWO3ijd35W9/c/orUMXHp+KC0/nvZzXa8ab29v0OJqUuuaDVr1hCyHkaY5JScAY6tx1VjwBw/Y0uzbs2nxl3L4TfDdkOzgk/oP1X1mskkk7eWFxomp+FqbWl2WSHlKlqyI+NHZTsjN1SSNki6te1wy0grstoyQiIgCIiAIiIAiIgCLpLI2JvM848vVUut6xYqxhtSNniHqZDsweqgvya6I7mzuFcp9ibq919WEiAsExGxeMgeuO6yPEnFdhsTYWRBrXBrXljxkuJx0649lT6jxpUiEp1m9HW8RpBJYXOwOzR9/wBVU6PG7iWw2zpBeGxZxPYYWB2fId/dYFuXkX2PW1W+Pl7+pchVGK57oz+o27HjzGSbw3NIIjkyHHJ7eyncDaTrdrXrGoOseBVdG6OSx1znHyjzOO/ZWuvcDatNPAZZopPFkbGTF1AJG/038/or/Wo2aJpVLSqTnRxhwh5v4sYJJ9zg/dV77ZUKNVaXXLj+C3GlT6ed7L6LQeHrsMMRbHM5jQHObO5rjt1IBCz7NU4dr8WDQRXhjjAH9q8Ajn/kyfTG6ztyrQlDj4IjkA2kYSHe+eqyt3SnROdIywZnl2cyOy4/VXZLHuhGM4LaLNOAoyfVN6fse0cS6zomjWKzLVjwy/rE3JGMdwOiwnFEWmz249doan4jccgr82QCe7fLYbrz+ybc0xdKTJK7A5nO5ifIeq3HB/4eajqIZa1kvo1TvyEYlkHoD+Uep39FIqK+pzhFLfsdeHXixTc+f7K0S29UstrUIJJ5nHaOMZ+vt6lbDQ/w8a1zbPEkzZCNxUhd8v8Amd39h9ytnpun0NFrfDaXWbBGfzEHLnnzJO5XM0nmd15qFfqyrZlWW8R4XudR4VeuyvUiZDDGMNZG0BrR6AKDLI0E5O65s2g1p3CprNsnYFVrLHJntVWuT727AA6qtbKY3l7dnZ2wuk02xJOcLtWLQ8OlHX9FZw6XOzfkjnJsVdevma3Q7c7wMkkeq0zDzNBKzmjTRFrQ3C0bPyjC3jFOyIiAIiIAiIgCIiArLQkkvOILeWJuwcO/UrDanca3xzZnia5z9y9/KB09tluNRf8ADTSyZa0SRHcjuNv3C88h0GF8pmvAWXhznAyDIaCc4x3x6rCzqXOet+ZrYlan37F1w/omi6rp7tUirVLFlrntjsGIPGQeo5hnCyU/4h6hRkNdzILToxyvMURjDXjq3BB6H2WmdxM/RaXw9Wp4vzEjlIGFh5nVLhns2qkUcs0jnlo7ZOUujjuuKS5RcxaUrJ+JHcfIuaH4otbIwXqLmNBySxoIH9CpXHT47zNM1ipZi+Gc4uMWd3EjZw+mfusDaqVnyhkDHlzzgMYScn0C0ug/h5rF/kfd/wDW1B3mHNIR12Z2+pHso6aK1FxhH7+RLdHHqkpxfT+SKyLUtS/+fVlmHTmY3bPudlb6R+Hur35efVnihW75IfI72A2HufsvS6jIKNeOGEc3I0N5sAZx7bBcvmLupKn6Kq/VlKebdPiK0it0nh3RdBDTQpsdO0YNiUB8p/zY29hgKwknHUlRZrLW5y5Vlq6P4SoZ3vyI41OT3IsZrTR3VbZtPJ+XH3UF9suOM9V8JZgG7lV22yzGtRObE5cSHZUKVwaCXOxhfKxfa04bu7oAOq6QwySu8Sf6N8lNRjytfAtujUuTvE0vIe/oPyj919ymw2Cl0ab7UoABwt2qqNcelGNba7JbZZ8PtfkdVta+fDGVW6VpwgYMjdWwGBgKUhOUREAREQBERAEREBnOPjLHw9LZgaXPhcD8vXB2/wBF5s3W5mQtj5ySRlxPc/7L2ixDHYgkgmaHRyNLXNPcHqvKNf4OtabYkkZI19ZziWOGM48j3ys7Mok5dcTWwMmEYOuRmbWocwJydupJ6Kx0DhHU9fIs2C6nRO4le35pB/hb+5291O4Y4bit6t42oNa+rXHOIS4EyOztkfy+efRbu1bcMknGe2VT8NQXVItW5Tb6K/ufHRNC0jQY2/BVw6YDBsS4dIfr29hgKfNZ5j1291RzXyM/MosmonsVFK9vhECobfVJ8l660xud1Cmv9eX9FSPtvcd3L5vsEDrnPqoepvuTKpInWLfMcn7KHLKO5UOe21g+YjCgPsz2X8sGzf5yvYVym9RR23GC22TLF1kWS4/RRPEs3DhoLGeZ6r7QUWt+aQlzu5KmNaGjAC06cBLmZQtzX2gfCtTjh+YjLu5PVSfQKXU0+xbcORuG+ZWl0zh2OPD5BzO8ytGMFFaRnym5PbKDTtJmtOBc0hvqtlpmlx1mDbdToK0cIAa0L7Ls4OAABgLlEQBERAEREAREQBERAFV69px1Crhv527hWiIDzivA/TNRL5xyB7DGXdhnGP6KTaJwd1ccSQ8zXYZkrDT3LlQlrW88Y/gd29iqOTjOfMS5Reov4iVNnJ3Ucuwf9VXTaw9/9w4H3UR1m3Mflby+6z/2lu/+TQWRVruW8lhrNyQoUuo8zzHDl7j2CjMoyTEGeRxHkNlY1qsUDcMaB7Kev9Pk+ZshszoriC2fGGo+V3POcnyHQKwjY1g2CNBJAAyfIK207RJ7TgXtLW/qtKuqNa1FGfO2U3uTK+Jj5XcsbS4+i0Gk8PvkcHzj6K+03RYazR8oVuxjWDDQpNETZGqUYq7QA0bKX0RF6eBERAEREAREQBERAEREAREQBERAfKevHOMPGVT3uHYJweVoyr1EB5vqXCr4yTG1UrqEsLuV0RBHovYHMa4YcAVGk0+tIcujGUB5bFUsSHDIXH6K1pcO2pyDJ8g9Oq30dCuz8rApDY2M/K0BAUGmcOw1wCWjPmVeQwRxDDWhfVEAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQH//2Q=="



@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    bot.send_message(user_id,"Добро пожаловать в бот донеров")
    checker = db.check_user(user_id)
    if checker == True:
        bot.send_message(user_id, "Главное меню: ", reply_markup=bt.main_menu_kb())
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
        bot.send_message(user_id, "Главное меню: ", reply_markup=bt.main_menu_kb())
    else:
            bot.send_message(user_id, "Sneeeeed your location")
            bot.register_next_step_handler(message, get_location, name , phone_number)
@bot.callback_query_handler(lambda call: call.data in ["cart", "back"])
def all_cals(call):
   user_id = call.message.chat.id
   if call.data == "cart":
       bot.send_message(user_id, "Ваша корзина: ")
   elif call.data == "back":
       bot.delete_message(user_id, call.message.message_id)
       bot.send_message(user_id, "Главное меню: ", reply_markup=bt.main_menu_kb())


@bot.message_handler(content_types=["text"])
def main_menu(message):
    user_id = message.from_user.id
    if message.text == "🍴Меню":
        all_products = db.get_cart_id_name()
        bot.send_message(user_id, "Выберите продукт: ", reply_markup=bt.products_in( all_products))
    elif message.text == "🛒Корзина":
        bot.send_message( user_id , "Ваша корзина: ")
    elif message.text == "✒️Отзыв":
        bot.send_message( user_id, "Ваш отзав? ")



bot.infinity_polling()
