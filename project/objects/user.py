import tkinter as tk
from tkinter import ttk
from tkinter import * 
from utils.grid_element import Grid_Element
from utils.brick import EV3UltrasonicSensor,EV3ColorSensor,wait_ready_sensors,reset_brick
from objects.grid import Grid
from utils.error_message import Error_Message
from utils.cube_counter import Cube_Counter
from threading import Thread
from time import sleep

#Global variables
status = False

#US_sensor thread
def run(status_message):
    cs = EV3ColorSensor(1)
    wait_ready_sensors(True)
    global status
    try:
        while True:
            if cs.get_color_name() != "Unknown":
                print(cs.get_color_name())
                sleep(1.5)
                if cs.get_color_name() != "Unknown":
                    print(cs.get_color_name())
                    status_message.update_message("Status: Ready")
                    status_message.message.configure(fg="green")
                    status = True
            else:
                status_message.update_message("Status: Not Ready")
                status_message.message.configure(fg="red")
                status = False
            sleep(1)
    except BaseException as error:
        print(error) # For debugging

class User:
    #Constructor
    def __init__(self):
        self.inputs = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.root = Tk()
        self.cube_counter = Cube_Counter(self.root)
        self.error_message = Error_Message(self.root)
        self.status_message = Error_Message(self.root)

    #Modify inputs
    def set_inputs(self,new_inputs):
        self.inputs = new_inputs
    
    #Get inputs
    def get_inputs(self):
        return self.inputs

    #Initialize the gui
    def start(self):

        #Start us thread
        us_thread = Thread(target=run,args=(self.status_message,))
        us_thread.start()

        # This is the section of code which creates the main window
        self.root.geometry('575x490+350+0')
        self.root.configure(background='#F0F8FF')
        self.root.title('GUI')

        # This is the section of code which creates the cube counter
        self.cube_counter.label.place(x=425,y=50)

        # This is the section of code which creates the status message
        self.status_message.message.place(x=425,y=100)

        # This is the section of code which creates the button grid
        y_pos = 50
        button_id = 0
        for i in range(5):
            for j in range(5):
                grid_button = Grid_Element(button_id,self.root,self.get_inputs(),self.error_message,self.cube_counter)
                self.inputs = grid_button.get_inputs()
                grid_button.button.configure(width=4, height=3, bg="#FFFFFF")
                grid_button.button.place(x=50+70*j,y=y_pos)
                button_id += 1
            y_pos += 70

        #Start button on_click function
        def on_click():
            global status
            grid = Grid(self.inputs)
            self.error_message.message.place(x=50,y=450)
            if status:
                if grid.is_valid() == 0:
                    self.root.quit()
                elif grid.is_valid() == 1:
                    m = "Sorry, you have exceeded the amount of cubes available, please try again"
                    self.error_message.update_message(m)
                elif grid.is_valid() == 2:
                    m = "Sorry, you have to place at least 1 cube, please try again"
                    self.error_message.update_message(m)
                elif grid.is_valid() == 3:
                    m = "Sorry, An unexpected error has occured, please try again"
                    self.error_message.update_message(m)
            else:
                m = "Sorry, there arent enough cubes loaded onto the machine"
                self.error_message.update_message(m)
                

        Button(self.root, width=35, height=2, text='Start Drawing', bg="green", fg="white", font=('arial', 12, 'normal'), command=on_click).place(x=50,y=400)

        #If the user closes the GUI, Exit the program
        def on_closing():
            reset_brick()
            exit(0)
        self.root.protocol("WM_DELETE_WINDOW", on_closing)

        self.root.mainloop()

    #Exit GUI
    def exit(self):
        self.root.destroy()