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
    await bot.send_message(message.from_user.id, f"Hello, {message.from_user.first_name} Dattebayo!\n Сhoose the character you would like to watch series with.", reply_markup=markup.mainMenu)

@dp.message_handler()
async def send_welcome(message: types.Message):
    if message.text == "Obito Uchiha":
        picture = types.InputFile('media/picture/obito.jpg')
        cursor.execute("""SELECT number FROM series WHERE id == 1""")
        list = []
        while True:
            results = cursor.fetchone()

            if results == None:
                break

            list.append(results[0])

        await bot.send_photo(message.from_user.id, photo=picture)
        await bot.send_message (message.from_user.id, f"{list}")
        await bot.send_message(message.from_user.id, "Do you want to choose another variant? Type 'yes' or 'no'.")

    elif message.text == "Itachi Uchiha":
        picture = types.InputFile('media/picture/itachi.jpg')
        cursor.execute("""SELECT number FROM series WHERE id == 2""")
        list = []
        while True:
            results = cursor.fetchone()

            if results == None:
                break

            list.append(results[0])

        await bot.send_photo(message.from_user.id, photo=picture)
        await bot.send_message(message.from_user.id, f"{list}")
        await bot.send_message(message.from_user.id, "Do you want to choose another variant? Type 'yes' or 'no'.")

    elif message.text == 'yes':
        await bot.send_message(message.from_user.id, "Here are the menu!", reply_markup=markup.mainMenu)

    elif message.text == 'no':
        await bot.send_message(message.from_user.id, "Enjoy watching the series!")

    else:
        await  bot.send_message(message.from_user.id, "I don't know this command :(. I'll call the menu so you can choose any available option.", reply_markup = markup.mainMenu)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)