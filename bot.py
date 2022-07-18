import config
import logging
import markup
import sqlite3

from aiogram import Bot, Dispatcher, executor, types

#Подключение к базе данных
db = sqlite3.connect('series.db')
#Курсор, позволяющий работать с бд
cursor = db.cursor()

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await bot.send_message(message.from_user.id, f"Hello, {message.from_user.first_name} Dattebayo!\n Сhoose the character you would like to watch series with.", reply_markup = markup.mainMenu)

@dp.message_handler()
async def send_welcome(message: types.Message):
    if message.text == "Obito Uchiha":
        cursor.execute("""SELECT number FROM series WHERE id == 1""")
        list = []
        while True:
            results = cursor.fetchone()

            if results == None:
                break

            list.append(results[0])

        await bot.send_message (message.from_user.id, f"{list}")

    elif message.text == "Itachi Uchiha":
        cursor.execute("""SELECT number FROM series WHERE id == 2""")
        list = []
        while True:
            results = cursor.fetchone()

            if results == None:
                break

            list.append(results[0])

        await bot.send_message(message.from_user.id, f"{list}")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)