from tkinter import *
import pymysql
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

mydb= pymysql.connect(user='root', password='',host='127.0.0.1',database='LifechoicesOnline')
mycursor=mydb.cursor()



window= tk.Tk()
window.title("admin page")
window.geometry("1000x1000")
window.configure(background="red")




sql_students = 'SELECT full_name, username, password, email, phone_number FROM users'
mycursor.execute(sql_students)
my_students = mycursor.fetchall()




frm = Frame(window, pady=50)
frm.pack(side=TOP)

scroll = Scrollbar(frm, orient=VERTICAL)
tv = ttk.Treeview(frm, columns=(1,2,3,4,5), show='headings', height='5', yscrollcommand=scroll.set)
scroll.pack(side=RIGHT, fill=Y)
tv.pack()

tv.heading(1, text='name')
tv.heading(2, text='username')
tv.heading(3, text='password')
tv.heading(4, text='email')
tv.heading(5, text='phone number')




for i in my_students:
    tv.insert("", 'end', values=i)













def sheets():
    sql_students = 'SELECT full_name, username, password, email, phone_number FROM users'
    sql_time= 'SELECT username, sign_in, sign_out from sign_register'


    mycursor.execute(sql_time)
    my_students = mycursor.fetchall()

    mycursor.execute(sql_students)
    my_time= mycursor.fetchall()



    frm = Frame(window, pady=50)
    frm.pack(side=TOP)

    scroll = Scrollbar(frm, orient=VERTICAL)
    tv = ttk.Treeview(frm, columns=(1,2,3), show='headings', height='5', yscrollcommand=scroll.set)
    scroll.pack(side=RIGHT, fill=Y)
    tv.pack()

    tv.heading(1, text='username')
    tv.heading(2, text='time in')
    tv.heading(3, text='time out')


    for i in my_students:
        tv.insert("", 'end', values=i)




def delete():
    passs=identity.get()
    mydb = pymysql.connect(user='root', password='', host='127.0.0.1', database='LifechoicesOnline')
    mycursor = mydb.cursor()

    sql= "DELETE FROM users WHERE username =%s"
    user_id= (str(passs),)
    mycursor.execute(sql,user_id)

    mydb.commit()
    messagebox.showinfo("Successful", "You have deleted a user")
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





flbl = tk.Label(window, text="Add user below", background="white")
flbl.pack(side=TOP)

fname = tk.Label(window, text="Full Name", background="white")
fname.pack(side=TOP)

name = tk.Entry(window, width=35)
name.pack(side=TOP)


user = tk.Label(window, text="Username",background="white")
user.pack(side=TOP)

use = tk.Entry(window, width=35)
use.pack(side=TOP)

lpass = tk.Label(window, text="Password ",background="white")
lpass.pack(side=TOP)

passw = tk.Entry(window, width=35)
passw.pack(side=TOP)


lnum = tk.Label(window, text="Mobile-Number", background="white")
lnum.pack(side=TOP)

numb = tk.Entry(window, width=35)
numb.pack(side=TOP)

lmail=tk.Label(window, text="Email", background="white")
lmail.pack(side=TOP)



email = tk.Entry(window, width=35)
email.pack(side=TOP)

logbtn= tk.Button(window, text="Create User", bg="white", command=verify)
logbtn.pack(side=TOP)

dlt = tk.Label(window, text="Delete Users below", background="white")
dlt.pack(side=TOP)

remove = Button(window, text="Remove users by username", background="white",width=40, command=delete)
remove.place(x=100,y=600)
identity = Entry(window, width=45)
identity.place(x=450,y=600)

logbtn= tk.Button(window, text="Check Timesheets", bg="white", command=sheets)
logbtn.pack(side=BOTTOM)



tk.mainloop()