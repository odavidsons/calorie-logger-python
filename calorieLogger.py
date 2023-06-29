import customtkinter as ctk
from view.mainView import mainView
from db.dbfunctions import dbfunctions

class calorieLogger(ctk.CTk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        self.resizable(True,True)
        self.mainFrame = mainView(self) #Render main app widgets
        self.mainFrame.grid()
        self.connectDB()
        self.make_dynamic(self)

    #Start database connection
    def connectDB(self):
        try:
            self.db = dbfunctions()
            print(self.db.databaseStatus())
            self.mainFrame.fillDateList()
        except: pass

    #Make a window's widgets dynamic when resizing
    def make_dynamic(self,window):
        col_count,row_count = window.grid_size()
        
        for i in range(row_count):
            window.grid_rowconfigure(i, weight=1)

        for i in range(col_count):
            window.grid_columnconfigure(i, weight=1)
