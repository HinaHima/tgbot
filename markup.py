from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

#Главное меню
btnObito = KeyboardButton('Obito Uchiha')
mainMenu = ReplyKeyboardMarkup(resize_keyboard= True).add(btnObito)