from tkinter import *
from tkinter.ttk import Combobox
import time

win = Tk()
win.state('zoomed')
win.configure(bg='pink')
win.resizable(width=False,height=False)

title=Label(win,text="Banking Automation" ,font=('arial',40,'bold'),bg='pink')
title.pack()

dt=time.strftime("%d-%b-%Y")
date=Label(win,text=f"{dt}" ,font=('arial',20,'bold'),bg='pink')
date.place(relx=.85,rely=.1)


def Main_screen():
    frm=Frame(win)
    frm.configure(bg='powder blue')
    frm.place(relx=.0,rely=.15,relwidth=1,relheight=.85)
    
    def forgotpass():
        frm.destroy()
        forgotpass_screen()
    def newuser():
        frm.destroy()
        newuser_screen()
    def login():
        frm.destroy()
        welcome_screen()
    
    

    lbl_acn=Label(frm,text='ACN',font=('arial',20,'bold'),bg='powder blue')
    lbl_acn.place(relx=.3,rely=.1)
    
    e_acn =Entry(frm,font=('arial',20,'bold'),bd=4)
    e_acn.place(relx=.45 , rely=.1)
    e_acn.focus()
    
    lbl_pass=Label(frm,text='Password',font=('arial',20,'bold'),bg='powder blue')
    lbl_pass.place(relx=.3,rely=.2)
    
    e_pass =Entry(frm,font=('arial',20,'bold'),bd=4,show='*')
    e_pass.place(relx=.45 , rely=.2)

    btn_login = Button(frm,text='Login',font=('arial',16,'bold'),bd=4,command=login)
    btn_login.place(relx=.49,rely=.3)
    
    btn_clear = Button(frm,text='Clear',font=('arial',16,'bold'),bd=4)
    btn_clear.place(relx=.6,rely=.3)
    
    btn_fpass = Button(frm,text='Forgot Password',command=forgotpass,font=('arial',16,'bold'),bd=4)
    btn_fpass.place(relx=.4,rely=.5)
    
    btn_newuser = Button(frm,command=newuser, text='Create new account',font=('arial',16,'bold'),bd=4)
    btn_newuser.place(relx=.61,rely=.5)
    
def forgotpass_screen():
    frm=Frame(win)
    frm.configure(bg='powder blue')
    frm.place(relx=0,rely=.15,relwidth=1,relheight=.85)
    
    def back():
        frm.destroy()
        Main_screen()
        
    btn_new=Button(frm,text='Back',font=('arial',16,'bold'),bd=4,command=back)
    btn_new.place(relx=0,rely=0)
    
    lbl_acn=Label(frm,text='ACN',font=('arial',20,'bold'),bg='powder blue')
    lbl_acn.place(relx=.3,rely=.1)
    
    e_acn =Entry(frm,font=('arial',20,'bold'),bd=4)
    e_acn.place(relx=.45 , rely=.1)
    e_acn.focus()
    
    
    lbl_mail=Label(frm,text='Email',font=('arial',20,'bold'),bg='powder blue')
    lbl_mail.place(relx=.3,rely=.2)
    
    e_mail =Entry(frm,font=('arial',20,'bold'),bd=4,show='*')
    e_mail.place(relx=.45 , rely=.2)
    
    lbl_mob=Label(frm,text='Mobile.no',font=('arial',20,'bold'),bg='powder blue')
    lbl_mob.place(relx=.3,rely=.3)
    
    e_mob =Entry(frm,font=('arial',20,'bold'),bd=4,show='*')
    e_mob.place(relx=.45 , rely=.3)
    
    btn_sub=Button(frm,text='Submit',font=('arial',16,'bold'),bd=4)
    btn_sub.place(relx=.45,rely=.5)
    
    btn_clr=Button(frm,text='Clear',font=('arial',16,'bold'),bd=4)
    btn_clr.place(relx=.6,rely=.5)
    
def newuser_screen():
    frm=Frame(win)
    frm.configure(bg='powder blue')
    frm.place(relx=0,rely=.15,relwidth=1,relheight=.85)
    
    def back():
        frm.destroy()
        Main_screen()
        
    btn_new=Button(frm,text='Back',font=('arial',16,'bold'),bd=4,command=back)
    btn_new.place(relx=0,rely=0)
    
    lbl_name=Label(frm,text='Name',font=('arial',20,'bold'),bg='powder blue')
    lbl_name.place(relx=.3,rely=.1)
    
    e_name =Entry(frm,font=('arial',20,'bold'),bd=4)
    e_name.place(relx=.45 , rely=.1)
    e_name.focus()
    
    lbl_pass=Label(frm,text='Password',font=('arial',20,'bold'),bg='powder blue')
    lbl_pass.place(relx=.3,rely=.2)
    
    e_pass =Entry(frm,font=('arial',20,'bold'),bd=4,show='*')
    e_pass.place(relx=.45 , rely=.2)
    
    
    lbl_mail=Label(frm,text='Email',font=('arial',20,'bold'),bg='powder blue')
    lbl_mail.place(relx=.3,rely=.3)
    
    e_mail =Entry(frm,font=('arial',20,'bold'),bd=4,show='*')
    e_mail.place(relx=.45 , rely=.3)
    
    lbl_mob=Label(frm,text='Mobile.no',font=('arial',20,'bold'),bg='powder blue')
    lbl_mob.place(relx=.3,rely=.4)
    
    e_mob =Entry(frm,font=('arial',20,'bold'),bd=4,show='*')
    e_mob.place(relx=.45 , rely=.4)
    
    lbl_gender=Label(frm,text='Gender',font=('arial',20,'bold'),bg='powder blue')
    lbl_gender.place(relx=.3,rely=.5)
   
    cd_gender = Combobox(frm,values=['...Select','Male','Female','Others'],font=('arial',19,'bold'))
    cd_gender.place(relx=.45,rely=.5)
    
    lbl_acntype=Label(frm,text='ACN type',font=('arial',20,'bold'),bg='powder blue')
    lbl_acntype.place(relx=.3,rely=.6)
   
    cd_acntype = Combobox(frm,values=['...Select','Current','Saving','Others'],font=('arial',19,'bold'))
    cd_acntype.place(relx=.45,rely=.6)

    btn_sub=Button(frm,text='Submit',font=('arial',16,'bold'),bd=4)
    btn_sub.place(relx=.45,rely=.7)
    
    btn_clr=Button(frm,text='Clear',font=('arial',16,'bold'),bd=4)
    btn_clr.place(relx=.6,rely=.7)
    
def welcome_screen():
    frm=Frame(win)
    frm.configure(bg='powder blue')
    frm.place(relx=0,rely=.15,relwidth=1,relheight=.85)
    
    def logout():
        frm.destroy()
        Main_screen()
        
    lbl_wel=Label(frm,text='Welcome,',font=('arial',20,'bold'),bg='powder blue')
    lbl_wel.place(relx=0,rely=0)
        
    btn_log=Button(frm,text='Logout',font=('arial',16,'bold'),bd=4,command=logout)
    btn_log.place(relx=.92,rely=0)
        


Main_screen()
win.mainloop()