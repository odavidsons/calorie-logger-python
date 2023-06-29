import customtkinter as ctk
import datetime
class mainView(ctk.CTkFrame):

    fontLarge = ('default',18,'bold')
    fontMedium = ('default',14)

    def __init__(self,master):
        super().__init__(master)
        topFrame = ctk.CTkFrame(self)
        topFrame.grid(row=0,column=0,columnspan=3,sticky="ew")
        labelTitle = ctk.CTkLabel(topFrame,text="Calorie logger",font=self.fontLarge)
        labelTitle.pack()
        
        self.leftFrame = ctk.CTkScrollableFrame(self)
        self.leftFrame.grid(row=1,column=0,padx=10)
        self.today = datetime.date.today()
        labelDate = ctk.CTkLabel(self.leftFrame,text="Date:")
        labelDate.grid(row=0,column=0,padx=5)
        self.inputDay = ctk.CTkLabel(self.leftFrame,text=self.today.day)
        self.inputDay.grid(row=0,column=1,padx=5)
        self.inputMonth = ctk.CTkLabel(self.leftFrame,text=self.today.month)
        self.inputMonth.grid(row=0,column=2,padx=5)
        self.inputYear = ctk.CTkLabel(self.leftFrame,text=self.today.year)
        self.inputYear.grid(row=0,column=3,padx=5)
        btnAddDate = ctk.CTkButton(self.leftFrame,text="Register today",command=self.addDate)
        btnAddDate.grid(row=0,column=4,padx=5)
        self.dateListFrame = ctk.CTkFrame(self.leftFrame)
        self.dateListFrame.grid(row=1,column=0,columnspan=5)

        centerFrame = ctk.CTkFrame(self)
        centerFrame.grid(row=1,column=1,padx=10)
        label1 = ctk.CTkLabel(centerFrame,text="Food name:",font=self.fontMedium)
        label1.grid(row=0,column=0,padx=5,pady=5)
        inputName = ctk.CTkEntry(centerFrame,font=self.fontMedium)
        inputName.grid(row=0,column=1,padx=5,pady=5)
        label2 = ctk.CTkLabel(centerFrame,text="Calories:",font=self.fontMedium)
        label2.grid(row=1,column=0,padx=5,pady=5)
        inputCalories = ctk.CTkEntry(centerFrame,font=self.fontMedium)
        inputCalories.grid(row=1,column=1,padx=5,pady=5)
        btnAdd = ctk.CTkButton(centerFrame,text=">> Add >>",font=self.fontMedium,command=lambda: self.addFood(self.today.day,self.today.month,self.today.year,inputName.get(),float(inputCalories.get())))
        btnAdd.grid(row=2,columnspan=2,padx=15,pady=5)

        rightFrame = ctk.CTkScrollableFrame(self)
        rightFrame.grid(row=1,column=2,padx=10)
        labelDate1 = ctk.CTkLabel(rightFrame,text="Date:")
        labelDate1.grid(row=0,column=0,padx=5)
        self.labelDateSelected = ctk.CTkLabel(rightFrame,text="")
        self.labelDateSelected.grid(row=0,column=1,padx=5)
        self.foodListFrame = ctk.CTkFrame(rightFrame)
        self.foodListFrame.grid(row=1,column=0,columnspan=3)

        footerFrame = ctk.CTkFrame(self)
        footerFrame.grid(row=2,column=0,columnspan=3,sticky="ew")
        labelFooter = ctk.CTkLabel(footerFrame,text="Made by David Santos")
        labelFooter.pack()

    #Fill the date list with all the records from the database
    def fillDateList(self):
        datelist = self.master.db.getDates()
        row = 0
        for result in datelist:
            date = f"{result[1]}/{result[2]}/{result[3]}"
            label = ctk.CTkLabel(self.dateListFrame,text=date)
            label.grid(row=row,column=0)
            btn = ctk.CTkButton(self.dateListFrame,text=f"Select",command=self.fillFoodList)
            btn.grid(row=row,column=1)
            row = row + 1


    #Fill the food list with all the records from the database
    def fillFoodList(self):
        self.labelDateSelected.configure(text=f"{self.today.day,self.today.month,self.today.year}")
        foodlist = self.master.db.getFoodsByDateId(self.today.day,self.today.month,self.today.year)
        row = 0
        for result in foodlist:
            food = f"{result[1]} | {result[2]}"
            label = ctk.CTkLabel(self.foodListFrame,text=food)
            label.grid(row=row,column=0)
            btn = ctk.CTkButton(self.foodListFrame,text=f"Remove ({row})")
            btn.grid(row=row,column=1)
            row = row + 1
    
    #Add a date entry
    def addDate(self):
        self.master.db.insertDate(self.inputDay.cget("text"),self.inputMonth.cget("text"),self.inputYear.cget("text"))
        self.fillDateList()

    #Add a food entry to a date
    def addFood(self,day,month,year,name,calories):
        self.master.db.insertFood(day,month,year,name,calories)
        self.fillFoodList()