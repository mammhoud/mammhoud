#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 22:04:11 2022

@author: mammhoud
"""

from tkinter import *
from tkinter import ttk
root=Tk()

x='mmammhoud'




bottom = ttk.Button(root, text=x,command=root.destroy())
bottom.pack()

root.mainloop()


