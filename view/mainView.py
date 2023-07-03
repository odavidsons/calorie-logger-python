"""
Author: David Santos
Repository: https://github.com/odavidsons/calorie-logger-python
Year: 2023

File imported by calorieLogger.py. Renders all of the widgets belonging to the main app frame. Also has the controller functions for the main frame.
"""
import customtkinter as ctk
import datetime
from tkinter import messagebox as msg
from tkinter.ttk import Treeview
from tkinter import END
import CTkListbox
#Import app views
from view.settings import settings
from view.export import export
from view.chart import chart

class mainView(ctk.CTkFrame):

    fontLarge = ('default',18,'bold')
    fontMedium = ('default',14)

    def __init__(self,master):
        super().__init__(master)

        #Top menu frame
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

        #Left list frame
        self.leftFrame = ctk.CTkFrame(self)
        self.leftFrame.grid(row=1,column=0,padx=10,pady=15,sticky="ns")
        self.today = datetime.date.today()
        labelDate = ctk.CTkLabel(self.leftFrame,text="Date:")
        labelDate.grid(row=0,column=0,padx=5)
        self.labelCurrentDate = ctk.CTkLabel(self.leftFrame,text=f"{self.today.day}/{self.today.month}/{self.today.year}")
        self.labelCurrentDate.grid(row=0,column=1,padx=5)
        self.btnAddDate = ctk.CTkButton(self.leftFrame,text="Register today",command=self.addDate)
        self.btnAddDate.grid(row=0,column=2,padx=5,pady=5)
        self.dateListBox = CTkListbox.CTkListbox(self.leftFrame)
        self.dateListBox.grid(row=1,columnspan=3,padx=5,pady=5)
        btnSelectDate = ctk.CTkButton(self.leftFrame,text=">> Select Date >>",font=self.fontMedium,command=self.selectDate)
        btnSelectDate.grid(row=2,columnspan=3,padx=10,pady=5)
        btnRemoveDate = ctk.CTkButton(self.leftFrame,text="Remove date",font=self.fontMedium,fg_color="#c21717",hover_color="#9e1919",command=self.removeDate)
        btnRemoveDate.grid(row=3,columnspan=3,padx=10,pady=5)

        #Center options frame
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
        label3 = ctk.CTkLabel(centerFrame,text="Carbs:",font=self.fontMedium)
        label3.grid(row=2,column=0,padx=5,pady=5)
        self.inputCarbs = ctk.CTkEntry(centerFrame,font=self.fontMedium)
        self.inputCarbs.grid(row=2,column=1,padx=5,pady=5)
        label4 = ctk.CTkLabel(centerFrame,text="Proteins:",font=self.fontMedium)
        label4.grid(row=3,column=0,padx=5,pady=5)
        self.inputProteins = ctk.CTkEntry(centerFrame,font=self.fontMedium)
        self.inputProteins.grid(row=3,column=1,padx=5,pady=5)
        label5 = ctk.CTkLabel(centerFrame,text="Fats:",font=self.fontMedium)
        label5.grid(row=4,column=0,padx=5,pady=5)
        self.inputFats = ctk.CTkEntry(centerFrame,font=self.fontMedium)
        self.inputFats.grid(row=4,column=1,padx=5,pady=5)
        btnAdd = ctk.CTkButton(centerFrame,text=">> Add >>",font=self.fontMedium,command=self.addFood)
        btnAdd.grid(row=5,columnspan=2,padx=15,pady=5)
        self.btnRemove = ctk.CTkButton(centerFrame,text="<< Remove <<",font=self.fontMedium,fg_color="#c21717",hover_color="#9e1919",command=self.removeFood)
        self.btnRemove.grid(row=6,columnspan=2,padx=15,pady=5)
        self.labelMessage = ctk.CTkLabel(centerFrame,text="")
        self.labelMessage.grid(row=7,columnspan=2,pady=5)

        #Right list frame
        rightFrame = ctk.CTkFrame(self)
        rightFrame.grid(row=1,column=2,padx=10,pady=15)
        labelDate1 = ctk.CTkLabel(rightFrame,text="Date:")
        labelDate1.grid(row=0,column=0,padx=5)
        self.labelDateSelected = ctk.CTkLabel(rightFrame,text="")
        self.labelDateSelected.grid(row=0,column=1,padx=5)
        self.btnclearSelection = ctk.CTkButton(rightFrame,text="Clear Selection",command=self.clearSelection)
        self.btnclearSelection.grid(row=0,column=2,padx=5,pady=5)
        self.foodListTree = Treeview(rightFrame,columns=("date_id","name","calories","carbs","proteins","fats"),show='headings')
        self.foodListTree.grid(row=1,column=0,columnspan=3,padx=10,pady=15,sticky="nsew")
        self.foodListTree.heading("name",text="Food")
        self.foodListTree.column("name", minwidth=80, width=80, stretch=ctk.YES)
        self.foodListTree.heading("calories",text="Calories")
        self.foodListTree.column("calories", minwidth=80, width=80, stretch=ctk.YES)
        self.foodListTree.heading("carbs",text="Carbs")
        self.foodListTree.column("carbs", minwidth=80, width=80, stretch=ctk.YES)
        self.foodListTree.heading("proteins",text="Proteins")
        self.foodListTree.column("proteins", minwidth=80, width=80, stretch=ctk.YES)
        self.foodListTree.heading("fats",text="Fats")
        self.foodListTree.column("fats", minwidth=80, width=80, stretch=ctk.YES)
        self.foodListTree["displaycolumns"]=("name", "calories","carbs","proteins","fats")

        self.selectedStatsFrame = ctk.CTkFrame(rightFrame)
        self.selectedStatsFrame.grid(row=2,columnspan=3,padx=10,pady=5,sticky="ew")
        labelTitle1 = ctk.CTkLabel(self.selectedStatsFrame,text="Total Macros",font=self.fontMedium)
        labelTitle1.grid(row=0,columnspan=4,padx=5)
        labelTotal = ctk.CTkLabel(self.selectedStatsFrame,text="Calories")
        labelTotal.grid(row=1,column=0,padx=5)
        labelCarbs = ctk.CTkLabel(self.selectedStatsFrame,text="Carbs")
        labelCarbs.grid(row=1,column=1,padx=5)
        labelProteins = ctk.CTkLabel(self.selectedStatsFrame,text="Protein")
        labelProteins.grid(row=1,column=2,padx=5)
        labelFats = ctk.CTkLabel(self.selectedStatsFrame,text="Fats")
        labelFats.grid(row=1,column=3,padx=5)
        self.labelTotalCalories = ctk.CTkLabel(self.selectedStatsFrame,text="")
        self.labelTotalCalories.grid(row=2,column=0,padx=5)
        self.labelTotalCarbs = ctk.CTkLabel(self.selectedStatsFrame,text="")
        self.labelTotalCarbs.grid(row=2,column=1,padx=5)
        self.labelTotalProteins = ctk.CTkLabel(self.selectedStatsFrame,text="")
        self.labelTotalProteins.grid(row=2,column=2,padx=5)
        self.labelTotalFats = ctk.CTkLabel(self.selectedStatsFrame,text="")
        self.labelTotalFats.grid(row=2,column=3,padx=5)
        btnChart = ctk.CTkButton(self.selectedStatsFrame,text="View chart",command=self.viewChart)
        btnChart.grid(row=3,columnspan=4,padx=10,pady=10)
        self.master.make_dynamic(self.selectedStatsFrame)

        footerFrame = ctk.CTkFrame(self)
        footerFrame.grid(row=3,column=0,columnspan=3,sticky="ew",pady=10)
        labelFooter = ctk.CTkLabel(footerFrame,text="Made by David Santos")
        labelFooter.pack()

    #Fill the date list with all the records from the database
    def fillDateList(self):
        #Clear the listbox
        for i in range(self.dateListBox.size()):
            self.dateListBox.delete(i)
        #Change the state of the register button if the current date already has been inserted
        date = self.labelCurrentDate.cget("text").split("/")
        date_id = self.master.db.getDateId(date[0],date[1],date[2])
        if date_id != None:
            self.btnAddDate.configure(state="disabled",text="Already registered today")
        datelist = self.master.db.getDates()
        row = 0
        for result in datelist:
            date = f"{result[1]}/{result[2]}/{result[3]}"
            self.dateListBox.insert(row,date)
            row = row + 1

    #Fill the food list with all the records from the database
    def fillFoodList(self):
        self.foodListTree.delete(*self.foodListTree.get_children()) #Clear the list
        date = self.labelDateSelected.cget("text").split("/")
        foodlist = self.master.db.getFoodsByDateId(date[0],date[1],date[2])
        row = 0
        calories = 0
        carbs = 0
        proteins = 0
        fats = 0
        for result in foodlist:
            self.foodListTree.insert('',END,values=(result[1],result[2],result[3],result[4],result[5],result[6]))
            row = row + 1
            calories = calories + result[3]
            carbs = carbs + result[4]
            proteins = proteins + result[5]
            fats = fats + result[6]
        self.labelTotalCalories.configure(text=f"{calories}Kcal")
        self.labelTotalCarbs.configure(text=f"{carbs}g")
        self.labelTotalProteins.configure(text=f"{proteins}g")
        self.labelTotalFats.configure(text=f"{fats}g")

    #Handle insertion for a date entry
    def addDate(self):
        date = self.labelCurrentDate.cget("text").split("/")
        self.master.db.insertDate(date[0],date[1],date[2])
        self.fillDateList()

    #Handle insertion for a food entry on the selected date
    def addFood(self):
        if self.labelDateSelected.cget("text") != "":
            date = self.labelDateSelected.cget("text").split("/")
            try: carbs = float(self.inputCarbs.get())
            except: carbs = 0
            try: proteins = float(self.inputProteins.get())
            except: proteins = 0
            try: fats = float(self.inputFats.get())
            except: fats= 0
            try:
                self.master.db.insertFood(date[0],date[1],date[2],self.inputName.get(),float(self.inputCalories.get()),carbs,proteins,fats)
                self.fillFoodList()
            except: msg.showwarning(title="Data invalid",message="Please enter a name and a valid number for the calories!")
        else: msg.showwarning(title="No date selected",message="You haven't selected a date to edit!")

    #Handle deletion for a date entry
    def removeDate(self):
        if self.dateListBox.get() != None:
            confirm = msg.askyesno(title="Remove date",message=f"Are you sure you want to remove this date? ({self.dateListBox.get()})")
            if confirm:
                date = self.dateListBox.get().split("/")
                date_id = self.master.db.getDateId(date[0],date[1],date[2])
                self.master.db.deleteDate(date_id[0])
                self.fillDateList()
        else: print("No date selected")

    #Handle deletion for a food entry on the selected date
    def removeFood(self):
        selected_items = self.foodListTree.selection()
        if len(selected_items) > 0:
            for food in selected_items:
                values = self.foodListTree.item(food)["values"]
                try:
                    self.master.db.deleteFood(values[0],values[1],values[2],values[3],values[4],values[5])
                    self.foodListTree.delete(food)
                    self.clearLabelMessage()
                except: print("Error in deleting food from DB")
        else: self.displayLabelMessage("Select a food on the list to remove")

    #Open a window with a pie chart if there is a date selected
    def viewChart(self):
        if self.labelDateSelected.cget("text") != "":
            carbs = self.labelTotalCarbs.cget("text").split("g")
            proteins = self.labelTotalProteins.cget("text").split("g")
            fats = self.labelTotalFats.cget("text").split("g")
            if carbs[0] != "0" and proteins[0] != "0" and fats[0] != "0":
                chart(carbs[0],proteins[0],fats[0])

    #Handle the date selection
    def selectDate(self):
        if self.dateListBox.get() != None:
            date = self.dateListBox.get().split("/")
            self.labelDateSelected.configure(text=f"{date[0]}/{date[1]}/{date[2]}")
            self.fillFoodList()
        else: print("No date selected")

    #Cler the current selection
    def clearSelection(self):
        self.labelDateSelected.configure(text="")
        self.foodListTree.delete(*self.foodListTree.get_children()) #Clear the list
        self.labelTotalCalories.configure(text="")
        self.labelTotalCarbs.configure(text="")
        self.labelTotalProteins.configure(text="")
        self.labelTotalFats.configure(text="")

    #Show a small label message on the center frame
    def displayLabelMessage(self,message):
        self.labelMessage.configure(text=message)
        #self.after(2000,self.labelMessage.configure(text=""))

    #Clear the text on the message label
    def clearLabelMessage(self):
        self.labelMessage.configure(text="")