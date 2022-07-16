import sqlite3

#Подключение к базе данных
db = sqlite3.connect('series.db')
#Курсор, позволяющий работать с бд
cursor = db.cursor()

#Создаем таблицу в бд, если таковой не имеется
cursor.execute("""CREATE TABLE IF NOT EXISTS characters(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)""")

#Создаем таблицу в бд, если таковой не имеется
cursor.execute("""CREATE TABLE IF NOT EXISTS series(
    id INTEGER,
    number INTEGER,
    FOREIGN KEY (id) REFERENCES characters(id)
)""")


###cursor.execute("SELECT * FROM series")
###print(cursor.fetchall())

#Создаем таблицу в бд, если таковой не имеется
#cursor.execute("""CREATE TABLE IF NOT EXISTS charser(
    #characterId INTEGER NOT NULL,
    #seriesId INTEGER NOT NULL,
    #FOREIGN KEY (characterId) REFERENCES characters(id),
    #FOREIGN KEY (seriesId) REFERENCES series(id)
#)""")

db.commit()