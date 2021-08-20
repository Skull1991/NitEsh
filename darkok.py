from tkinter import *
from tkinter import PhotoImage
skull=Tk()
skull.title("lol")
skull.config(bg="#CECCBE")
skull.geometry('800x800')
btnState=False
onImg=PhotoImage(file=r'skull.png')
offImg=PhotoImage(file=r'reaper.png')
def switch():
    global btnState
    if btnState:
        btn.config(image=offImg,bg="#CECCBE",activebackground="#CECCBE")
        skull.config(bg="#CECCBE")
        txt.config(text="DARK Mode:OFF",bg="#CECCBE")
        txt1.config(text="Username", bg="#CECCBE")
        btnState=False
    else:
        btn.config(image=onImg, bg="#2B2B2B", activebackground="#2B2B2B")
        skull.config(bg="#2B2B2B")
        txt.config(text="DARK Mode:ON",bg="#2B2B2B")
        txt1.config(text="Username", bg="#2B2B2B")
        btnState=True

txt=Label(skull,text="Dark Mode:OFF",font="arial 20",bg="#CECCBE",fg="green")
txt.place(relx=0.5,rely=0.3,anchor="center")
btn=Button(skull,text="OFF",borderwidth=0,command=switch,bg="#CECCBE",activebackground="#CECCBE",image=offImg)
btn.place(relx=0.5,rely=0.5,anchor="center")

e1=Entry(skull)
e1.place(relx=0.3,rely=0.3,anchor="center")
txt1=Label(skull,text="Username",font="arial 20",bg="#CECCBE",fg="green")
txt1.place(relx=0.2,rely=0.3,anchor="center")
skull.mainloop()
