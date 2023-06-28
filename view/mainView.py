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
        today = datetime.date.today()
        labelDate = ctk.CTkLabel(self.leftFrame,text="Date:")
        labelDate.grid(row=0,column=0,padx=5)
        inputDay = ctk.CTkLabel(self.leftFrame,text=today.day)
        inputDay.grid(row=0,column=1,padx=5)
        inputMonth = ctk.CTkLabel(self.leftFrame,text=today.month)
        inputMonth.grid(row=0,column=2,padx=5)
        inputYear = ctk.CTkLabel(self.leftFrame,text=today.year)
        inputYear.grid(row=0,column=3,padx=5)
        btnAddDate = ctk.CTkButton(self.leftFrame,text="Register today",command=lambda: master.db.insertDate(inputDay.cget("text"),inputMonth.cget("text"),inputYear.cget("text")))
        btnAddDate.grid(row=0,column=4,padx=5)
        self.dateListFrame = ctk.CTkFrame(self.leftFrame)
        self.dateListFrame.grid(row=1,column=0,columnspan=4)

        centerFrame = ctk.CTkFrame(self)
        centerFrame.grid(row=1,column=1,padx=10)
        label1 = ctk.CTkLabel(centerFrame,text="Food name:",font=self.fontMedium)
        label1.grid(row=0,column=0,padx=5,pady=5)
        input1 = ctk.CTkEntry(centerFrame,font=self.fontMedium)
        input1.grid(row=0,column=1,padx=5,pady=5)
        label2 = ctk.CTkLabel(centerFrame,text="Calories:",font=self.fontMedium)
        label2.grid(row=1,column=0,padx=5,pady=5)
        input2 = ctk.CTkEntry(centerFrame,font=self.fontMedium)
        input2.grid(row=1,column=1,padx=5,pady=5)
        btnAdd = ctk.CTkButton(centerFrame,text=">> Add >>",font=self.fontMedium)
        btnAdd.grid(row=2,columnspan=2,padx=15,pady=5)

        rightFrame = ctk.CTkScrollableFrame(self)
        rightFrame.grid(row=1,column=2,padx=10)

        footerFrame = ctk.CTkFrame(self)
        footerFrame.grid(row=2,column=0,columnspan=3,sticky="ew")
        labelFooter = ctk.CTkLabel(footerFrame,text="Made by David Santos")
        labelFooter.pack()

    