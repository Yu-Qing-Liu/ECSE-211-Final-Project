import tkinter as tk
from tkinter import ttk
from tkinter import * 

class Error_Message():

    #Constructor
    def __init__(self,root):
        self.root = root
        self.message = Text(root, fg="red", wrap="word")
    
    #Update inputs
    def update_inputs(self,message):
        self.message.insert("end", message)

    #Hide message
    def hide_message(self):
        self.message.pack_forget()

    #Delete message
    def delete_message(self):
        self.message.delete()
