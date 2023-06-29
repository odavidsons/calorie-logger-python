"""
Author: David Santos
Repository: https://github.com/odavidsons/calorie-logger-python
Year: 2023

File imported by mainView.py. Renders all of the widgets belonging to the export window. Also has the controller functions for this window.
"""
import customtkinter as ctk
import json

class export(ctk.CTkToplevel):

    def __init__(self,master):
        super().__init__(master)
        self.title("Export")
        self.format = ctk.StringVar(value="Choose..")
        self.format_list = ["JSON","CSV"]
        labelFormat = ctk.CTkLabel(self,text="Select format:")
        labelFormat.grid(row=0,column=0,padx=10,pady=20)
        selectFormat = ctk.CTkOptionMenu(self,values=self.format_list,variable=self.format)
        selectFormat.grid(row=0,column=1,padx=10)
        btnExport = ctk.CTkButton(self,text="Export",command=self.exportData)
        btnExport.grid(row=1,columnspan=2,padx=10,pady=20)

    def exportData(self):
        format = self.format.get()
        data = {"date": "day/month/year"}
        query_dates = self.master.db.getDates()
        for date in query_dates:
            data.update({"date": date})

        if format == "JSON":
            json_data = json.dumps(list(data))
            with open("calorieLoggerExport.json","w") as outfile:
                outfile.write(json_data)
        elif format == "CSV":
            print(format)