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

    # Returning tuple(ID, NAME, SURNAME) of user if it's exists
    @classmethod
    def getUser(cls, table, login, password):
        # Creating query to get client data
        query = f"""
            SELECT {table}.ID, {table}.NAME, {table}.SURNAME
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

    # Getting data from any table
    @classmethod
    def getUsers(cls, table):
        query = f"SELECT * FROM {table}"
        return cls.cur.execute(query).fetchall()

    # Getting notary data from table
    @classmethod
    def getNotariesNames(cls):
        query = "SELECT ID, NAME, SURNAME, PATRONYMIC FROM NOTARIES"
        return cls.cur.execute(query).fetchall()

    # Adding client into DataBase
    @classmethod
    def addUser(cls, table, surname, name, patronymic, phone_number, login, password):
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

    # Adding deal into table
    @classmethod
    def addDeal(cls, date, name, discount, price, notaryID, clientID):
        # Separating several deals
        name = "; ".join(name)
        # Adding new deal
        query = """
                INSERT INTO COMPLETEDDEALS(NAME, DATE, DISCOUNT, PRICE, NOTARY_ID, CLIENT_ID)
                VALUES (?,?,?,?,?,?)
            """
        # Executing query
        cls.cur.execute(query, (name, date, discount, price, notaryID, clientID))
        # Commit changes into main Database
        #cls.db.commit()

    # Delete user from any table in the database
    @classmethod
    def deleteUser(cls, userID, table):
        # Query to delete user from his own table
        query = f"DELETE FROM {table} WHERE ID = ?"
        # Deleting data from a private table depending on the postfix
        if table == "notaries":
            query2 = f"DELETE FROM ENTRYDATA WHERE LOGIN like '%@notary.com' and ID = ?"
        else:
            query2 = f"DELETE FROM ENTRYDATA WHERE LOGIN like '%@client.com' and ID = ?"
        # Executing queries
        cls.cur.execute(query, (userID, ))
        cls.cur.execute(query2, (userID, ))

        # Commit changes into main Database
        cls.db.commit()

