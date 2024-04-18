import json
import sqlalchemy, psycopg2

from sqlalchemy import (
    select,
    insert,
    update,
    delete,
    create_engine,
    inspect
    )

with open("access.json") as file: 
    access = json.load(file)
ip = access["ip"]
port = access["port"]
username = access['username']
password = access['password']
hostname = access['hostname']

class DataBase():
    def __init__(self, ip, port,  username, password, hostname):
        self.ip = ip
        self.port = port
        self.username = username
        self.password = password
        self.hostname = hostname
        
    
    async def connection(self):
        try:
            print(f"{ip} \n {username}, {password}, {hostname}")
            connection = psycopg2.connect(
                dbname = hostname,
                user= username,
                password= password,
                host= ip)
            engine = create_engine(
                f'postgresql+psycopg2://{self.username}:{self.password}@{self.ip}:{self.port}/{self.hostname}')
            insp = inspect(engine)
            print(insp.get_table_names())
            print("Connect to the database")
            connection.close()
        except Exception as e:
            print(f"Can't establish connection to database, please try again, or fix the bug syka \n {e}")
            
            
    async def fetch_customer(self):
        connection = psycopg2.connect(
                dbname = hostname,
                user= username,
                password= password,
                host= ip)
        with connection.cursor() as cursor:
            cursor.execute("Select * from customer")
            all_customers = cursor.fetchall()
            return all_customers
            
            
    async def add_customer(self, name, surname, phone, carid):
        connection = psycopg2.connect(
                dbname = hostname,
                user= username,
                password= password,
                host= ip)
        with connection.cursor() as cursor:
            cursor.execute(f'''INSERT INTO customer (name, surname, phone_humber, car_id)
                        VALUES (%s, %s, %s, %s);''',
                       (name, surname, phone, carid))
        connection.commit()
        '''здесь надо написать функции поиска по полям id и имени в таблице customer
            далее дописать вызов второго модального окна и второй функции на сам апдейт'''
    async def update_search(self, id, name): #доделать завтра
        connection = psycopg2.connect(
                dbname = hostname,
                user= username,
                password= password,
                host= ip)
        with connection.cursor() as cursor:
            cursor.execute(f"select * from customer where id == %s and name == %s", (id, name))
            result = cursor.fetchall()
        return result
    
    
    async def update_cast(self, id, name,):
        pass
    
    async def query_cast(self, query):
        connection = psycopg2.connect(
                dbname = hostname,
                user= username,
                password= password,
                host= ip)
        with connection.cursor() as cursor:
            cursor.execute(query)
            query_res = cursor.fetchall()
        return query_res

