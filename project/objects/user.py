import tkinter as tk
from tkinter import ttk
from tkinter import * 
from utils.grid_element import Grid_Element
from utils.brick import EV3UltrasonicSensor
from objects.grid import Grid
from utils.error_message import Error_Message

class User:
    #Constructor
    def __init__(self):
        self.inputs = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.root = Tk()
        self.us = EV3UltrasonicSensor(2)
        self.us_data = self.us.get_cm()

    #Modify inputs
    def set_inputs(self,new_inputs):
        self.inputs = new_inputs
    
    #Get inputs
    def get_inputs(self):
        return self.inputs

    #Initialize the gui
    def start(self):

        # This is the section of code which creates the main window
        self.root.geometry('450x490')
        self.root.configure(background='#F0F8FF')
        self.root.title('GUI')


        # This is the section of code which creates the button grid
        
        y_pos = 50
        button_id = 0
        for i in range(5):
            for j in range(5):
                grid_button = Grid_Element(button_id,self.root,self.get_inputs())
                self.inputs = grid_button.get_inputs()
                grid_button.button.configure(width=4, height=3)
                grid_button.button.place(x=50+70*j,y=y_pos)
                button_id += 1
            y_pos += 70

        #Start button onClick function
        def on_click():
            grid = Grid(self.inputs)
            error_message = Error_Message(self.root)
            error_message.message.place(x=50,y=450)
            if(True):#self.us_data < 5):
                if grid.is_valid() == 0:
                    error_message.hide_message()
                    self.root.quit()
                elif grid.is_valid() == 1:
                    m = "Sorry, you have exceeded the amount of cubes available, please try again"
                    error_message.update_inputs(m)
                elif grid.is_valid() == 2:
                    m = "Sorry, you have to place at least 1 cube, please try again"
                    error_message.update_inputs(m)
                elif grid.is_valid() == 3:
                    m = "Sorry, An unexpected error has occured, please try again"
                    error_message.update_inputs(m)

        Button(self.root, width=35, height=2, text='Start Drawing', bg="#00FF00", font=('arial', 12, 'normal'), command=on_click).place(x=50,y=400)

        #If the user closes the GUI, Exit the program
        def on_closing():
            exit(0)
        self.root.protocol("WM_DELETE_WINDOW", on_closing)

        self.root.mainloop()
    
    #Reset the inputs
    def reset(self):
        self.inputs = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]