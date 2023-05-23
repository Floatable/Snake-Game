import tkinter as tk
from tkinter import messagebox
def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass
 
 
message_box('You Lost!', 'Play again...')