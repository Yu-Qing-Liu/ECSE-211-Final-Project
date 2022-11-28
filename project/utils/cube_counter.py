import tkinter as tk
from tkinter import ttk
from tkinter import * 

class Cube_Counter:

    #Constructor
    def __init__(self,root):
        self.cubes = 0
        self.text = ("■",self.cubes)
        self.label = Label(root, text=self.text,fg="#0A7029",font=('arial', 15, 'normal'))
    
    #Update inputs
    def update_num_cubes(self,new_amount):
        self.cubes = new_amount
        new_text = ("■",self.cubes)
        if self.cubes < 16: 
            self.label.configure(text=new_text,fg="#0A7029")
        else: 
            self.label.configure(text=new_text,fg="#FF0000")
        return None
