import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5702323388:AAEUAHBVYF1oN9Gma-fwLDpV24XnMgjrv8U'
logging.basicConfig(level=logging.INFO)  # Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я могу генерировать тексты по заданным вами параметрам")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
