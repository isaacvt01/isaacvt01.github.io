from tkinter import *
from tkinter import ttk
from src.db.show_data import show_data


# Define a function that creates a table with all the data in the database.
def read():
    # Define the variable ask_for_options as the Tkinter window. Put a size of 250x200
    # Define the variable table with the Tkinter table. with the column property we indicate how many columns we want.
    # Put the headings of the tables with the name of each field
    window = Tk()
    window.title('Database')
    table = ttk.Treeview(window, column=('c1', 'c2', 'c3', 'c4'))

    table.grid(row=1, column=0)
    table.heading('#0', text="ID")
    table.heading('#1', text="Model")
    table.heading('#2', text="Usage")
    table.heading('#3', text="Bicycle type")
    table.heading('#4', text="Bicycle brand")
    # Call the function show_data with the parameter table
    show_data(table)

    window.mainloop()
