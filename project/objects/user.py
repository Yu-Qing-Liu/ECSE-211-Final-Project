import tkinter as tk
from tkinter import ttk
from tkinter import * 
from utils.grid_elem import Gridelem

class User:
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
        root.geometry('450x490')
        root.configure(background='#F0F8FF')
        root.title('GUI')


        # This is the section of code which creates the button grid
        
        y_pos = 50
        button_id = 0
        for i in range(5):
            for j in range(5):
                grid_button = Gridelem(button_id,root,self.get_inputs())
                self.inputs = grid_button.get_inputs()
                grid_button.button.configure(width=4, height=3)
                grid_button.button.place(x=50+70*j,y=y_pos)
                button_id += 1
            y_pos += 70

        #Start button onClick function

        def on_click():
            root.destroy()
            return None

        Button(root, width=35, height=2, text='Start Drawing', bg="#00FF00", font=('arial', 12, 'normal'), command=on_click).place(x=50,y=400)

        root.mainloop()
    
    #Reset the inputs
    def reset(self):
        self.inputs = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]