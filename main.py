# kerakli modullarni chaqirib olamiz
from aiogram import Bot,Dispatcher,executor,types
from config import API_TOKEN
import logging
from tugmalar import natija, natija2



# Logging qismi
logging.basicConfig(level=logging.INFO)

# Botni ulash qismi
bot=Bot(token=API_TOKEN)
dp=Dispatcher(bot)

# Start command
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    ism = message.from_user.first_name
    await message.answer(f"Assalomu aleykum {ism}. Botimizga xush kelibsiz.",reply_markup=natija)

@dp.message_handler()
async def buttons(message: types.Message):
    if message.text == "O'zbek tili🇺🇿":
        await message.answer("Siz o'zbek tilini tanladingiz.",reply_markup=natija2)
    elif message.text == "Rus tili🇷🇺":
        await message.answer("Вы выбрали русский")
    elif message.text == "Ingliz tili🇺🇸":
        await message.answer("You have selected English")
    elif message.text == "telefon raqam":
        await message.answer_contact(phone_number="99 848 70 07",first_name="Mirsolih")
        await message.answer("Siz bilan bog'lanamiz")
    elif message.text == "Joylashuv":
        await message.answer_location(41.334896756804774, 69.21547319114438)
        await message.answer("<b>Bizning manzil</b>: Beruniy ko'chasi 35A.\n<b>Mo'ljal</b>: Bursa restorani yonida", parse_mode="HTML")



# Start the bot
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)


