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
            WHERE ENTRYDATA.LOGIN = ?
        """

        # Executing query
        return cls.cur.execute(query, (login, )).fetchone() is not None

    # Updating the table when a user edits a profile (not work with Admin and Offers tables)
    @classmethod
    def updateTable(cls, table, ID, name, surname, patronymic, phone_number, login, password):
        # Updating data in user table
        updateTable = f"UPDATE {table} SET NAME=?, SURNAME=?, PATRONYMIC=?, PHONE_NUMBER=? WHERE ID=?"
        # Updating data in private table
        updateEntryData = f"UPDATE ENTRYDATA SET LOGIN=?, PASSWORD=? WHERE ID=?"
        # Executing queries
        cls.cur.execute(updateTable, (name, surname, patronymic, phone_number, ID))
        cls.cur.execute(updateEntryData, (login, password, ID))
        # Commit changes
        # db.commit()

    # Returning tuple(ID, SURNAME, NAME, Patronymic, Phone_Number, Login, Password) of user if it's exists
    @classmethod
    def getUser(cls, table, login, password):
        # Creating query to get client data
        query = f"""
            SELECT {table}.ID, {table}.SURNAME, {table}.NAME, {table}.PATRONYMIC, {table}.PHONE_NUMBER, LOGIN, PASSWORD
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


    @classmethod
    def getInfoFromCompletedDeals(cls, clientID):
        query = """
            SELECT NAME, DATE, PRICE
            FROM COMPLETEDDEALS
            WHERE CLIENT_ID = ?
        """

        return cls.cur.execute(query, (clientID, )).fetchall()
    @classmethod
    def getClientsByNotaryID(cls, notaryID):
        query = """
            SELECT * FROM CLIENTS
            WHERE CLIENTS.ID IN (SELECT COMPLETEDDEALS.CLIENT_ID FROM COMPLETEDDEALS
                                WHERE COMPLETEDDEALS.NOTARY_ID = ?)
        """

        return cls.cur.execute(query, (notaryID, )).fetchall()

    # Getting data to view completed deals
    @classmethod
    def getNotariesNameByID(cls, ID):
        query = f"""
        SELECT Completeddeals.ID, Completeddeals.Name, Discount, Notaries.Name, Price, Date
        FROM completeddeals join Notaries on Notaries.ID = completeddeals.Notary_ID and Client_ID = ?
        """
        return cls.cur.execute(query, (ID, )).fetchall()

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
    # Adding offer into table
    @classmethod
    def addOffer(cls, name, descr, price):
        # Adding new record into table
        query = """
            INSERT INTO OFFERS(NAME, DESCR, PRICE)
            VALUES (?, ?, ?)
        """
        # Executing the query
        cls.cur.execute(query, (name, descr, price))
        # Commit changes into main Database
        #cls.db.commit()

    # Adding deal into table
    @classmethod
    def addDeal(cls, date, name, discount, price, clientID, notaryID):
        # Separating several deals
        name = "; ".join(name)
        # Adding new deal
        query = """
                INSERT INTO COMPLETEDDEALS(NAME, DATE, DISCOUNT, PRICE, CLIENT_ID, NOTARY_ID)
                VALUES (?,?,?,?,?,?)
            """
        # Executing query
        cls.cur.execute(query, (name, date, discount, price, clientID, notaryID))
        # Commit changes into main Database
        #cls.db.commit()

    # Adding record to table
    @classmethod
    def addUnconfRecord(cls, userID, recordID, type, descr):
        query = """
                INSERT INTO UnconfirmedRecords(USER_ID, RECORD_ID, TYPE, DESCRIPTION)
                VALUES (?,?,?,?)
            """
        cls.cur.execute(query, (userID, recordID, type, descr))

        #cls.db.commit()
    # Getting description from table by ID
    @classmethod
    def getUnconfRecordDescr(cls, recordID):
        query = """
                SELECT DESCRIPTION FROM UnconfirmedRecords
                WHERE ID = ?
            """
        return cls.cur.execute(query, (recordID, )).fetchone()

    @classmethod
    def deleteUnconfRecord(cls, recordID):
        query = """
                DELETE FROM UnconfirmedRecords
                WHERE ID = ?
        """
        cls.cur.execute(query, (recordID, ))

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
