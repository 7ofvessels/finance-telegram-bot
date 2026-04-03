from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from bot.services.expense_service import add_expense

router = Router()


@router.message(Command("add"))
async def add_expense_handler(message: Message):
    try:
        parts = message.text.split(maxsplit=3)

        if len(parts) < 3:
            await message.answer(
                "Использование:\n"
                "/add сумма категория комментарий"
            )
            return

        _, amount, category = parts[:3]
        comment = parts[3] if len(parts) == 4 else None

        amount = float(amount)

        add_expense(
            user_id=message.from_user.id,
            amount=amount,
            category=category,
            comment=comment
        )

        await message.answer(
            f"✅ Расход добавлен:\n"
            f"{amount} — {category}"
        )

    except ValueError:
        await message.answer("❌ Неверный формат суммы. Пример: /add 500 еда обед")
    except Exception as e:
        await message.answer(f"❌ Ошибка: {str(e)}")