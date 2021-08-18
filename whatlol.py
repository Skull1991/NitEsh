from tkinter import *
from tkinter import messagebox
import sqlite3
import random


skull=Tk()
global bill_no
global c_name
global c_phone
def clear():
    c_name.set('')
    c_phone.set('')
    item.set('')
    rate.set(0)
    quantity.set(0)
    welcome()
def exit():
    op = messagebox.askyesno("Do you really want to exit?")
    if op > 0:
        root.destroy()

def save_bill():
    op = messagebox.askyesno("Do you want t o save the Bill?")
    if op > 0:
        bill_details = textarea.get('1.0', END)
        f1 = open("bills/" + str(bill_no.get()) + ".txt", "w")
        f1.write(bill_details)
        f1.close()
        messagebox.showinfo("Saved", f"Bill no, :{bill_no.get()} Saved Successfully")
    else:
        return
def welcome():
    textarea.delete(1.0, END)
    textarea.insert(END, "\t  Welcome To Retail Billing Tool")
    textarea.insert(END, f"\n*****************************************************\n")
    # textarea.insert(END, f"\n\nBill Number:\t\t{bill_no.get()}")
    textarea.insert(END, f"\nCustomer's Name:\t\t{c_name.get()}")
    textarea.insert(END, f"\nPhone Number:\t\t{c_phone.get()}")
    textarea.insert(END, f"\n\n*****************************************************")
    textarea.insert(END, "\nProduct Name : \t\t Quantity: \t\t Price: ")
    textarea.insert(END, f"\n*****************************************************\n")
    textarea.configure(font='cambria 15 bold')


def admin():
    pass
def employee():
    global root
    root=Tk()
    frame_colour = 'lavender'
    root.geometry('1280x720')
    c_name = StringVar()
    c_phone = StringVar()
    item = StringVar()
    rate = IntVar()
    quantity = IntVar()
    bill_no = StringVar()
    x = random.randint(1000, 9999)
    bill_no.set(str(x))
    global lst
    lst = []


    global textarea
    employee = Button()


    title = Label(root, pady=2, text="Billing Tool", bd=12, bg=frame_colour, fg='black', font=('cambria', 30, 'bold'))
    title.pack(fill=X)
    F1 = LabelFrame(root, text="Customer's information", font=('cambria', 18, 'bold'), fg='black', bg=frame_colour)
    F1.place(x=0, y=80, relwidth=1)

    cname_label = Label(F1, text='Customer Name : ', font=('cambria', 18, 'bold'), bg=frame_colour, fg='black')
    cname_label.grid(row=0, column=0, padx=20, pady=5)
    cname_entry = Entry(F1, width=15, textvariable=c_name, font='cambria 15 bold')
    cname_entry.grid(row=0, column=1, padx=10, pady=5)

    cphone_lbl = Label(F1, text='Phone Number : ', font=('cambria', 18, 'bold'), bg=frame_colour, fg='black')
    cphone_lbl.grid(row=0, column=2, padx=20, pady=5)
    cphone_txt = Entry(F1, width=15, font='cambria 15 bold', textvariable=c_phone)
    cphone_txt.grid(row=0, column=3, padx=10, pady=5)

    # product information
    # -----------------------------------------------
    F2 = LabelFrame(root, text='Product Information', font=('cambria', 18, 'bold'), fg='black', bg=frame_colour)
    F2.place(x=0, y=180, width=630, height=500)

    itm = Label(F2, text='Product Name : ', font=('cambria', 18, 'bold'), bg=frame_colour, fg='black').grid(row=0,
                                                                                                            column=0,
                                                                                                            padx=30,
                                                                                                            pady=20)
    itm_txt = Entry(F2, width=20, textvariable=item, font='cambria 15 bold').grid(row=0, column=1, padx=10, pady=20)

    rateofProduct = Label(F2, text='Product Rate : ', font=('cambria', 18, 'bold'), bg=frame_colour, fg='black').grid(
        row=1, column=0, padx=30, pady=20)

    rate_txt = Entry(F2, width=20, textvariable=rate, font='cambria 15 bold').grid(row=1, column=1, padx=10, pady=20)

    quantityOfProduct = Label(F2, text='Product Quantity : ', font=('cambria', 18, 'bold'), bg=frame_colour,
                              fg='black').grid(row=2, column=0, padx=30, pady=20)
    quantity_txt = Entry(F2, width=20, textvariable=quantity, font='cambria 15 bold').grid(row=2, column=1, padx=10,
                                                                                           pady=20)

    # Buttons to save, edit and generate bill
    # ---------------------------------------------------------------------------------------------------------------
    btn1 = Button(F2, text='Add', font='cambria 15 bold',  padx=5, pady=10, bg='black', fg='white',
                  width=15)
    btn1.grid(row=3, column=0, padx=10, pady=30)
    btn2 = Button(F2, text='Get Bill', font='cambria 15 bold', padx=5, pady=10, bg='black', fg='white',
                  width=15)
    btn2.grid(row=3, column=1, padx=10, pady=30)

    btn4 = Button(F2, text='Exit', font='cambria 15 bold', padx=5, pady=10, command=exit, bg='black', fg='white',
                  width=15)
    btn4.grid(row=4, column=1, padx=10, pady=30)

    # Bill showing area
    # -------------------------------------------------------------------------------------------------------------------
    F3 = Frame(root)
    F3.place(x=700, y=180, width=550, height=500)

    title = Label(F3, text='Billing Area', font='cambria 15 bold')
    title.pack(fill=X)
    scrol_y = Scrollbar(F3, orient=VERTICAL)
    textarea = Text(F3, yscrollcommand=scrol_y)
    scrol_y.pack(side=RIGHT, fill=Y)
    scrol_y.config(command=textarea.yview)
    textarea.pack()
    welcome()



employee=Button(skull,text='Employee',command=employee)
employee.grid(row=0,column=0,columnspan=2,ipadx=300,ipady=100,padx=5,pady=5)
admin=Button(skull,text='  Admin  ',command=admin)
admin.grid(row=1,column=0,columnspan=2,ipadx=300,ipady=100,padx=5,pady=5)
skull.mainloop()