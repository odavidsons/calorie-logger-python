"""
Author: David Santos
Repository: https://github.com/odavidsons/calorie-logger-python
Year: 2023

File imported by mainView.py. Renders all of the widgets belonging to the export window. Also has the controller functions for this window.
"""
import customtkinter as ctk
import json
from customtkinter import filedialog as fd
from os import getcwdb

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
        self.labelMessage = ctk.CTkLabel(self,text="")
        self.labelMessage.grid(row=2,columnspan=2,padx=10,pady=10)

    def exportData(self):
        format = self.format.get()
        """Export JSON format
        data = {"dates": [
            {
                "day":"dd",
                "month": "mm",
                "year": "yyyy",
                "foods": [
                    {
                        "name": "food example",
                        "calories": value
                    }
                ]
            }
            ]}"""
        
        data= {"dates": []}
        query_dates = self.master.db.getDates()
        for date in query_dates:
            foods_list = self.master.db.getFoodsByDateId(date[1],date[2],date[3])
            data["dates"].append({"day":date[1],"month":date[2],"year":date[3],"foods":foods_list})

        if format == "JSON":
            json_data = json.dumps(data,indent=4)
            file_types = (('JSON files', '*.json'),('All files', '*.*'))
            try:
                filename = fd.asksaveasfilename(title="Choose export location",filetypes=file_types,initialdir=getcwdb())
                with open(filename,"w") as outfile:
                    outfile.write(json_data)
                self.labelMessage.configure(text=f"Data exported!\n{filename}")
            except: pass
        elif format == "CSV":
            print(format)