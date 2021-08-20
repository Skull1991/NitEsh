from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import os
root=Tk()

global e1
global e2

def ok():
    uname=e1.get()
    password=e2.get()
    if(uname==""and password==""):
        messagebox.showinfo("","Blank Not Allowed")
    elif(uname=="Admin"and password=="123"):
        messagebox.showinfo("","Login Success")
        root.withdraw()
        os.system("whatlol.py")


    else:
        messagebox.showinfo("","Incorrect")




root.title("Login")
myimage=ImageTk.PhotoImage(Image.open('login.png'))
Label(image=myimage).pack()
#e1 entry for username entry
e1=Entry(root,width=40,border=0,font=('Consolas',13))
e1.place(x=510,y=210)

#e2 entry for password entry
e2=Entry(root,width=40,border=0,show='*',font=('Consolas',13))
e2.place(x=510,y=300)

Button(root,text='LOGIN',padx=20,pady=10,border=0,bg="#D2463E",activebackground="#D2463E",command=ok).place(x=640,y=525)
root.mainloop()