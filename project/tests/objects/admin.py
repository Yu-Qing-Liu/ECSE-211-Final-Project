import tkinter as tk
from tkinter import ttk
from tkinter import * 
from utils.grid_elem import Gridelem

class Admin:
    #Constructor
    def __init__(self):
        self.inputs = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    #Modify inputs
    def set_inputs(self,new_inputs):
        self.inputs = new_inputs
    
    #Get inputs
    def get_inputs(self):
        return self.inputs

    #Initialize the gui
    def start(self):

        root = Tk()

        # This is the section of code which creates the main window
        root.geometry('350x500')
        root.configure(background='#F0F8FF')
        root.title('Admin')


        # This is the section of code which creates the button grid
        
        y_pos = 50
        button_id = 0
        for i in range(5):
            for j in range(5):
                grid_button = Gridelem(button_id,root,self.get_inputs())
                self.inputs = grid_button.get_inputs()
                grid_button.button.place(x=50+50*j,y=y_pos)
                button_id += 1
            y_pos += 50

        #Start button onClick function

        def on_click():
            root.destroy()
            return None

        Button(root, text='Start Drawing', bg="#FFFFFF", font=('arial', 12, 'normal'), command=on_click).place(x=50,y=350)

        root.mainloop()
    
    #Reset the inputs
    def reset(self):
        self.inputs = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]