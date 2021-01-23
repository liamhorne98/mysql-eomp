from tkinter import *
import pymysql
import tkinter as tk


mydb= pymysql.connect(user='root', password='',host='127.0.0.1',database='LifechoicesOnline')
mycursor=mydb.cursor()


def verify():
    # user_verify = username.get()
    # pass_verify= password.get()
    # sql= "select * from Login where username = %s and password = %s"
    # mycursor.execute(sql, [(user_verify), (pass_verify)])
    # results = mycursor.fetchall()
    if logbtn:
        window.withdraw()
        import login
        login.login()

def admin():
    if adbtn:
        window.withdraw()
        import adminlogin
        adminlogin.adminlogin()

def sign():
    if regbtn:
        window.withdraw()
        import regist
        regist.regist()


window= tk.Tk()
window.title("Login page")
window.geometry("450x250")
window.configure(background="red")

logbtn= tk.Button(window, text="Login", bg="white", command=verify)
logbtn.place(x=100, y=80, width=100)

regbtn=tk.Button(window, text="Register", bg="white", command=sign)
regbtn.place(x=100, y=120, width=100)


adbtn=tk.Button(window, text="Admin", bg="white", command=admin)
adbtn.place(x=100, y=160, width=100)
tk.mainloop()