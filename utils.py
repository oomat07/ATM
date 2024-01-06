import psycopg2
from dotenv import load_dotenv
import os
from random import randint
load_dotenv()
conn_params = {
    'dbname' : os.getenv('dbname'),
    'user' : os.getenv ('user'),
    'password' : os.getenv('password'),
    'host' : os.getenv('host'),
    'port' : os.getenv('port')
}

conn = psycopg2.connect(**conn_params)
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS clients(
               client_id  SERIAL PRIMARY KEY,
               firstname VARCHAR(50),
               lastname VARCHAR(50),
               middlename VARCHAR(50),
               acoount_number BIGINT UNIQUE
);  
  """)


cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions(
               transaction_id  SERIAL PRIMARY KEY,
               account_number BIGINT,
               amount NUMERIC,
               type VARCHAR(50),
               FOREIGN KEY (account_number) REFERENCES clients(acoount_number)
);                    
    """)

conn.commit()

def create_account():
    try:
        firstname = input("YOUR FIRSTNAME: ")
        lastname = input("YOUR LASTNAME: ") 
        middlename = input("YOUR MIDDLENAME: ")
        firstname = input("YOUR NAME: ")    
        account_number = 11800000000 + randint(0, 99999999)
    
        cursor.execute(f"""INSERT INTO clients (firstname, lastname, middlename, account_number) VALUES ({firstname}, 
        {lastname},{middlename}, {account_number})
        """)
        conn.commit()
        print(f"счет создан. Номер счета: {account_number}")
    except Exception as e:
        print(f"ERROR! ACCOUNT WAS NOT CREATED: {e}")


def deposit():
    try:
        account_number = int(input("введите номер счета: "))
        amount = float(input("введите сумму пополнения: "))
        cursor.execute(f"""
                   INSERT INTO transactions (account_number, amount, type)
                   VALURS ({account_number}, {amount}, "deposit")
        """)
        conn.comit()
        print("счет пополнен")
    except Exception as e:
        print(f"ошибка! счет не был пополнен: {e}")

def chek_balance(amount, account_number):
    cursor.execute(f"SELECT sum(amount) FROM transictions WHERE acoount_number = {account_number}")
    balance = cursor.fetchall()[0]
    return balance >= amount

def with_draw():
    account_number = int(input(f"введите номер счета: "))
    amount = float(input("введите сумму пополнения: "))
    cursor.execute(f"""
                   INSERT INTO transitions (account_number, amount, type)
                   VALUES ({account_number}, {amount}, "deposit")
  """)
    conn.commit()


# git config --global user.email "you@example.com"
# git config --global user.name "Ваше Имя"