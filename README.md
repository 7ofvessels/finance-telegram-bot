Telegram Bot для учёта личных финансов



Telegram-бот для учёта расходов с сохранением данных в базе и просмотром статистики.



Возможности



- Добавление расходов через Telegram-команды

- Хранение данных в базе данных (SQLite + SQLAlchemy)

- Просмотр статистики расходов

- Агрегация данных по категориям

- Использование pandas для обработки данных





Стек технологий



- Python 3.10+

- aiogram 3.x

- SQLAlchemy

- SQLite

- pandas





Установка и запуск



1. Клонирование репозитория


```
git clone <your-repo-url>

cd finance-telegram-bot
```




2. Создание виртуального окружения

```
bash

python -m venv venv
```


3. Активация окружения



Windows:


```
venv\\Scripts\\activate
```


Mac/Linux:


```
source venv/bin/activate
```


4. Установка зависимостей

```
pip install -r requirements.txt
```


Настройка


Создайте файл .env:

```
BOT_TOKEN=your_telegram_bot_token
```


Инициализация базы данных

```
python -m bot.db.init_db
```


Запуск бота

```
python -m bot.main
```


Команды бота



+ Добавить расход



/add <сумма> <категория> <комментарий>



Пример:



add 500 еда обед





+-= Статистика



/stats



Показывает:



* Общую сумму расходов

* Расходы по категориям






Архитектура проекта



bot

├── handlers/        # Обработчики команд Telegram

├── services/        # Бизнес-логика

├── db/              # Работа с базой данных

├── config.py        # Конфигурация

├── main.py          # Точка входа






Планы развития



* Фильтрация по датам (/stats week/month)

* Экспорт данных в CSV

* Категории через inline-кнопки

* Docker-развертывание





🦊 Автор



[7ofvessels]

GitHub: <github.com/7ofvessels>

