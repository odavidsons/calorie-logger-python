import sqlite3

class dbfunctions():

    conn = None
    cursor = None

    def __init__(self):
        try:
            self.conn = sqlite3.connect("calorielogger")
            self.cursor = self.conn.cursor()
            self.initializeTables()
        except: print("There was an error starting the database connection.")
    
    def initializeTables(self):
        query = "CREATE TABLE dates (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, day INTEGER NOT NULL, month INTEGER NOT NULL, year INTEGER NOT NULL);"
        try:
            self.cursor.execute(query)
            self.conn.commit()
        except: self.conn.rollback()

    def getDates(self):
        query = "SELECT * FROM dates;"
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except: print("Error getting date list")

    def insertDate(self,day,month,year):
        values = [day,month,year]
        query = "INSERT INTO dates (day,month,year) VALUES (?,?,?);"
        try:
            self.cursor.execute(query,values)
            self.conn.commit()
            print(f"Inserted date: {day},{month},{year}")
        except:
            self.conn.rollback()

    def databaseStatus(self):
        if self.conn != None and self.cursor != None:
            return "Database connected"
        else: return "Database disconnected"

    