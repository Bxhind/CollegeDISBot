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
username = ['username']
password = ['password']
hostname = ['hostname']

class DataBase():
    def __init__(self, ip, port,  username, password, hostname):
        self.ip = ip
        self.port = port
        self.username = username
        self.password = password
        self.hostname = hostname
        
    
    async def connection(self):
        try:
            connection = psycopg2.connect(
                dbname = hostname,
                user= username,
                password= password,
                host= ip)
            engine = create_engine(
                f'postgresql+psycopg2://{self.username}:{self.password}@{self.ip}:{self.port}/{self.hostname}')
            insp = inspect(engine)
            print(insp.get_table_names())
            connection.close()
        except:
            print("Can't establish connection to database, please try again, or fix the bug syka")
            
    
    async def fetch_customer(self):
        connection = psycopg2.connect(
                dbname = hostname,
                user= username,
                password= password,
                host= ip)
        with connection.cursor() as cursor:
            cursor.execute("Select * from customer")
            all_customers = cursor.fetchall()
            
            
    
