"""
Author: David Santos
Repository: https://github.com/odavidsons/calorie-logger-python
Year: 2023

File imported by calorieLogger.py. Contains all of the database creation and querying functions.
"""
import sqlite3

class dbfunctions():

    conn = None
    cursor = None

    def __init__(self):
        try:
            self.conn = sqlite3.connect("calorieloggerDB")
            self.cursor = self.conn.cursor()
            self.initializeTables()
        except: print("There was an error starting the database connection.")
    
    #Create the database tables if they don't exist already
    def initializeTables(self):
        query = "CREATE TABLE dates (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, day INTEGER NOT NULL, month INTEGER NOT NULL, year INTEGER NOT NULL);"
        try:
            self.cursor.execute(query)
            self.conn.commit()
        except: self.conn.rollback()

        query = "CREATE TABLE foods (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, date_id INTEGER NOT NULL, name TEXT NOT NULL, calories REAL NOT NULL, carbs REAL NOT NULL DEFAULT 0, proteins REAL NOT NULL DEFAULT 0, fats REAL NOT NULL DEFAULT 0, CONSTRAINT fk_date_id FOREIGN KEY (date_id) REFERENCES dates (id) ON DELETE CASCADE);"
        try:
            self.cursor.execute(query)
            self.conn.commit()
        except: self.conn.rollback()

    #Return all the dates in the 'dates' table
    def getDates(self):
        query = "SELECT * FROM dates;"
        try:
            self.cursor.execute(query)
            list = self.cursor.fetchall()
            return list
        except: print("Error getting date list")

    #Return the id of a date
    def getDateId(self,day,month,year):
        query = f"SELECT id FROM dates WHERE day = '{day}' AND month = '{month}' AND year = '{year}';"
        try:
            self.cursor.execute(query)
            id = self.cursor.fetchone()
            return id
        except: print("Error getting date id")

    #Return all of the foods in a specific date
    def getFoodsByDateId(self,day,month,year):
        date_id = self.getDateId(day,month,year)
        query = f"SELECT * FROM foods WHERE date_id = '{date_id[0]}';"
        try:
            self.cursor.execute(query)
            list = self.cursor.fetchall()
            return list
        except: print("Error getting food list")

    #Insert a new date
    def insertDate(self,day,month,year):
        values = [day,month,year]
        query = "INSERT INTO dates (day,month,year) VALUES (?,?,?);"
        try:
            self.cursor.execute(query,values)
            self.conn.commit()
            print(f"Inserted date: {day},{month},{year}")
        except:
            self.conn.rollback()

    #Insert a new food entry for a date
    def insertFood(self,day,month,year,name,calories,carbs,proteins,fats):
        date_id = self.getDateId(day,month,year)
        values = [date_id[0],name,calories,carbs,proteins,fats]
        query = "INSERT INTO foods (date_id,name,calories,carbs,proteins,fats) VALUES (?,?,?,?,?,?);"
        try:
            self.cursor.execute(query,values)
            self.conn.commit()
            print(f"Inserted food: {date_id},{name},{calories},{carbs},{proteins},{fats}")
        except:
            self.conn.rollback()

    #Delete a date entry
    def deleteDate(self,id):
        query = f"DELETE FROM dates WHERE id = '{id}';"
        try:
            self.cursor.execute(query)
            self.conn.commit()
            print(f"Deleted date: {id}")
        except:
            self.conn.rollback()

    #Delete a food entry in a date
    def deleteFood(self,date_id,name,calories,carbs,proteins,fats):
        query = f"DELETE FROM foods WHERE date_id = '{date_id}' AND name = '{name}' AND calories = '{calories}' AND carbs = '{carbs}' AND proteins = '{proteins}' AND fats = '{fats}';"
        try:
            self.cursor.execute(query)
            self.conn.commit()
            print(f"Deleted food: {date_id},{name},{calories}")
        except:
            self.conn.rollback()

    #Check if there is a database connection active
    def databaseStatus(self):
        if self.conn != None and self.cursor != None:
            return "Database connected"
        else: return "Database disconnected"

    