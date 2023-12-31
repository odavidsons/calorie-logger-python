"""
Author: David Santos
Repository: https://github.com/odavidsons/calorie-logger-python
Year: 2023

File imported by mainView.py. Renders all of the widgets belonging to the export window. Also has the controller functions for this window.
"""
import customtkinter as ctk
import json
import yaml
from customtkinter import filedialog as fd
from os import getcwdb

class export(ctk.CTkToplevel):

    fontLarge = ('default',18,'bold')
    fontMedium = ('default',14)

    def __init__(self,master):
        super().__init__(master)
        self.title("Export")
        self.format = ctk.StringVar(value="Choose..")
        self.format_list = ["JSON","YAML","Plain Text"]
        labelFormat = ctk.CTkLabel(self,text="Select format:",font=self.fontMedium)
        labelFormat.grid(row=0,column=0,padx=20,pady=20)
        selectFormat = ctk.CTkOptionMenu(self,values=self.format_list,variable=self.format,font=self.fontMedium)
        selectFormat.grid(row=0,column=1,padx=20)
        btnExport = ctk.CTkButton(self,text="Export",font=self.fontMedium,command=self.exportData)
        btnExport.grid(row=1,columnspan=2,padx=10,pady=10)
        self.labelMessage = ctk.CTkLabel(self,text="")
        self.labelMessage.grid(row=2,columnspan=2,padx=20,pady=5)

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
                        "calories": value,
                        "carbs": value,
                        "proteins": value,
                        "fats": value
                    }
                ]
            }
            ]}"""
        
        data= {"dates": []}
        query_dates = self.master.db.getDates()
        for date in query_dates:
            query_foods = self.master.db.getFoodsByDateId(date[1],date[2],date[3])
            foods_list = []
            for food in query_foods:
                foods_list.append({"name": food[2],"calories": food[3],"carbs": food[4],"proteins": food[5],"fats": food[6]})
            data["dates"].append({"day":date[1],"month":date[2],"year":date[3],"foods":foods_list})

        if format == "JSON":
            json_data = json.dumps(data,indent=4)
            file_types = (('JSON files', '*.json'),('All files', '*.*'))
            try:
                filename = fd.asksaveasfilename(title="Choose export location",filetypes=file_types,initialdir=getcwdb())
                with open(filename,"w") as outfile:
                    outfile.write(json_data)
                self.labelMessage.configure(text=f"Data exported!\n{filename}")
            except: print("failed export")
        elif format == "YAML":
            file_types = (('YAML files', '*.yaml'),('All files', '*.*'))
            try:
                filename = fd.asksaveasfilename(title="Choose export location",filetypes=file_types,initialdir=getcwdb())
                with open(filename,"w") as outfile:
                    yaml.dump(data,outfile,indent=4)
                self.labelMessage.configure(text=f"Data exported!\n{filename}")
            except: print("failed export")
        elif format == "Plain Text":
            file_types = (('Text files', '*.txt'),('All files', '*.*'))
            try:
                filename = fd.asksaveasfilename(title="Choose export location",filetypes=file_types,initialdir=getcwdb())
                with open(filename,"w") as outfile:
                    for key in data["dates"]:
                        outfile.write(str(key)+"\n")
                self.labelMessage.configure(text=f"Data exported!\nPath: {filename}")
            except: print("failed export")