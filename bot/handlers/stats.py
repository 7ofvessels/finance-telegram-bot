from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

import pandas as pd

from bot.services.expense_service import get_expenses_by_user

router = Router()


@router.message(Command("stats"))
async def stats_handler(message: Message):
    expenses = get_expenses_by_user(message.from_user.id)

    if not expenses:
        await message.answer("Нет данных 📭")
        return

    # превращаем в DataFrame
    data = [
        {
            "amount": e.amount,
            "category": e.category,
            "date": e.created_at
        }
        for e in expenses
    ]

    df = pd.DataFrame(data)

    total = df["amount"].sum()

    by_category = df.groupby("category")["amount"].sum()

    response = f"📊 Статистика:\n\nОбщие расходы: {total}\n\nПо категориям:\n"

    for category, amount in by_category.items():
        response += f"{category}: {amount}\n"

    await message.answer(response)