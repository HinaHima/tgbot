import sqlite3

#Подключение к базе данных
db = sqlite3.connect('series.db')
#Курсор, позволяющий работать с бд
cursor = db.cursor()

#cursor.execute("""SELECT number FROM series WHERE id == """)
#print(cursor.fetchall())

#cursor.execute("SELECT * FROM charser")
#print(cursor.fetchall())

#cursor.execute("DROP TABLE series")

#cursor.execute("""SELECT number FROM series WHERE id == 1""")
#print(cursor.fetchall())

#cursor.execute("DROP TABLE charser")

#db.commit()

##print(cursor.fetchall())

#cursor.execute("""INSERT INTO characters VALUES (2, 'Itachi Uchiha')""")

#cursor.execute("""INSERT INTO series VALUES""")

