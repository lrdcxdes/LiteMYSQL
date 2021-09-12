# =============================================================================
# Придумал и разработал - lordcodes (vk.com/rezy0, t.me/lord_codes)
# Гитхаб - https://github.com/LORD-ME-CODE/LiteMYSQL
# PypI - pypi.org/project/lite-mysql/
# =============================================================================

import pymysql
from pymysql.cursors import DictCursor
import aiomysql
import logging

def send_print(text):
    logging.info(text)

class lmysql():
    def __init__(self, host='localhost', user='root', password='', db='', port=3306, log=True):
        self.conn = pymysql.connect(
                            host=host,
                            user=user,
                            password=password,
                            db=db,
                            port=port,
                            cursorclass=DictCursor
                    )
        self.cursor = self.conn.cursor()
        self.log = log
        if self.log:
            send_print('Соединение с базой данных установлено, курсор подключён.')

    def create(self, names, table="albums"):
        self.cursor.execute(f"CREATE TABLE {table} ({names})")
        self.conn.commit()
        if self.log:
            send_print(f'Таблица {table} была успешно создана.')
        
    
    def insert_data(self, data_mass, table_rows, table="albums"): 
        len_title = r"%s,"*(len(table_rows.split(', '))-1) + r"%s"
        self.cursor.executemany(f"INSERT INTO {table} ({table_rows}) VALUES ({len_title})", data_mass)
        self.conn.commit()
        if self.log:
            send_print(f'В таблицу {table} вставлен новый столбец со значениями: {data_mass}')

        
    def edit_data(self, title_last, last, title_new, new, table="albums"):
        self.cursor.execute(f"""UPDATE `{table}`
SET {title_new} = %s WHERE {title_last} = %s""",
                            [new, last])
        self.conn.commit()
        if self.log:
            send_print(f'В таблице {table} изменено значение {title_new} = {new} , где {title_last} = {last}')
        
    def delete_data(self, name, title_name, table="albums"):
        self.cursor.execute(f"DELETE FROM `{table}` WHERE {title_name} = %s", [name])
        self.conn.commit()
        if self.log:
            send_print(f'В таблице {table} удалено значение , где {title_name} = {name}')
        
    def select_data(self, name, title, row_factor=False, table="albums"):
        self.cursor.execute(f"SELECT * FROM `{table}` WHERE {title} = %s", [name])
        if self.log:
            send_print(f'Взят столбец из таблицы {table} где {title} = {name}')
        if row_factor:
            return self.cursor.fetchone()
        else:
            return self.cursor.fetchall()
        
    def select_data_with_sort(self, type_sort, name, title_name, table="albums"):
        a = []
        if name != None:
            for row in self.cursor.execute(f"SELECT {type_sort}, * FROM `{table}` ORDER BY {title_name}", [name]):
                a.append(row)
            return a
        else:
            for row in self.cursor.execute(f"SELECT {type_sort}, * FROM `{table}` ORDER BY {title_name}"):
                a.append(row)
            return a
        
    def search(self, type_search, name_search, table="albums"):
        self.cursor.execute(f"SELECT * FROM `{table}` WHERE {type_search} LIKE {name_search}")
        if self.log:
            send_print(f'Взят столбец из таблицы {table} где {type_search} LIKE {name_search}')
        return self.cursor.fetchall()
    
    def get_all_data(self, table="albums"):
        self.cursor.execute(f"SELECT * FROM `{table}`")
        if self.log:
            send_print(f'Взяты все столбцы из таблицы {table}')
        return self.cursor.fetchall()
    
    def get_cursor(self):
        if self.log:
            send_print(f'Получен курсор')
        return self.cursor
    
    def get_connect(self):
        if self.log:
            send_print(f'Получено соединение')
        return self.conn


class aiolmysql():
    def __init__(self, host='localhost', port=3306, user='root', password='', db='', log=True):
        self.settings = [host, port, user, password, db, log]

    async def connect(self):
        self.conn = await aiomysql.connect(host=self.settings[0],
                                        port=self.settings[1],
                                        user=self.settings[2],
                                        password=self.settings[3],
                                        db=self.settings[4])
        self.cursor = await self.conn.cursor()
        self.log = self.settings[5]
        if self.log:
            send_print('Соединение с базой данных установлено, курсор подключён.')

    async def create(self, names, table="albums"):
        await self.cursor.execute(f"CREATE TABLE {table} ({names})")
        await self.conn.commit()
        if self.log:
            send_print(f'Таблица {table} была успешно создана.')
        
    
    async def insert_data(self, data_mass, table_rows, table="albums"): 
        len_title = r"%s,"*(len(table_rows.split(', '))-1) + r"%s"
        await self.cursor.executemany(f"INSERT INTO `{table}` ({table_rows}) VALUES ({len_title})", data_mass)
        await self.conn.commit()
        if self.log:
            send_print(f'В таблицу {table} вставлен новый столбец со значениями: {data_mass}')

        
    async def edit_data(self, title_last, last, title_new, new, table="albums"):
        await self.cursor.execute(f"""UPDATE `{table}`
SET {title_new} = %s WHERE {title_last} = %s""",
                            [new, last])
        await self.conn.commit()
        if self.log:
            send_print(f'В таблице {table} изменено значение {title_new} = {new} , где {title_last} = {last}')
        
    async def delete_data(self, name, title_name, table="albums"):
        await self.cursor.execute(f"DELETE FROM `{table}` WHERE {title_name} = %s", [name])
        await self.conn.commit()
        if self.log:
            send_print(f'В таблице {table} удалено значение , где {title_name} = {name}')
        
    async def select_data(self, name, title, row_factor=False, table="albums"):
        await self.cursor.execute(f"SELECT * FROM `{table}` WHERE {title} = %s", [name])
        if self.log:
            send_print(f'Взят столбец из таблицы {table} где {title} = {name}')
        if row_factor:
            return self.cursor.fetchone()
        else:
            return self.cursor.fetchall()
        
    async def select_data_with_sort(self, type_sort, name, title_name, table="albums"):
        a = []
        if name != None:
            for row in (await self.cursor.execute(f"SELECT {type_sort}, * FROM `{table}` ORDER BY {title_name}", [name])):
                a.append(row)
            return a
        else:
            for row in (await self.cursor.execute(f"SELECT {type_sort}, * FROM `{table}` ORDER BY {title_name}")):
                a.append(row)
            return a
        
    async def search(self, type_search, name_search, table="albums"):
        await self.cursor.execute(f"SELECT * FROM `{table}` WHERE {type_search} LIKE {name_search}")
        if self.log:
            send_print(f'Взят столбец из таблицы {table} где {type_search} LIKE {name_search}')
        return await self.cursor.fetchall()
    
    async def get_all_data(self, table="albums"):
        await self.cursor.execute(f"SELECT * FROM `{table}`")
        if self.log:
            send_print(f'Взяты все столбцы из таблицы {table}')
        return await self.cursor.fetchall()
    
    async def get_cursor(self):
        if self.log:
            send_print(f'Получен курсор')
        return self.cursor
    
    def get_connect(self):
        if self.log:
            send_print(f'Получено соединение')
        return self.conn
