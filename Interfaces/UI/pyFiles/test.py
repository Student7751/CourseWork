import sys
from PyQt5.QtSql import QSqlDatabase
import sqlite3
from PyQt5.QtWidgets import QTableView, QApplication
from datetime import date

db = sqlite3.connect('ProgramDB.db')

def create_table(db):
    query = """
    CREATE TABLE IF NOT EXISTS UnconfirmedRecords
    (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        USER_ID INTEGER NOT NULL,
        RECORD_ID INTEGER NOT NULL,
        TYPE TEXT NOT NULL,
        DESCRIPTION TEXT NOT NULL
    )
    """
    # query = """
    # CREATE TABLE IF NOT EXISTS OFFERS
    # (
    #     ID INTEGER PRIMARY KEY AUTOINCREMENT,
    #     NAME TEXT NOT NULL,
    #     DESCR TEXT NOT NULL,
    #     PRICE INT NOT NULL
    # )
    # """
    # query = """
    #     CREATE TABLE if not exists CLIENTS
    #     (
    #      ID INTEGER PRIMARY KEY AUTOINCREMENT,
    #      SURNAME TEXT NOT NULL,
    #      NAME TEXT NOT NULL,
    #      PATRONYMIC TEXT NOT NULL,
    #      PHONE_NUMBER TEXT NOT NULL
    #     )
    #     """
    # query = """
    # CREATE TABLE if not exists ENTRYDATA
    # (
    #  ID INTEGER,
    #  LOGIN TEXT NOT NULL,
    #  PASSWORD TEXT NOT NULL
    # )
    # """
    cur = db.cursor()
    cur.execute("DROP TABLE UnconfirmedRecords")
    cur.execute(query)

    # query = """
    #     CREATE TABLE if not exists NOTARIES
    #     (
    #      ID INTEGER PRIMARY KEY AUTOINCREMENT,
    #      SURNAME TEXT NOT NULL,
    #      NAME TEXT NOT NULL,
    #      PATRONYMIC TEXT NOT NULL,
    #      PHONE_NUMBER TEXT NOT NULL
    #     )
    #     """

def insert_user(db, surname, name, patronymic, phone_number):
    query = """
    INSERT INTO Notaries(SURNAME, NAME, PATRONYMIC, PHONE_NUMBER)
    VALUES (?,?,?,?)
    """
    # query2 = "select max(ID) + 1 from clients"
    cur = db.cursor()
    # res = cur.execute(query2).fetchone()
    cur.execute(query, (surname, name, patronymic, phone_number))
    db.commit()

    # # Получаем количество строк в таблице
    # cur.execute("SELECT COUNT(*) FROM Clients")
    # row_count = cur.fetchone()[0]
    #
    # # Формируем новый ID с префиксом "10"
    # new_id = "10" + str(row_count)
    #
    # # Обновляем ID вставленной записи
    # update_query = """
    # UPDATE Clients SET ID = ? WHERE ID = ?
    # """
    # cur.execute(update_query, (new_id, cur.lastrowid))
    # db.commit()

def get_all_clients(db, name):
    query = f'SELECT * FROM {name}'
    cur = db.cursor()
    items_io = cur.execute(query)
    item_lst = [i for i in items_io]
    return item_lst

def update_mbd(db, id, login, password):
    query = """
        INSERT INTO EntryData(ID, Login, PASSWORD)
        VALUES (?,?,?)
        """
    cur = db.cursor()
    cur.execute(query, (id, login, password))
    db.commit()

def insertRecord(db, userID, RecordID, Descr):
    query = """
        INSERT INTO UnconfirmedRecords(USER_ID, RECORD_ID, DESCRIPTION)
        VALUES (?,?,?)
    """
    cur = db.cursor()
    cur.execute(query, (userID, RecordID, Descr))
    db.commit()

def getRecord(db, RecordID):
    query = """
        SELECT DESCRIPTION FROM UnconfirmedRecords
        WHERE ID = ?
    """
    cur = db.cursor()
    cur.execute(query, (RecordID, ))
    res = cur.fetchone()
    return res

def deleteRecord(db, RecordID):
    query = """
            delete from UnconfirmedRecords where RECORD_ID = ?
        """
    cur = db.cursor()
    cur.execute(query, (RecordID, ))
    db.commit()

def insertOffer(db, name, date, discount, price, clientID, notaryID):
    query = """
        INSERT INTO COMPLETEDDEALS(NAME, DATE, DISCOUNT, PRICE, CLIENT_ID, NOTARY_ID)
        VALUES (?,?,?,?,?,?)
    """
    cur = db.cursor()
    cur.execute(query, (name, date, discount, price, clientID, notaryID))
    db.commit()

def update_client(db, client_id, updated_name, updated_surname, updated_patronymic, updated_number):
    query = "UPDATE Clients SET NAME=?, SURNAME=?, PATRONYMIC=?, PHONE_NUMBER=? WHERE ID=?"
    cur = db.cursor()
    cur.execute(query, (updated_name, updated_surname,
                updated_patronymic, updated_number, client_id))
    db.commit()

