from aiogram.types import KeyboardButton,ReplyKeyboardMarkup,InlineKeyboardButton,InlineKeyboardMarkup



# # Languages buttons
# uzbek = KeyboardButton(text="O'zbek tili🇺🇿")
# russian = KeyboardButton(text="Rus tili🇷🇺")
# english = KeyboardButton(text="Ingliz tili🇺🇸")


# ichki tugma
uz = InlineKeyboardButton(text="O'zbek tili🇺🇿",callback_data="🇺🇿")
ru = InlineKeyboardButton(text="rus tili🇷🇺",callback_data="🇷🇺")
us = InlineKeyboardButton(text="ingiliz tili🇺🇸",callback_data="🇺🇸")
site = InlineKeyboardButton(text="Saytga kirish", url="https://t.me/marsit_bot")
sin = InlineKeyboardButton(text="Botni boshqalarga yuborish", switch_inline_query ="")
sin2 = InlineKeyboardButton(text="Hozirgi chatga abar yuborish", switch_inline_query_current_chat = "Salom")
natija = InlineKeyboardMarkup().add(uz,ru,us).add(site).add(sin).add(sin2)

# Main page buttons
info = KeyboardButton(text="Ma'lumot")
contact = KeyboardButton(text="Telefon raqamni yuborish", request_contact=True)
location = KeyboardButton(text="Lokatsiya yuborish", request_location=True)
kurslar = KeyboardButton(text="Kurslar")
telefon_raqam = KeyboardButton(text="telefon raqam")
joylashuv = KeyboardButton(text="joylashuv")





# natija = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(uzbek,russian).add(english)
# natija = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(uzbek,russian,english)
natija2 = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(info).row(contact,location).add(kurslar).add(telefon_raqam,joylashuv)
