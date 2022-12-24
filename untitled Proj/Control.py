# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title("Hello World")


# Full Name

ttk.Label(root, text="full Name:").grid(row=0, column=0, padx=10, pady=10)
EntryFullName = ttk.Entry(root, width=25, font=('Arial', 16))
EntryFullName.grid(row=0, column=1, columnspan=2, pady=10)


#gender
ttk.Label(root, text="Gender:").grid(row=1, column=0)
SpanGender=StringVar()
ttk.Radiobutton(root,text="MALE",variable=SpanGender,value="Male").grid(row=1, column=1)
ttk.Radiobutton(root,text="FEMALE",variable=SpanGender,value="Female").grid(row=1, column=2)


#radio buttom

#Comment



ttk.Label(root,text="comments:").grid(row=2,column=0)
xtComments=Text(root,width=30,height=14,font=('Arial',16))
xtComments.grid(row=2,column=1,columnspan=2)


#buttom

#bottom

root.mainloop()
