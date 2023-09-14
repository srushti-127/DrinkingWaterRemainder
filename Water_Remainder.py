from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import time
from plyer import notification
from threading import *

class Student:

    def __init__(self, root):
        # ==> Main Body of Root and Title <==
        self.root = root
        self.flag = False
        self.flag_another = False
        self.Sub = False
        self.Name = ""
        self.Weight = 0
        self.sugar_level = 0
        self.kidney_stones = ''
        self.uti = ""
        self.root.title("Water Reminder System")
        self.root.geometry("500x500+0+0")
        self.root.resizable(0, 0)
        root.wm_iconbitmap('.\water.ico')
        title = Label(self.root, text="Welcome to Water Reminder !!", bd=10, relief=SOLID,
                      font=("Times New Roman", 25, "bold"), bg="#404040", fg="White")
        title.pack(side=TOP, fill=X)

        Management_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="#333945")
        Management_Frame.place(x=20, y=85, width=455, height=388)

        m_title = Label(Management_Frame, text='"Drink Water to keep your body fit & hydrated !!"',
                        font=("Times New Roman", 15, "bold"), bg="#758AA2", fg="black")
        m_title.grid(row=0, column=0, pady=0, padx=2)

        # ====> Button Section <====
        #Label(Management_Frame, text="Click on This Button", font=("Arial", 10, "bold"),
             # bg="#333945", fg="white").grid(row=1, column=0)

        Submit_btn = Button(Management_Frame, command=self.SubmitBTN, text="Enter Name and Weight", width=20, bd=4,
                            relief=SOLID, font=("Arial", 12, "bold"), bg="#ff9933", fg="Black")
        Submit_btn.grid(row=4, column=0, pady=10, padx=45)

        Sugar_btn = Button(Management_Frame, command=self.SugarBtn, text="Enter the sugar level", width=20, bd=4,
                            relief=SOLID, font=("Arial", 12, "bold"), bg="#ff9933", fg="Black")
        Sugar_btn.grid(row=5, column=0, pady=5, padx=15)

        kidney_stone_btn = Button(Management_Frame, command=self.KidneyStoneBtn, text="Enter whether you have kidney stone or not", width=40, bd=4,
                           relief=SOLID, font=("Arial", 12, "bold"), bg="#ff9933", fg="Black")
        kidney_stone_btn.grid(row=6, column=0, pady=5, padx=15)

        UTI_btn = Button(Management_Frame, command=self.UTIBtn, text="Enter whether you have Urinary tract infection  or not", width=40, bd=4,
                     relief=SOLID, font=("Arial", 12, "bold"), bg="#ff9933", fg="Black")
        UTI_btn.grid(row=7, column=0, pady=5, padx=15)



        Start_Reminder = Button(Management_Frame, command=self.StartBTN, text="Start Reminder", width=20, bd=4,
                                relief=SOLID, font=("Arial", 17, "bold"), bg="#ff9933", fg="Black")
        Start_Reminder.grid(row=8, column=0, pady=10, padx=45)

        Stop_Reminder = Button(Management_Frame, command=self.StopBTN, text="Stop Reminder", width=20, bd=4,
                               relief=SOLID, font=("Arial", 17, "bold"), bg="#ff9933", fg="Black")
        Stop_Reminder.grid(row=9, column=0, pady=10, padx=45)

    def SubmitBTN(self):
        try:
            self.Name = simpledialog.askstring("Enter Name", "What is your Name?")
        except ValueError:
            messagebox.showerror("Error", "Name Must be Text")
        try:
            self.Weight = int(simpledialog.askstring("Enter Weight", "What is your Weight?"))
        except ValueError:
            messagebox.showerror("Error", "Weight Must be Value")

        if self.Name == "" or self.Name == " ":
            messagebox.showerror("Invalid Name", " Invalid Name, Please Enter Again !!!")
            self.Name = ""
        elif self.Weight <= 0 or self.Weight == " " or len(str(self.Weight)) == 0:
            messagebox.showerror("Invalid Weight", " Invalid Weight, Please Enter Again !!!")
            self.Weight = 0
        else:
            Final_Name = "Your Name is " + self.Name + ", And Weight " + str(self.Weight) + ", Right?"
            messagebox.showinfo("Conformation", Final_Name)

    def SugarBtn(self):
        try:
            self.sugar_level = int(simpledialog.askstring("Enter sugar level", "What is your sugar level?"))
        except ValueError:
            messagebox.showerror("Error", "Sugar level Must be Value")

        if self.sugar_level <= 0 or self.sugar_level == " " or len(str(self.sugar_level)) == 0:
            messagebox.showerror("Invalid sugar_level", " Invalid sugar_level, Please Enter Again !!!")
            self.sugar_level = 0
        else:
            Final_display = " Your sugar level is " + str(self.sugar_level) + ", Right?"
            messagebox.showinfo("Conformation", Final_display)

    def KidneyStoneBtn(self):
        try:
            self.kidney_stones = simpledialog.askstring("Enter whether you have kidney stone or not", "Do u have/had kidney stones?(answer with Yes/No)")
        except ValueError:
            messagebox.showerror("Error", "Answer Must be string")

        if self.kidney_stones == " " or len(str(self.kidney_stones)) == 0:
            messagebox.showerror("Invalid answer", " Invalid Answer, Please Enter Again !!!")
            self.kidney_stones = ''
        else:
            Final_display1 = " Your answer is " + self.kidney_stones + " for kidney stones, Right?"
            messagebox.showinfo("Conformation", Final_display1)


    def UTIBtn(self):
        try:
            self.uti = simpledialog.askstring("Enter whether you have Urinary tract infection or not", "Do u have/had Urinary tract infection?(answer with Yes/No)")
        except ValueError:
            messagebox.showerror("Error", "Answer Must be string")

        if self.uti == " " or len(str(self.uti)) == 0:
            messagebox.showerror("Invalid answer", " Invalid Answer, Please Enter Again !!!")
            self.uti = ''
        else:
            Final_display2 = " Your answer is " + self.uti + "  for Urinary tract infection, Right?"
            messagebox.showinfo("Conformation", Final_display2)



    def StopBTN(self):
        self.flag = False

    def StartBTN(self):

        if self.Name == "":
            self.flag_another = False
            messagebox.showerror("Something went Wrong ",
                                 "Please Provide Details Click on Name And Weight Button !!!")
        elif self.Weight == 0:
            self.flag_another = False
            messagebox.showerror("Something went Wrong ", "Please Provide Details on Weight!!!")

        elif self.sugar_level == 0:
            self.flag_another = False
            messagebox.showerror("Something went Wrong ", "Please Provide Details on sugar level Button !!!")

        elif self.kidney_stones == 0:
            self.flag_another = False
            messagebox.showerror("Something went Wrong ", "Please Provide Details on kidney stones Button !!!")

        elif self.uti == 0:
            self.flag_another = False
            messagebox.showerror("Something went Wrong ", "Please Provide Details on urinary tract infection Button !!!")

        else:
            if self.flag == False:
                self.flag = True
                thread = Thread(target=self.StartNotify)
                thread.start()
            elif self.flag_another == False:
                messagebox.showerror("Something went Wrong ",
                                     "Please Provide Details !!!")
            else:
                messagebox.showwarning("Activated", "Notification Already Activated")

    def StartNotify(self):

        if __name__ == "__main__":
            self.flag_another = True
            while self.flag:

                if self.sugar_level < 70:
                    notification.notify(
                        title="Hey " + self.Name + ", Please Drink A 50ml Water Now !!",
                        message="Now, It's time to drink Water because It's Require as per your Health...",
                        app_icon=".\water.ico",
                        timeout=3
                    )
                elif self.sugar_level >= 70 and self.sugar_level <= 100:
                    notification.notify(
                        title="Hey " + self.Name + ", Please Drink A 120ml Water Now !!",
                        message="Now, It's time to drink Water because It's Require as per your Health...",
                        app_icon=".\water.ico",
                        timeout=3
                    )

                elif self.sugar_level >= 101 and self.sugar_level <= 125 or self.uti == "Yes" or self.kidney_stones == "Yes":
                    notification.notify(
                        title="Hey " + self.Name + ", Please Drink A 200ml Water Now !!",
                        message="Now, It's time to drink Water because It's Require as per your Health...",
                        app_icon=".\water.ico",
                        timeout=3
                    )
                else:
                    notification.notify(
                        title="Hey " + self.Name + ", Please Drink A 300ml Water Now !!",
                        message="Now, It's time to drink Water because It's Require as per your Health...",
                        app_icon=".\water.ico",
                        timeout=3
                    )

                if self.sugar_level < 70:
                    if self.Weight <= 30:
                        time.sleep(90 * 60)
                    elif self.Weight <= 40:
                        time.sleep(80*60)
                    elif self.Weight <= 50:
                        time.sleep(75 * 60)
                    elif self.Weight <= 60:
                        time.sleep(70 * 60)
                    elif self.Weight <= 70:
                        time.sleep(60 * 60)
                    elif self.Weight <= 80:
                        time.sleep(48 * 60)
                    elif self.Weight <= 90:
                        time.sleep(42 * 60)
                    elif self.Weight > 90:
                        time.sleep(40 * 60)
                    else:
                        time.sleep(39 * 60)

                elif self.sugar_level >= 70 and self.sugar_level <= 100:
                    if self.Weight <= 30:
                        time.sleep(90 * 60)
                    elif self.Weight <= 40:
                        time.sleep(80*60)
                    elif self.Weight <= 50:
                        time.sleep(75 * 60)
                    elif self.Weight <= 60:
                        time.sleep(70 * 60)
                    elif self.Weight <= 70:
                        time.sleep(60 * 60)
                    elif self.Weight <= 80:
                        time.sleep(48 * 60)
                    elif self.Weight <= 90:
                        time.sleep(42 * 60)
                    elif self.Weight > 90:
                        time.sleep(40 * 60)
                    else:
                        time.sleep(39 * 60)

                elif self.sugar_level >= 101 and self.sugar_level <= 125 or self.uti == "Yes" or self.kidney_stones == "Yes":
                    if self.Weight <= 30:
                        time.sleep(90 * 60)
                    elif self.Weight <= 40:
                        time.sleep(80*60)
                    elif self.Weight <= 50:
                        time.sleep(75 * 60)
                    elif self.Weight <= 60:
                        time.sleep(70 * 60)
                    elif self.Weight <= 70:
                        time.sleep(60 * 60)
                    elif self.Weight <= 80:
                        time.sleep(48 * 60)
                    elif self.Weight <= 90:
                        time.sleep(42 * 60)
                    elif self.Weight > 90:
                        time.sleep(40 * 60)
                    else:
                        time.sleep(39 * 60)

                else:
                    if self.Weight <= 30:
                        time.sleep(90 * 60)
                    elif self.Weight <= 40:
                        time.sleep(80*60)
                    elif self.Weight <= 50:
                        time.sleep(75 * 60)
                    elif self.Weight <= 60:
                        time.sleep(70 * 60)
                    elif self.Weight <= 70:
                        time.sleep(60 * 60)
                    elif self.Weight <= 80:
                        time.sleep(48 * 60)
                    elif self.Weight <= 90:
                        time.sleep(42 * 60)
                    elif self.Weight > 90:
                        time.sleep(40 * 60)
                    else:
                        time.sleep(39 * 60)

root = Tk()
ob = Student(root)
root.mainloop()