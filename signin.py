from tkinter import*
from tkinter import messagebox
from PIL import ImageTk  
import pymysql

#Functionality part

def login_user():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','All fields are required')
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password="Sonu123#12")  
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Connection error. Try again')
            return
        query='use userdata'
        mycursor.execute(query)
        query='select * from data where username=%s and password=%s'  
        mycursor.execute(query,(usernameEntry.get(),passwordEntry.get()))
        row=mycursor.fetchone()
        if row == None: 
            messagebox.showerror('Error','Invalid username or password')
        else:
            messagebox.showinfo('Welcome','Login is succesfull')
            login_window.destroy()
            import new
            
def signup_page():
    login_window.destroy()  
    import signup  

def hide():
    openeye.config(file='iconamoon_eye-off-thin.png')
    passwordEntry.config(show='*')  
    eyeButton.config(command=show)  

def show():
    openeye.config(file='vector.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)


def user_enter(event):  
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)

def password_enter(event):  
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)

#GUI part
        
login_window=Tk()
login_window.geometry('990x660+250+50')
login_window.resizable(0,0)  
login_window.title('Login Page')

bgImage=ImageTk.PhotoImage(file='Frame 4.png')
bgLabel=Label(login_window,image=bgImage)
bgLabel.place(x=0, y=0) 

heading=Label(login_window,text='USER LOGIN',font=('Outfit',23,'bold'),bg='#111D5A',fg='white')
heading.place(x=605,y=130)

usernameEntry=Entry(login_window,width=19,font=('Outfit',15),bd=0,fg='black')
usernameEntry.place(x=580,y=210)
usernameEntry.insert(0,'Username')
usernameEntry.bind('<FocusIn>',user_enter)  

frame1=Frame(login_window,width=248,height=2,bg='white')
frame1.place(x=580,y=240)

passwordEntry=Entry(login_window,width=19,font=('Outfit',15),bd=0,fg='black')
passwordEntry.place(x=580,y=270)
passwordEntry.insert(0,'Password')
passwordEntry.bind('<FocusIn>',password_enter)

frame2=Frame(login_window,width=248,height=2,bg='white')
frame2.place(x=580,y=300)

openeye=PhotoImage(file='vector.png')
eyeButton=Button(login_window,image=openeye,bd=0,bg='white',activebackground='white',command=hide,cursor='hand2')  
eyeButton.place(x=800,y=275)

loginButton=Button(login_window,text='Login',font=('Outfit',16,'bold'),fg='black',bg='white',activebackground='black',activeforeground='white',cursor='hand2',bd=0,width=19,command=login_user)
loginButton.place(x=578,y=340)

orLabel=Label(login_window,text='----------OR----------',font=('Outfit',16),bg='#111D5A',fg='white')
orLabel.place(x=583,y=410)

signupLabel=Label(login_window,text='Dont have an account?',font=('Outfit',9,'bold'),bg='#111D5A',fg='white')
signupLabel.place(x=605,y=460)
newaccountButton=Button(login_window,text='Sign up',font=('Outfit',9,'bold'),fg='light blue',bg='#111D5A',activebackground='#111D5A',activeforeground='light blue',cursor='hand2',bd=0,command=signup_page)
newaccountButton.place(x=740,y=460)

login_window.mainloop()