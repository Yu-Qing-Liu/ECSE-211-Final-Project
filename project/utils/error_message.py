import tkinter as tk
from tkinter import ttk
from tkinter import * 

class Error_Message:

    #Constructor
    def __init__(self,root):
        self.message = Label(root,text="",fg="red")
    
    #Update inputs
    def update_message(self,message):
        self.message.configure(text=message)

    #Hide message
    def hide_message(self):
        self.message.place_forget()
