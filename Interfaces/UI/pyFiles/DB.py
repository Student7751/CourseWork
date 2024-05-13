# Importing sqlite to work on DataBase
import sqlite3


class DB:
    """Class containing methods for working with the database.
    The database including 4 tables: Clients, Notaries, Admins and "private" table - ENTRYDATA.
    The ENTRYDATA table including private parameters for all users such as login and password."""

    # Connecting the main DataBase (Creating new one if it does not exist)
    db = sqlite3.connect('ProgramDB.db')
    # Creating cursor to work in DataBase
    cur = db.cursor()

    # Returning True if login exists in the table
    @classmethod
    def isLoginExists(cls, login):
        # Getting ID for example (may get any column or something)
        query = f"""
            SELECT ID
            FROM ENTRYDATA
            WHERE ENTRYDATA.LOGIN = "{login}"
        """

        # Executing query
        return cls.cur.execute(query).fetchone() is not None

    # Getting data from private table ENTRYDATA
    @classmethod
    def getEntryData(cls):
        query = "SELECT * FROM ENTRYDATA"
        return tuple(cls.cur.execute(query))

    # Returning tuple(NAME, SURNAME) of user if it's exists
    @classmethod
    def getUser(cls, table, login, password):
        # Creating query to get client data
        query = f"""
            SELECT NAME, SURNAME
            FROM {table} JOIN ENTRYDATA
            ON {table}.ID = ENTRYDATA.ID
            WHERE ENTRYDATA.LOGIN = ? AND ENTRYDATA.PASSWORD = ?
            """
        # Executing query with parameters
        cls.cur.execute(query, (login, password))
        # Fetching result
        res = cls.cur.fetchone()
        # Returning result
        return res if res else ()

    @classmethod
    def getUsers(cls, table):
        query = f"SELECT * FROM {table}"
        return tuple(cls.cur.execute(query))

    # Adding client into DataBase
    @classmethod
    def addUser(cls, table, name, surname, patronymic, phone_number, login, password):
        # Adding client into Clients table
        insertClients = f"""
                INSERT INTO {table}(SURNAME, NAME, PATRONYMIC, PHONE_NUMBER)
                VALUES (?,?,?,?)
                """
        # Adding client private data into ENTRYDATA table
        insertEntryData = """
            INSERT INTO ENTRYDATA(ID, LOGIN, PASSWORD)
            VALUES (?,?,?)
            """
        # Execute queries to tables
        cls.cur.execute(insertClients, (surname, name, patronymic, phone_number))
        # Getting ID of added client to insert it into ENTRYDATA table
        last_inserted_id = cls.cur.lastrowid
        cls.cur.execute(insertEntryData, (last_inserted_id, login, password))
        # Commit changes into main DataBase
        cls.db.commit()
