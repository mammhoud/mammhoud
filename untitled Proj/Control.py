# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Hello World")


#Full Name

ttk.Label(root, text="full Name:").grid(row=0,column=0,padx=10,pady=10)
EntryFullName=ttk.Entry(root,width=25,font=('Arial',16))
EntryFullName.grid(row=0,column=1,columnspan=2,pady=10)



root.mainloop()