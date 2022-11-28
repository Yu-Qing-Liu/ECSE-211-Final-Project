import tkinter as tk
from tkinter import ttk
from tkinter import * 

class Grid_Element:

    #Constructor
    def __init__(self,id,root,inputs,error_message,cube_counter):
        self.id = id
        self.inputs = inputs
        self.state = False
        def on_click():
            error_message.hide_message()
            if self.state:
                self.button.configure(bg="#FFFFFF")
            else:
                self.button.configure(bg="#000000")
            self.state = not self.state
            self.update_inputs()
            cube_counter.update_num_cubes(self.count_cubes())
        self.button = Button(root,command=on_click)
    
    #Count inputs
    def count_cubes(self):
        cubes = 0
        for num in self.inputs:
            if num == 1:
                cubes+=1
        return cubes

    #Update inputs
    def update_inputs(self):
        if(self.state):
            self.inputs[self.id] = 1
        else:
            self.inputs[self.id] = 0
        return None

    #Retrieve inputs
    def get_inputs(self):
        return self.inputs
