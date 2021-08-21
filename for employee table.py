from tkinter import*
from tkinter import ttk
root=Tk()
root.geometry('500x500')
my_tree=ttk.Treeview(root)
my_tree['columns']=("Name","Id","Favourite Pizza")
my_tree.column("#0",width=0,stretch=NO)
my_tree.column("Name",anchor=W,width=120)
my_tree.column("Id",anchor=CENTER,width=80)
my_tree.column("Favourite Pizza",anchor=W,width=120)
my_tree.heading("#0",text="",anchor=W)
my_tree.heading("Name",text="Customer Name",anchor=W)
my_tree.heading("Id",text="ID",anchor=CENTER)
my_tree.heading("Favourite Pizza",text="Favourite Pizza",anchor=W)

#data insert in tree
my_tree.insert(parent='',index='end',iid=0,text="Parent",values=("John",1,"pepporine"))
my_tree.pack(pady=20)







root.mainloop()