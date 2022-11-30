import tkinter as tk
from tkinter import ttk
from tkinter import * 

class Gridelem():

    #Constructor
    def __init__(self,id,root,inputs):
        self.id = id
        self.root = root
        self.inputs = inputs
        self.state = False
        def on_click():
            if self.state:
                self.button.configure(bg="#FFFFFF")
            else:
                self.button.configure(bg="#000000")
            self.state = not self.state
            self.update_inputs()
        self.button = Button(root, text='     ', bg="#FFFFFF", font=('arial', 12, 'normal'), command=on_click)
    
    #Update inputs
    def update_inputs(self):
        if(self.state):
            self.inputs[self.id] = 1
        else:
            self.inputs[self.id] = 0
        return self.inputs

    #Retrieve inputs
    def get_inputs(self):
        return self.inputs

    #Modify inputs
    def set_grid(self,new_inputs):
        self.inputs = new_inputs
