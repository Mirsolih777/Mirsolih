from aiogram.types import KeyboardButton,ReplyKeyboardMarkup



# Languages buttons
uzbek = KeyboardButton(text="O'zbek tili🇺🇿")
russian = KeyboardButton(text="Rus tili🇷🇺")
english = KeyboardButton(text="Ingliz tili🇺🇸")


# Main page buttons
info = KeyboardButton(text="Ma'lumot")
contact = KeyboardButton(text="Telefon raqamni yuborish", request_contact=True)
location = KeyboardButton(text="Lokatsiya yuborish", request_location=True)
kurslar = KeyboardButton(text="Kurslar")



ingiliz_tili = KeyboardButton(text="ingiliz tili")
rus_tili = KeyboardButton(text="rus tili")



natija = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(uzbek,russian).add(english)
# natija = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(uzbek,russian,english)
natija2 = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(info).add(contact).add(location).add(kurslar)

natija3 = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(ingiliz_tili).add(rus_tili)