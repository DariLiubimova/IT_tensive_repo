'''
Соберите данные о моделях холодильников Саратов с маркетплейса beru.ru: URL, название, цена, размеры, общий объем, объем холодильной камеры.
Создайте соответствующие таблицы в SQLite базе данных и загрузите полученные данные в таблицу beru_goods.
Для парсинга можно использовать зеркало страницы beru.ru с результатами для холодильников Саратов по адресу:
video.ittensive.com/data/018-python-advanced/beru.ru/
'''
import sqlite3
import numpy as np
import pandas as pd
conn=sqlite3.connect('E:\Dari\ITtensive\БД\sqllite') #соединение
db=conn.cursor() #создание объекта для работы с бд
#запрос:
'''db.execute("""CREATE TABLE films
            (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            url text,
            title text default '',
            budget INTEGER default 0,
            sales_www INTEGER default 0)""")
conn.commit() #чтобы выполнить запрос'''
'''db.execute("""CREATE TABLE sample
            (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            name text)""")'''
conn.commit() #чтобы выполнить запрос
names=np.loadtxt('names.txt', dtype='str')
for name in names:
    db.execute('INSERT INTO sample (name) VALUES (?)', (name,))
conn.commit()
data=np.array(db.execute('SELECT * FROM sample').fetchall())
print(data)
data=pd.read_sql_query('SELECT * FROM sample', conn)
print(data)