import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command

from bot.config import BOT_TOKEN
from bot.handlers.add_expense import router as add_router
from bot.handlers.stats import router as stats_router

bot = Bot(token="...")
dp = Dispatcher()
dp.include_router(stats_router)

dp.include_router(add_router)


@dp.message(Command("start"))
async def start_handler(message):
    await message.answer(
        "Привет! 👋\n\n"
        "Я бот для учёта расходов.\n\n"
        "Добавить расход:\n"
        "/add 500 еда обед"
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())