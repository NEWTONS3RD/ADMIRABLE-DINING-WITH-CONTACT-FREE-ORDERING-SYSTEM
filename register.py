from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import pymysql
def login_window():
root.destroy()
def clear():
entryemail.delete(0, END)
entrycontact.delete(0, END)
entrypassword.delete(0, END)
entryconfirmpassword.delete(0, END)
entryfirstname.delete(0, END)
entrylastname.delete(0, END)
entryanswer.delete(0, END)
comboquestion.current(0)
check.set(0)
def register():
if entryfirstname.get() == '' or entrylastname.get() == '' or entryemail.get() == '' or
entrycontact.get() == '' or \
entrypassword.get() == '' or entryconfirmpassword.get() == '' or comboquestion.get() ==
'Select' or entryanswer.get() == '':
showerror('Error', "All Fields Are Required", parent=root)
elif entrypassword.get() != entryconfirmpassword.get():
showerror('Error', "Password Mismatch", parent=root)
elif check.get() == 0:
showerror('Error', "Please Agree To Our Terms & Conditions", parent=root)
else:
try:
con = pymysql.connect(host='localhost', user='root', password='1305', database='register')
cur = con.cursor()
cur.execute('select * from student where email=%s', entryemail.get())
row = cur.fetchone()
if row != None:
showerror('Error', "User Already Exists", parent=root)
else:
cur.execute(
'insert into student (f_name,l_name,email,contact,question,answer,password)
values(%s,%s,%s,%s,%s,%s,%s)',
(entryfirstname.get(), entrylastname.get(), entryemail.get(), entrycontact.get(),
comboquestion.get(),
entryanswer.get(), entrypassword.get()))
con.commit()
con.close()
showinfo('Success', "Registration Successful", parent=root)
clear()
root.destroy()
import login
except Exception as e:
showerror('Error', f"Error due to: {e}", parent=root)
root = Tk()
root.geometry('1350x710+0+10')
root.title('Registration Form')
bg = PhotoImage(file='bg.png')
bgLabel = Label(root, image=bg)
bgLabel.place(x=0, y=0)
registerFrame = Frame(root, bg='white', width=650, height=650)
registerFrame.place(x=630, y=30)
titleLabel = Label(registerFrame, text='Registration Form', font=('arial', 22, 'bold '), bg='white',fg='deep pink', )

titleLabel.place(x=200, y=5)
firstnameLabel = Label(registerFrame, text='First Name', font=('times new roman', 18, 'bold'),bg='white',fg='gray20', )


firstnameLabel.place(x=20, y=80)
entryfirstname = Entry(registerFrame, font=('times new roman', 18), bg='lightgray')
entryfirstname.place(x=20, y=115, width=250)
lastnameLabel = Label(registerFrame, text='Last Name', font=('times new roman', 18, 'bold'),bg='white',fg='gray20', )

lastnameLabel.place(x=370, y=80)
entrylastname = Entry(registerFrame, font=('times new roman', 18), bg='lightgray')
entrylastname.place(x=370, y=115, width=250)
contactLabel = Label(registerFrame, text='Contact Number', font=('times new roman', 18, 'bold'),bg='white',fg='gray20', )

contactLabel.place(x=20, y=200)
entrycontact = Entry(registerFrame, font=('times new roman', 18), bg='lightgray')
entrycontact.place(x=20, y=235, width=250)
emailLabel = Label(registerFrame, text='Email', font=('times new roman', 18, 'bold'), bg='white',fg='gray20', )

emailLabel.place(x=370, y=200)
entryemail = Entry(registerFrame, font=('times new roman', 18), bg='lightgray')
entryemail.place(x=370, y=235, width=250)
questionLabel = Label(registerFrame, text='Security Question', font=('times new roman',18,'bold'), bg='white',fg='gray20', )
questionLabel.place(x=20, y=320)
comboquestion = ttk.Combobox(registerFrame, font=('times new roman', 16), state='readonly',justify=CENTER)

comboquestion['values'] = ('Select', 'Your First Pet Name?', 'Your Birth Place Name?', 'Your BestFriend Name?','Your Favourite Teacher?', 'Your Favourite Hobby?')


comboquestion.place(x=20, y=355, width=250)
comboquestion.current(0)
answerLabel = Label(registerFrame, text='Answer', font=('times new roman', 18, 'bold'),bg='white',fg='gray20', )


answerLabel.place(x=370, y=320)
entryanswer = Entry(registerFrame, font=('times new roman', 18), bg='lightgray')
entryanswer.place(x=370, y=355, width=250)
passwordLabel = Label(registerFrame, text='Password', font=('times new roman', 18, 'bold'),bg='white',fg='gray20', )


passwordLabel.place(x=20, y=440)
entrypassword = Entry(registerFrame, font=('times new roman', 18), bg='lightgray')
entrypassword.place(x=20, y=475, width=250)
confirmpasswordLabel = Label(registerFrame, text='Confirm Password', font=('times new roman',18, 'bold'),bg='white',fg='gray20', )



confirmpasswordLabel.place(x=370, y=440)
entryconfirmpassword = Entry(registerFrame, font=('times new roman', 18), bg='lightgray')
entryconfirmpassword.place(x=370, y=475, width=250)
check = IntVar()
checkButton = Checkbutton(registerFrame, text='I Agree All The Terms & Conditions',variable=check, onvalue=1,offvalue=0, font=('times new roman', 14, 'bold'), bg='white')


checkButton.place(x=20, y=530)
button = PhotoImage(file='button.png')
registerbutton = Button(registerFrame, image=button, bd=0, cursor='hand2', bg='white',activebackground='white', activeforeground='white', command=register)


registerbutton.place(x=250, y=580)
loginimage = PhotoImage(file='login.png')
loginbutton1 = Button(root, image=loginimage, bd=0, cursor='hand2', bg='gold',activebackground='gold',activeforeground='gold')

loginbutton1.place(x=240, y=330)
root.mainloop()