def delete_client(db, table):
    # Define the SQL query to delete a book with a specific ID
    query = f"DROP TABLE {table}"
    # Execute the query with the provided book ID as a parameter
    db.execute(query)
    # Commit the changes to the database
    db.commit()

def addOffer(db, name, descr, price):
    query = """
    insert into OFFERS(name, descr, price)
    values (?, ?, ?)
    """
    cur = db.cursor()

    cur.execute(query, (name, descr, price))

    db.commit()

#create_table(db)
# update_mbd(db, 1, "Philosoph", "123")
# update_mbd(db, 2, "log2", "pass2")
# update_mbd(db, 3, "log3", "pass3")
# update_mbd(db, 4, "log4", "pass4")
# update_mbd(db, 5, "log5", "pass5")
# delete_client(db, "ENTRYDATA")
# delete_client(db, "clients")
# delete_client(db, "notaries")
print(get_all_clients(db, "ADMINS"))
#insertRecord(db, 21, 12, "Новая услуга2: Залупка с медом")
#print(get_all_clients(db, "UnconfirmedRecords"))
#deleteRecord(db, 10)
#print(get_all_clients(db, "UnconfirmedRecords"))
#print(date(2000, 12, 12))
#insertOffer(db, "Авовоов", date(2013, 12, 13), 3, 2200, 13, 1)
#insertOffer(db, "Name2", "11.11.2011", 7.12, 2004, 3, 19)
print(get_all_clients(db, "COMPLETEDDEALS"))
# addOffer(db, 'Заверение договора', 'Проверка подлинности документа и правильности содержания договоров', 3000)
# addOffer(db, 'Выдача нотариальных заверений', 'Нотариус может заверить копии документов, выдать нотариальные свидетельства', 3500)
# addOffer(db, 'Оформление наследства', 'Нотариус помогает оформить наследственные права на имущество', 2500)
# addOffer(db, 'Оформление сделок с недвижимостью', 'Оформление сделок купли-продажи, дарения и т.д', 3700)
# addOffer(db, 'Оформление доверенностей', 'Нотариус может удостоверить правильность составления доверенностей', 2600)

cur = db.cursor()

#cur.execute("CREATE INDEX idx_login ON ENTRYDATA(LOGIN);")
#cur.execute("CREATE INDEX idx_password ON ENTRYDATA(PASSWORD);")
# def getUsers(cls, table, batch_size=1000):
#     ...
#     while True:
#         rows = cls.cur.fetchmany(batch_size)
#         if not rows:
#             break
#         for row in rows:
#             yield row
# print(cur.execute("PRAGMA index_list('CLIENTS');").fetchall())
# print(get_all_clients(db, "EntryData"))
# print(get_all_clients(db, "Clients"))
# print(get_all_clients(db, "NOTARIES"))
# print(get_all_clients(db, "ADMINS"))

# for i in range(1, 10):
#     delete_client(db, i)
# insert_user(db, "Бытийный", "Сократ", "Ничеевич", "+79831765432")
# insert_user(db, "Загадочный", "Федор", "Евгеньевич", "+79836435432")
# insert_user(db, "Грибник", "Дмитрий", "Валерьевич", "+79831765413")
# insert_user(db, "Непредсказуемый", "Желатин", "Арсеньевич", "+79831765445")
# insert_user(db, "Последний", "Константин", "Ластович", "+79831765441")

# print(get_all_clients(db, "NOTARIES"))
# insert_user(db, "Новый2", "Нотариус", "ХИХИХИХА", "+79131715441")
# print(get_all_clients(db, "NOTARIES"))

def get_client(db, login, password):
    cur = db.cursor()

    query = f"""
    SELECT *
    FROM CLIENTS JOIN ENTRYDATA
    WHERE ENTRYDATA.LOGIN = "{login}" AND ENTRYDATA.PASSWORD = "{password}"
    AND CLIENTS.ID = ENTRYDATA.ID
    """

    res = cur.execute(query)
    return list(i for i in res)

def add_client(db, surname, name, patronymic, phone_number, login, password):
    query = """
        INSERT INTO Clients(SURNAME, NAME, PATRONYMIC, PHONE_NUMBER)
        VALUES (?,?,?,?)
        """
    query2 = """
    INSERT INTO ENTRYDATA(ID, LOGIN, PASSWORD)
    VALUES (?,?,?)
    """
    cur = db.cursor()
    last_inserted_id = cur.lastrowid
    cur.execute(query, (surname, name, patronymic, phone_number))
    cur.execute(query2, (last_inserted_id, login, password))
    db.commit()

login = "log3"
password = "pass9"
#add_client(db, "New", "Client", "OGO", "+9123812412", "NerLog", "NerPass")
# print(get_all_clients(db, "EntryData"))
# print(get_all_clients(db, "Clients"))
# print(get_client(db, "NerLog", "NerPass"))


