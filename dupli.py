import os
from tkinter import *
from tkinter import messagebox

main = Tk()
main.geometry("715x500")
main.title("Skull Nation")
main.resizable(0, 0)


def Exit():
    sure = messagebox.askyesno("Exit", "Are you sure you want to exit?", parent=main)
    if sure == True:
        main.destroy()


main.protocol("WM_DELETE_WINDOW", Exit)


def emp():
    main.withdraw()
    os.system("login.py")
    main.deiconify()




label1 = Label(main)
label1.place(relx=0, rely=0, width=715, height=500)
img = PhotoImage(file="./project1.png")
label1.configure(image=img)

button1 = Button(main,command=emp)
button1.place(relx=0.28, rely=0.4, width=146, height=90)
button1.configure(relief="flat")
button1.configure(overrelief="flat")
button1.configure(activebackground="#ffffff")
button1.configure(cursor="hand2")
button1.configure(foreground="#ffffff")
button1.configure(background="#ffffff")
button1.configure(borderwidth="0")
img2 = PhotoImage(file="./un1.png")
button1.configure(image=img2)


button2 = Button(main)
button2.place(relx=0.566, rely=0.4, width=146, height=90)
button2.configure(relief="flat")
button2.configure(overrelief="flat")
button2.configure(activebackground="#ffffff")
button2.configure(cursor="hand2")
button2.configure(foreground="#ffffff")
button2.configure(background="#ffffff")
button2.configure(borderwidth="0")
img3 = PhotoImage(file="./2.png")
button2.configure(image=img3)


main.mainloop()
