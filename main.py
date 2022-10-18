from aiogram import Bot, Dispatcher, executor, types
import os

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def _start(message: types.Message):
    await message.answer("Assalomu alaykum!")

executor.start_polling(dp, skip_updates=True)

