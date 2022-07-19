from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

#Главное меню
btnObito = KeyboardButton('Obito Uchiha')
btnItachi = KeyboardButton('Itachi Uchiha')
mainMenu = ReplyKeyboardMarkup(resize_keyboard= True, one_time_keyboard= True).add(btnObito, btnItachi)