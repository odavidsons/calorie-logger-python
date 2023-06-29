import customtkinter as ctk
import datetime
from tkinter import messagebox as msg

class mainView(ctk.CTkFrame):

    fontLarge = ('default',18,'bold')
    fontMedium = ('default',14)

    def __init__(self,master):
        super().__init__(master)
        topFrame = ctk.CTkFrame(self)
        topFrame.grid(row=0,column=0,columnspan=3,sticky="ew")
        labelTitle = ctk.CTkLabel(topFrame,text="Calorie logger",font=self.fontLarge)
        labelTitle.pack(pady=10)
            
        optionsFrame = ctk.CTkFrame(self)
        optionsFrame.grid(row=1,column=0,columnspan=3,sticky="nsew")
        self.btnExport = ctk.CTkButton(optionsFrame,text="Export")
        self.btnExport.grid(row=0,column=0,padx=20)
        self.btnSettings = ctk.CTkButton(optionsFrame,text="Settings")
        self.btnSettings.grid(row=0,column=1,padx=20)
        self.master.make_dynamic(optionsFrame)

        self.leftFrame = ctk.CTkFrame(self)
        self.leftFrame.grid(row=2,column=0,padx=10,pady=15)
        self.today = datetime.date.today()
        labelDate = ctk.CTkLabel(self.leftFrame,text="Date:")
        labelDate.grid(row=0,column=0,padx=5)
        self.labelCurrentDate = ctk.CTkLabel(self.leftFrame,text=f"{self.today.day}/{self.today.month}/{self.today.year}")
        self.labelCurrentDate.grid(row=0,column=1,padx=5)
        self.btnAddDate = ctk.CTkButton(self.leftFrame,text="Register today",command=self.addDate)
        self.btnAddDate.grid(row=0,column=2,padx=5)
        self.dateListFrame = ctk.CTkScrollableFrame(self.leftFrame)
        self.dateListFrame.grid(row=1,column=0,columnspan=3,padx=10,sticky="nsew")

        centerFrame = ctk.CTkFrame(self)
        centerFrame.grid(row=2,column=1,padx=10,pady=15)
        label1 = ctk.CTkLabel(centerFrame,text="Food name:",font=self.fontMedium)
        label1.grid(row=0,column=0,padx=5,pady=5)
        self.inputName = ctk.CTkEntry(centerFrame,font=self.fontMedium)
        self.inputName.grid(row=0,column=1,padx=5,pady=5)
        label2 = ctk.CTkLabel(centerFrame,text="Calories:",font=self.fontMedium)
        label2.grid(row=1,column=0,padx=5,pady=5)
        self.inputCalories = ctk.CTkEntry(centerFrame,font=self.fontMedium)
        self.inputCalories.grid(row=1,column=1,padx=5,pady=5)
        btnAdd = ctk.CTkButton(centerFrame,text=">> Add >>",font=self.fontMedium,command=self.addFood)
        btnAdd.grid(row=2,columnspan=2,padx=15,pady=5)

        rightFrame = ctk.CTkFrame(self)
        rightFrame.grid(row=2,column=2,padx=10,pady=15)
        labelDate1 = ctk.CTkLabel(rightFrame,text="Date:")
        labelDate1.grid(row=0,column=0,padx=5)
        self.labelDateSelected = ctk.CTkLabel(rightFrame,text="")
        self.labelDateSelected.grid(row=0,column=1,padx=5)
        self.foodListFrame = ctk.CTkScrollableFrame(rightFrame)
        self.foodListFrame.grid(row=1,column=0,columnspan=3,padx=10,sticky="nsew")
        labelTotal = ctk.CTkLabel(rightFrame,text="Total calories:")
        labelTotal.grid(row=2,column=0)
        self.labelTotalCalories = ctk.CTkLabel(rightFrame,text="")
        self.labelTotalCalories.grid(row=2,column=1)

        footerFrame = ctk.CTkFrame(self)
        footerFrame.grid(row=3,column=0,columnspan=3,sticky="ew")
        labelFooter = ctk.CTkLabel(footerFrame,text="Made by David Santos")
        labelFooter.pack()

    #Fill the date list with all the records from the database
    def fillDateList(self):
        #Change the state of the register button if the current date already has been inserted
        date = self.labelCurrentDate.cget("text").split("/")
        date_id = self.master.db.getDateId(date[0],date[1],date[2])
        if date_id != None:
            self.btnAddDate.configure(state="disabled",text="Already registered today")
        datelist = self.master.db.getDates()
        row = 0
        for result in datelist:
            date = f"{result[1]}/{result[2]}/{result[3]}"
            label = ctk.CTkLabel(self.dateListFrame,text=date)
            label.grid(row=row,column=0,padx=5)
            btn = ctk.CTkButton(self.dateListFrame,text=f"Select",command=self.fillFoodList)
            btn.grid(row=row,column=1,padx=5)
            row = row + 1


    #Fill the food list with all the records from the database
    def fillFoodList(self):
        self.labelDateSelected.configure(text=f"{self.today.day}/{self.today.month}/{self.today.year}")
        foodlist = self.master.db.getFoodsByDateId(self.today.day,self.today.month,self.today.year)
        row = 0
        calories = 0
        for result in foodlist:
            food = f"{result[2]} | {result[3]}"
            label = ctk.CTkLabel(self.foodListFrame,text=food)
            label.grid(row=row,column=0,padx=5)
            btn = ctk.CTkButton(self.foodListFrame,text=f"Remove",command=lambda: print(result[0]))
            btn.grid(row=row,column=1,padx=5)
            row = row + 1
            calories = calories + result[3]
        self.labelTotalCalories.configure(text=calories)
    
    #Call insertion for a date entry
    def addDate(self):
        date = self.labelCurrentDate.cget("text").split("/")
        self.master.db.insertDate(date[0],date[1],date[2])
        self.fillDateList()

    #Call insertion for a food entry on the selected date
    def addFood(self):
        if self.labelDateSelected.cget("text") != "":
            date = self.labelDateSelected.cget("text").split("/")
            try:
                self.master.db.insertFood(date[0],date[1],date[2],self.inputName.get(),float(self.inputCalories.get()))
                self.fillFoodList()
            except: msg.showwarning(title="Data invalid",message="Please enter a name and a valid number for the calories!")
        else: msg.showwarning(title="No date selected",message="You haven't selected a date to edit!")

    #Call deletion for a food entry on the selected date
    def removeFood(self):
        pass