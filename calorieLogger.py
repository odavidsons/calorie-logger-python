import customtkinter as ctk
from view.mainView import mainView
from db.dbfunctions import dbfunctions

class calorieLogger(ctk.CTk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        self.mainFrame = mainView(self)
        self.mainFrame.pack()
        self.connectDB()
        self.resizable(True,True)
        
    def connectDB(self):
        try:
            self.db = dbfunctions()
            print(self.db.databaseStatus())
            self.fillDateList()
        except: pass

    def fillDateList(self):
        datelist = self.db.getDates()
        row = 0
        for result in datelist:
            date = f"{result[1]}/{result[2]}/{result[3]}"
            label = ctk.CTkLabel(self.mainFrame.dateListFrame,text=date)
            label.grid(row=row,column=0)
            btn = ctk.CTkButton(self.mainFrame.dateListFrame,text=f"Select ({row})")
            btn.grid(row=row,column=1)
            row = row + 1
    
    #Make a window's widgets dynamic when resizing
    def make_dynamic(self,window):
        col_count,row_count = window.grid_size()
        
        for i in range(row_count):
            window.grid_rowconfigure(i, weight=1)

        for i in range(col_count):
            window.grid_columnconfigure(i, weight=1)

        for child in window.children.values():
            try:
                child.grid_configure(sticky="nsew")
                self.make_dynamic(child)
            except: pass
