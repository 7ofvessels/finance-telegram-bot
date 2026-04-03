from bot.db.session import SessionLocal
from bot.db.models import Expense


def add_expense(user_id: int, amount: float, category: str, comment: str = None):
    session = SessionLocal()


    expense = Expense(
        user_id=user_id,
        amount=amount,
        category=category,
        comment=comment
    )

    session.add(expense)
    session.commit()
    session.close()

def get_expenses_by_user(user_id: int):
    session = SessionLocal()

    expenses = session.query(Expense).filter(Expense.user_id == user_id).all()

    session.close()
    return expenses
