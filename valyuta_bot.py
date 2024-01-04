import logging


from aiogram import Bot, Dispatcher, executor, types

import valyuta

API_TOKEN = ''

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start", "help"])
async def welcome_bot(message: types.Message):
    await message.reply(f"Assalom alaykum {message.from_user.full_name}.\nBotimizga xush kelibsiz!")
    await message.answer(f"Hozir {valyuta.sana} sana bilan dollar kursi {valyuta.kurs} so'mga teng.")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)