# =============================================================================
# Придумал и разработал - lordcodes (vk.com/rezy0, t.me/lord_codes)
# Гитхаб - https://github.com/LORD-ME-CODE/LiteMYSQL
# PypI - pypi.org/project/lite-mysql/
# =============================================================================

import pymysql
from pymysql.cursors import DictCursor
import aiomysql


class lmysql():
    def __init__(self, host='localhost', user='root', password='', db='', port=3306):
        self.conn = pymysql.connect(
                            host=host,
                            user=user,
                            password=password,
                            db=db,
                            port=port,
                            cursorclass=DictCursor
                    )
        self.cursor = self.conn.cursor()

    def create(self, names, table="albums"):
        self.cursor.execute(f"CREATE TABLE {table} ({names})")
        self.conn.commit()
    
    def insert_data(self, data_mass, table_rows, table="albums"): 
        len_title = r"%s,"*(len(table_rows.split(', '))-1) + r"%s"
        self.cursor.executemany(f"INSERT INTO {table} ({table_rows}) VALUES ({len_title})", data_mass)
        self.conn.commit()
        
    def edit_data(self, title_last, last, title_new, new, table="albums"):
        self.cursor.execute(f"""UPDATE `{table}`
SET {title_new} = %s WHERE {title_last} = %s""",
                            [new, last])
        self.conn.commit()
        
    def delete_data(self, name, title_name, table="albums"):
        self.cursor.execute(f"DELETE FROM `{table}` WHERE {title_name} = %s", [name])
        
    def select_data(self, name, title, row_factor=False, table="albums"):
        self.cursor.execute(f"SELECT * FROM {table} WHERE {title}=?", [name])
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
        return self.cursor.fetchall()
    
    def get_all_data(self, table="albums"):
        self.cursor.execute(f"SELECT * FROM `{table}`")
        return self.cursor.fetchall()
    
    def get_cursor(self):
        return self.cursor
    
    def get_connect(self):
        return self.conn


class aiolmysql():
    async def __init__(self, host='localhost', port=3306, user='root', password='', db=''):
        self.conn = await aiomysql.connect(host=host,
                                        port=port,
                                        user=user,
                                        password=password,
                                        db=db)
        self.cursor = await self.conn.cursor()
    
    async def create(self, names, table="albums"):
        await self.cursor.execute(f"CREATE TABLE {table} ({names})")
        await self.conn.commit()
    
    async def insert_data(self, data_mass, table_rows, table="albums"): 
        len_title = r"%s,"*(len(table_rows.split(', '))-1) + r"%s"
        await self.cursor.executemany(f"INSERT INTO {table} ({table_rows}) VALUES ({len_title})", data_mass)
        await self.conn.commit()
        
    async def edit_data(self, title_last, last, title_new, new, table="albums"):
        await self.cursor.execute(f"""UPDATE `{table}`
SET {title_new} = %s WHERE {title_last} = %s""",
                            [new, last])
        await self.conn.commit()
        
    async def delete_data(self, name, title_name, table="albums"):
        await self.cursor.execute(f"DELETE FROM `{table}` WHERE {title_name} = %s", [name])
        
    async def select_data(self, name, title, row_factor=False, table="albums"):
        await self.cursor.execute(f"SELECT * FROM {table} WHERE {title}=?", [name])
        if row_factor:
            return await self.cursor.fetchone()
        else:
            return await self.cursor.fetchall()
        
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
        return await self.cursor.fetchall()
    
    async def get_all_data(self, table="albums"):
        await self.cursor.execute(f"SELECT * FROM `{table}`")
        return await self.cursor.fetchall()
    
    async def get_cursor(self):
        return self.cursor
    
    async def get_connect(self):
        return self.conn
