#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 22:04:11 2022

@author: mammhoud
"""
import sqlite3
class DBConnection:
    def __init__(self):
        self._db = sqlite3.connect("Reservaion.db")
        self._db.row_factory=sqlite3.Row
        self._db.execute("create table if not exists Ticket(ID ineger primary key ")
        


from tkinter import *
from tkinter import ttk
root=Tk()

x='mmammhoud'




bottom = ttk.Button(root, text=x,command=root.destroy())

#list view comment
''''''
tk.Label(root,text="comments:").grid(row=2,column=0)
xtComments=Text(root,width=30,height=14,font=('Arial',16))
xtComments.grid(row=2,column=1,columnspan=2)

''''''

root.mainloop()


