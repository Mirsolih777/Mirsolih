
from aiogram import Bot,Dispatcher,executor,types
from config import API_TOKEN
import logging
from tugmalar import natija,natija2



logging.basicConfig(level=logging.INFO)


bot=Bot(token=API_TOKEN)
dp=Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    ism = message.from_user.first_name
    await message.answer(f"Assalomu aleykum {ism}. Botimizga xush kelibsiz.",reply_markup=natija)


@dp.message_handler()
async def buttons(message: types.Message):
    if message.text == "O'zbek tili🇺🇿":
        await message.answer("Siz o'zbek tilini tanladingiz.",reply_markup=natija2)
    elif message.text == "Rus tili🇷🇺":
        await message.answer("Вы выбрали русский",reply_markup=natija2)
    elif message.text == "Ingliz tili🇺🇸":
        await message.answer("You have selected English",reply_markup=natija2)

    


# Start the bot
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
