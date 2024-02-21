from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql

#Functionality

def clear():
    emailEntry.delete(0,END)
    usernameEntry.delete(0,END)
    passwordEntry.delete(0,END)
    confirmEntry.delete(0,END)
    check.set(0)

def connect_database():
    if emailEntry.get()=='' or usernameEntry.get()=='' or passwordEntry.get()=='' or confirmEntry.get()=='':
        messagebox.showerror('Error','All fields are required')
    elif passwordEntry.get()!=confirmEntry.get():
        messagebox.showerror('Error','Password Mismatch')
    elif check.get()==0:
        messagebox.showerror('Error','Please accept terms and conditons')
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='Sonu123#12')  
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Database connectivity issue. Try again')
            return
        try:  
            query='create database userdata'
            mycursor.execute(query)  
            query='use userdata'
            mycursor.execute(query)  
            query='create table data(id int auto_increment primary key not null,email varchar(50),username varchar(100),password varchar(20))'
            mycursor.execute(query) 
        except:  
            mycursor.execute('use userdata')
        
        query='select * from data where username=%s'
        mycursor.execute(query,(usernameEntry.get()))
        
        row=mycursor.fetchone()
        if row!=None:  
            messagebox.showerror('Error','Username already exists')
        else:
            query='insert into data(email,username,password) values(%s,%s,%s)' 
            mycursor.execute(query,(emailEntry.get(),usernameEntry.get(),passwordEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success','Registration is successfull')
            clear()
            signup_window.destroy()
            import signin

def login_page():
    signup_window.destroy()  
    import signin  

#GUI
    
signup_window=Tk()
signup_window.geometry('990x660+250+50')
signup_window.title('Signup Page')
signup_window.resizable(0,0)

background=ImageTk.PhotoImage(file='Frame 4.png') #If we have jpg image then use ImageTk, otherwise only PhotoImage is required.
bgLabel=Label(signup_window,image=background)
bgLabel.grid()

frame=Frame(signup_window,width=50,height=20,bg='#0F1D5B')
frame.place(x=554,y=100)

heading=Label(frame,text='CREATE AN ACCOUNT',font=('Outfit',18,'bold'),bg='#0F1D5B',fg='white')
heading.grid(row=0,column=0,padx=10,pady=10)

emailLabel=Label(frame,text='Email',font=('Outfit',13,'bold'),bg='#0F1D5B',fg='white')
emailLabel.grid(row=1,column=0,sticky='w',padx=25,pady=(10,0))  #sticky aligns it and w means west i.e., right
emailEntry=Entry(frame,width=25,font=('Outfit',10,'bold'),bg='white',fg='black')
emailEntry.grid(row=2,column=0,sticky='w',padx=25)

usernameLabel=Label(frame,text='Username',font=('Outfit',13,'bold'),bg='#0F1D5B',fg='white')
usernameLabel.grid(row=3,column=0,sticky='w',padx=25,pady=(10,0))  #pady is in form of tuple where top and bottom spacing are separated with comma
usernameEntry=Entry(frame,width=25,font=('Outfit',10,'bold'),bg='white',fg='black')
usernameEntry.grid(row=4,column=0,sticky='w',padx=25)

passwordLabel=Label(frame,text='Password',font=('Outfit',13,'bold'),bg='#0F1D5B',fg='white')
passwordLabel.grid(row=5,column=0,sticky='w',padx=25,pady=(10,0))
passwordEntry=Entry(frame,width=25,font=('Outfit',10,'bold'),bg='white',fg='black')
passwordEntry.grid(row=6,column=0,sticky='w',padx=25)

confirmLabel=Label(frame,text='Confirm Password',font=('Outfit',13,'bold'),bg='#0F1D5B',fg='white')
confirmLabel.grid(row=7,column=0,sticky='w',padx=25,pady=(10,0))
confirmEntry=Entry(frame,width=25,font=('Outfit',10,'bold'),bg='white',fg='black')
confirmEntry.grid(row=8,column=0,sticky='w',padx=25)

check=IntVar()
tandc=Checkbutton(frame,text="I agree to the terms and conditions",font=('Outfit',9),bg='#0F1D5B',fg='white',activebackground='#0F1D5B',selectcolor='#042741',cursor='hand2',variable=check)  #variable=check will return the value 1 or 0 to check variable
tandc.grid(row=9,column=0,pady=10,padx=15)

signupButton=Button(frame,text='Signup',font=('Outfit',16,'bold'),bd=0,bg='white',fg='#0F1D5B',activebackground='black',activeforeground='white',width=17,command=connect_database)
signupButton.grid(row=10,column=0,pady=10)

alreadyLabel=Label(frame,text='Already have an account?',font=('Outfit',9,'bold'),bg='#0F1D5B',fg='white')
alreadyLabel.grid(row=11,column=0,sticky='w',padx=35,pady=10)
loginButton=Button(frame,text='Login',font=('Outfit',9,'bold'),fg='light blue',bg='#0F1D5B',activebackground='#0F1D5B',activeforeground='light blue',cursor='hand2',bd=0,command=login_page)
loginButton.place(x=192,y=400)

signup_window.mainloop()