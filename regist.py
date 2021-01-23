import pymysql
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

mydb= pymysql.connect(user='root', password='',host='127.0.0.1',database='LifechoicesOnline')
mycursor=mydb.cursor()
def verify():
    try:
        name_verify =name.get()
        user_verify = use.get()
        pass_verify= passw.get()
        mail_verify= email.get()
        num_verify= numb.get()


        sql= "INSERT INTO users (full_name,username,password,email,phone_number) VALUES(%s,%s,%s,%s,%s)"
        val=(name_verify,user_verify,pass_verify,mail_verify,num_verify)
        mycursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo("message","Successfully created")
    except ValueError as e:
        print(e)
        messagebox.showinfo("ERROR","This user already exists")
        window.destroy()

window= Tk()
window.title("Register page")
window.geometry("450x450")
window.configure(background="red")

fname = tk.Label(window, text="Full Name", background="white")
fname.place(x=50, y=20)

name = tk.Entry(window, width=35)
name.place(x=250, y=20, width=100)


user = tk.Label(window, text="Username",background="white")
user.place(x=50, y=50)

use = tk.Entry(window, width=35)
use.place(x=250, y=50, width=100)

lpass = tk.Label(window, text="Password ",background="white")
lpass.place(x=50, y=80)

passw = tk.Entry(window, width=35)
passw.place(x=250, y=80, width=100)


lnum = tk.Label(window, text="Mobile-Number", background="white")
lnum.place(x=50, y=110)

numb = tk.Entry(window, width=35)
numb.place(x=250, y=110, width=100)

lmail=tk.Label(window, text="Email", background="white")
lmail.place(x=50, y=150)

email = tk.Entry(window, width=35)
email.place(x=250, y=150, width=100)


logbtn= tk.Button(window, text="Create User", bg="white", command=verify)
logbtn.place(x=150, y=200, width=100)
tk.mainloop()