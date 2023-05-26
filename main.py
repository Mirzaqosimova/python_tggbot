import logging
from aiogram import Bot, Dispatcher, executor, types
from config.database import database

API_TOKEN = "5005447561:AAHT37FFhrjtQ41n8YbkRMxxRcfBczvsecI"
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

async def on_startup(dispatcher):
    await database.connect()


async def on_shutdown(dispatcher):
    await database.disconnect()

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram. Send me your contact")


@dp.message_handler()
async def echo(message: types.Message):
    print(message.text)
    await bot.send_photo(chat_id=message.chat.id, photo=message.text)

if __name__ == '__main__':
     executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)