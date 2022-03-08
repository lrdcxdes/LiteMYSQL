# LiteMYSQL 
База данных? Без проблем!

# КРАТКАЯ ДОКУМЕНТАЦИЯ
Привет! Эта библиотека создана для простого и быстрого создания и редактирования базы данных формата MYSQL.
 Библиотека основана на pymysql, aiomysql

Pypi - https://pypi.org/project/LMSQL
ReadTheDocs - 

## Импорты
Рекомендуем использовать from Lite_MYSQL import lmysql или же from Lite_MYSQL import aiolmysql (они будут рассмотрены тут), но есть и другие варианты импорта.

# Примеры
```python
from LMSQL import lmysql
sql = lmysql() #Соединяемся с БД 
sql.create('id, hash') #Создаем 2 столбца - id и hash
sql.insert_data((1, 'lord'), 'id, name') #Добавляем данные
a = sql.select_data(1, 'id') #Ищем строку, в которой id = '234'
print(a) #Результат - [{'id':1, name:'lord'}]
sql.edit_data('id', 1, 'name', 'genius') #Изменяем данные - там, где id = 234, теперь hash = 1234
a = sql.select_data(1, 'id') #Ищем строку, в которой id = 1
print(a) #Результат - [{'id':1, name:'genius'}]
b = sql.search('name', 'dima123') #Поиск строк 
print(b) #Результат - [{'id':2, 'name':'dima123')]
a = sql.select_data_with_sort('rowid', None, 'id') #Сортировка строк по возрастанию данных в id
print(a) #Результат - [{'id':1, 'name':'lord'}, {'id':2, 'name':'dima'}]
a = sql.get_all_data() #Вернем всю таблицу?
print(a) #Результат - [{'id':1, 'name':'lord'}, {'id':2, 'name':'dima'}]
```

```python
from LMSQL import aiolmysql
import asyncio

async def main():
    sql = aiolmysql() #Соединяемся с БД
    await sql.connect() #Соединяемся с БД
    await sql.create('id, hash') #Создаем 2 столбца - id и hash
    await sql.insert_data((1, 'lord'), 'id, name') #Добавляем данные
    a = await sql.select_data(1, 'id') #Ищем строку, в которой id = '234'
    print(a) #Результат - [{'id':1, name:'lord'}]
    await sql.edit_data('id', 1, 'name', 'genius') #Изменяем данные - там, где id = 234, теперь hash = 1234
    a = await sql.select_data(1, 'id') #Ищем строку, в которой id = 1
    print(a) #Результат - [{'id':1, name:'genius'}]
    b = await sql.search('name', 'dima123') #Поиск строк 
    print(b) #Результат - [{'id':2, 'name':'dima123')]
    a = await sql.select_data_with_sort('rowid', None, 'id') #Сортировка строк по возрастанию данных в id
    print(a) #Результат - [{'id':1, 'name':'lord'}, {'id':2, 'name':'dima'}]
    a = await sql.get_all_data() #Вернем всю таблицу?
    print(a) #Результат - [{'id':1, 'name':'lord'}, {'id':2, 'name':'dima'}]

asyncio.run(main())
```

# Контакты

Что-то не работает, есть вопросы, пожелания? Пиши - t.me/lord_codes


# Удачи!
