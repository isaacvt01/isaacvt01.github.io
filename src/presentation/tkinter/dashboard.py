import tkinter as tk
from src.presentation.tkinter.create import create
from src.presentation.tkinter.delete import delete
from src.presentation.tkinter.update import update
from src.presentation.tkinter.read import read

# Define a function to display a Tkinter window with the options cancel, delete, insert, update and show all.
def dashboard():
    # Create the variable sudo_window with the value of a Tkinter window
    sudo_window = tk.Tk()
    sudo_window.title('Sudo mode')
    sudo_window.geometry('350x250')
    # Add text prompt + cancel, delete, insert, update, show all buttons
    # In each button is associated with the function that will be called, you can see in command
    tk.Label(sudo_window,
             text="What do you want to do?").grid(row=0, column=2, sticky=tk.W, pady=5)
    tk.Button(sudo_window,
              text='Cancel',
              command=sudo_window.quit).grid(row=6,
                                             column=2,
                                             sticky=tk.W,
                                             pady=5)
    tk.Button(sudo_window,
              text='Delete',
              command=delete).grid(row=2,
                                   column=2,
                                   sticky=tk.W,
                                   pady=5)
    tk.Button(sudo_window,
              text='Insert',
              command=create).grid(row=3,
                                   column=2,
                                   sticky=tk.W,
                                   pady=5)
    tk.Button(sudo_window,
              text='Update',
              command=update).grid(row=4,
                                   column=2,
                                   sticky=tk.W,
                                   pady=5)
    tk.Button(sudo_window,
              text='Show all',
              command=read).grid(row=5,
                                 column=2,
                                 sticky=tk.W,
                                 pady=5)

    tk.mainloop()