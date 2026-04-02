import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command

from bot.config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message):
    await message.answer(
        "Привет! 👋\n\n"
        "Я бот для учёта личных расходов.\n\n"
        "Команды:\n"
        "/add сумма категория комментарий\n"
        "/stats — статистика за месяц"
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())