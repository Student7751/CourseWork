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
    def getClientByLog(cls, login, password):
        # Creating query to get client data
        query = f"""
            SELECT NAME, SURNAME
            FROM CLIENTS JOIN ENTRYDATA
            WHERE ENTRYDATA.LOGIN = "{login}" AND ENTRYDATA.PASSWORD = "{password}"
            AND CLIENTS.ID = ENTRYDATA.ID
            """
        # Executing query
        res = cls.cur.execute(query)
        # Returning result
        return tuple(res)

    @classmethod
    def getAdminByLog(cls, login, password):
        pass

    # Adding client into DataBase
    @classmethod
    def addClient(cls, name, surname, patronymic, phone_number, login, password):
        # Adding client into Clients table
        insertClients = """
                INSERT INTO Clients(SURNAME, NAME, PATRONYMIC, PHONE_NUMBER)
                VALUES (?,?,?,?)
                """
        # Adding client private data into ENTRYDATA table
        insertEntryData = """
            INSERT INTO ENTRYDATA(ID, LOGIN, PASSWORD)
            VALUES (?,?,?)
            """
        # Getting ID of added client to insert it into ENTRYDATA table
        last_inserted_id = cls.cur.lastrowid
        # Execute queries to tables
        cls.cur.execute(insertClients, (surname, name, patronymic, phone_number))
        cls.cur.execute(insertEntryData, (last_inserted_id, login, password))
        # Commit changes into main DataBase
        cls.db.commit()
