
import pymysql.cursors
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from datetime import *
mydb= pymysql.connect(user='root', password='',host='127.0.0.1',database='LifechoicesOnline')
mycursor=mydb.cursor()


window= tk.Tk()
window.title("Login page")
window.geometry("450x450")
window.configure(background="red")
date = datetime.now






def verify():
    user_verify = username.get()
    pass_verify= password.get()
    sql= "select * from users where username = %s and password = %s"
    mycursor.execute(sql, [(user_verify), (pass_verify)])
    results = mycursor.fetchall()
    if results:
        messagebox.showinfo('Message', 'Logged in successfully')


        root = Tk()
        root.title("Sign-out")
        root.geometry("350x200")
        signIn = datetime.now()
        x = signIn.strftime("%H:%M:%S")

        def signout():
            timeout = datetime.now()

            y = timeout.strftime("%H:%M:%S")
            z = username.get()

            timeInfo = z, x, y

            timeComm = "INSERT INTO sign_register(username, sign_in, sign_out) VALUES(%s, %s, %s)"

            mycursor.execute(timeComm, timeInfo)

            mydb.commit()
            messagebox.showinfo('Message', 'Signed out!')
            root.destroy()

        outbtn = Button(root, command=signout, text="Sign out when ready")
        outbtn.place(x=10, y=10)

    else:
        messagebox.showinfo("message", "wrong login")

lbuse = tk.Label(window, text="Username")
lbuse.place(x=50, y=20)

username = tk.Entry(window, width=35)
username.place(x=250, y=20, width=100)

lbpass = tk.Label(window, text="Password")
lbpass.place(x=50, y=50)

password = tk.Entry(window, width=35)
password.place(x=250, y=50, width=100)

lnum = tk.Label(window, text="Mobile-Number")
lnum.place(x=50, y=80)

numb = tk.Entry(window, width=35)
numb.place(x=250, y=80, width=100)

logbtn= tk.Button(window, text="Login", bg="white", command=verify)
logbtn.place(x=50, y=135, width=55)

logout= tk.Button(window, text="Login", bg="white", command=verify)
logout.place(x=50, y=135, width=55)


def close():
    ext = messagebox.askyesno(title="?", message="are you sure, you want to exit?")
    if ext == True:
        window.destroy()
    else:
        return None




#exit button
exitbtn = Button(window, command=close, text="exit")
exitbtn.place(x=120, y=135)

tk.mainloop()


