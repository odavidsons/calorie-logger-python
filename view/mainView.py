import customtkinter as ctk
import datetime
from tkinter import messagebox as msg
from tkinter.ttk import Treeview
from tkinter import END
from view.settings import settings
from view.export import export

class mainView(ctk.CTkFrame):

    fontLarge = ('default',18,'bold')
    fontMedium = ('default',14)

    def __init__(self,master):
        super().__init__(master)

        optionsFrame = ctk.CTkFrame(self)
        optionsFrame.grid(row=0,column=0,columnspan=3,sticky="nsew")
        labelTitle = ctk.CTkLabel(optionsFrame,text="Calorie logger",font=self.fontLarge)
        labelTitle.grid(row=0,column=0,columnspan=4,pady=15)
        self.btnExport = ctk.CTkButton(optionsFrame,text="Export",font=self.fontMedium,command=lambda: export(master))
        self.btnExport.grid(row=1,column=0,padx=20,pady=10)
        self.btnSettings = ctk.CTkButton(optionsFrame,text="Settings",font=self.fontMedium,command=lambda: settings(master))
        self.btnSettings.grid(row=1,column=1,padx=20,pady=10)
        self.btnToggleMode = ctk.CTkButton(optionsFrame,text="Toggle Theme",font=self.fontMedium,command=self.master.toggleUIMode)
        self.btnToggleMode.grid(row=1,column=2,padx=20,pady=10)
        self.btnExit = ctk.CTkButton(optionsFrame,text="Exit",font=self.fontMedium,command=self.master.quit)
        self.btnExit.grid(row=1,column=3,padx=20,pady=10)
        self.master.make_dynamic(optionsFrame)

        self.leftFrame = ctk.CTkFrame(self)
        self.leftFrame.grid(row=1,column=0,padx=10,pady=15)
        self.today = datetime.date.today()
        labelDate = ctk.CTkLabel(self.leftFrame,text="Date:")
        labelDate.grid(row=0,column=0,padx=5)
        self.labelCurrentDate = ctk.CTkLabel(self.leftFrame,text=f"{self.today.day}/{self.today.month}/{self.today.year}")
        self.labelCurrentDate.grid(row=0,column=1,padx=5)
        self.btnAddDate = ctk.CTkButton(self.leftFrame,text="Register today",command=self.addDate)
        self.btnAddDate.grid(row=0,column=2,padx=5,pady=5)
        self.dateListFrame = ctk.CTkScrollableFrame(self.leftFrame)
        self.dateListFrame.grid(row=1,column=0,columnspan=3,padx=10,pady=15,sticky="nsew")

        centerFrame = ctk.CTkFrame(self)
        centerFrame.grid(row=1,column=1,padx=10,pady=15)
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
        self.btnRemove = ctk.CTkButton(centerFrame,text="<< Remove <<",font=self.fontMedium,fg_color="#c21717",hover_color="#9e1919",command=self.removeFood)
        self.btnRemove.grid(row=3,columnspan=2,padx=15,pady=5)
        self.labelMessage = ctk.CTkLabel(centerFrame,text="")
        self.labelMessage.grid(row=4,columnspan=2,pady=5)

        rightFrame = ctk.CTkFrame(self)
        rightFrame.grid(row=1,column=2,padx=10,pady=15)
        labelDate1 = ctk.CTkLabel(rightFrame,text="Date:")
        labelDate1.grid(row=0,column=0,padx=5)
        self.labelDateSelected = ctk.CTkLabel(rightFrame,text="")
        self.labelDateSelected.grid(row=0,column=1,padx=5)
        self.btnClearList = ctk.CTkButton(rightFrame,text="Clear Selection",command=self.clearList)
        self.btnClearList.grid(row=0,column=2,padx=5,pady=5)
        self.foodListTree = Treeview(rightFrame,columns=("date_id","name","calories"),show='headings')
        self.foodListTree.grid(row=1,column=0,columnspan=3,padx=10,pady=15,sticky="nsew")
        self.foodListTree.heading("name",text="Food")
        self.foodListTree.heading("calories",text="Calories")
        self.foodListTree["displaycolumns"]=("name", "calories")
        labelTotal = ctk.CTkLabel(rightFrame,text="Total calories:")
        labelTotal.grid(row=2,column=0)
        self.labelTotalCalories = ctk.CTkLabel(rightFrame,text="")
        self.labelTotalCalories.grid(row=2,column=1)

        footerFrame = ctk.CTkFrame(self)
        footerFrame.grid(row=2,column=0,columnspan=3,sticky="ew")
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
            label.grid(row=row,column=0,padx=5,pady=5)
            btn = ctk.CTkButton(self.dateListFrame,text=f"Select",command=self.fillFoodList)
            btn.grid(row=row,column=1,padx=5,pady=5)
            row = row + 1


    #Fill the food list with all the records from the database
    def fillFoodList(self):
        self.foodListTree.delete(*self.foodListTree.get_children()) #Clear the list
        self.labelDateSelected.configure(text=f"{self.today.day}/{self.today.month}/{self.today.year}")
        foodlist = self.master.db.getFoodsByDateId(self.today.day,self.today.month,self.today.year)
        row = 0
        calories = 0
        for result in foodlist:
            self.foodListTree.insert('',END,values=(result[1],result[2],result[3]))
            row = row + 1
            calories = calories + result[3]
        self.labelTotalCalories.configure(text=calories)
    
    #Handle insertion for a date entry
    def addDate(self):
        date = self.labelCurrentDate.cget("text").split("/")
        self.master.db.insertDate(date[0],date[1],date[2])
        self.fillDateList()

    #Handle insertion for a food entry on the selected date
    def addFood(self):
        if self.labelDateSelected.cget("text") != "":
            date = self.labelDateSelected.cget("text").split("/")
            try:
                self.master.db.insertFood(date[0],date[1],date[2],self.inputName.get(),float(self.inputCalories.get()))
                self.fillFoodList()
            except: msg.showwarning(title="Data invalid",message="Please enter a name and a valid number for the calories!")
        else: msg.showwarning(title="No date selected",message="You haven't selected a date to edit!")

    #Handle deletion for a food entry on the selected date
    def removeFood(self):
        selected_items = self.foodListTree.selection()
        if len(selected_items) > 0:
            for food in selected_items:
                values = self.foodListTree.item(food)["values"]
                try:
                    self.master.db.deleteFood(values[0],values[1],values[2])
                    self.foodListTree.delete(food)
                except: print("Error in deleting food from DB")
        else: self.displayLabelMessage("Select a food on the list to remove")

    #Cler the current selection
    def clearList(self):
        self.labelDateSelected.configure(text="")
        self.foodListTree.delete(*self.foodListTree.get_children()) #Clear the list
        self.labelTotalCalories.configure(text="")

    #Show a small label message on the center frame
    def displayLabelMessage(self,message):
        self.labelMessage.configure(text=message)
        #self.after(2000,self.labelMessage.configure(text=""))