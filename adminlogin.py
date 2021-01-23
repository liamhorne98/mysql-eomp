from tkinter import messagebox
import pymysql
import tkinter
import tkinter as tk
mydb= pymysql.connect(user='root', password='',host='127.0.0.1',database='LifechoicesOnline')
mycursor=mydb.cursor()


window= tk.Tk()
window.title("Login page")
window.geometry("450x450")
window.configure(background="red")



def verify():
            user_verify = username.get()
            pass_verify= password.get()
            sql= "select * from admin where username = %s and password = %s"
            mycursor.execute(sql, [(user_verify), (pass_verify)])
            results = mycursor.fetchall()
            if results:
                import admin
                admin
            else:
                messagebox.showerror('error','incorrect login details')

lbuse = tk.Label(window, text="Username")
lbuse.place(x=50, y=20)

username = tk.Entry(window, width=35)
username.place(x=250, y=20, width=100)

lbpass = tk.Label(window, text="Password")
lbpass.place(x=50, y=50)

password = tk.Entry(window, width=35)
password.place(x=250, y=50, width=100)


logbtn= tk.Button(window, text="Login", bg="white", command=verify)
logbtn.place(x=50, y=135, width=55)

logout= tk.Button(window, text="Login", bg="white", command=verify)
logout.place(x=50, y=135, width=55)








window.mainloop()
