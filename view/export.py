import customtkinter as ctk

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
        print(self.format.get())