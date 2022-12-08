import pymongo
from tkinter import *
from tkinter import ttk
from src.db.show_data import show_data


def read():
    window = Tk()
    window.title('Database')
    table = ttk.Treeview(window, column=('c1', 'c2', 'c3', 'c4'))

    table.grid(row=1, column=0)
    table.heading('#0', text="ID")
    table.heading('#1', text="Model")
    table.heading('#2', text="Usage")
    table.heading('#3', text="Bicycle type")
    table.heading('#4', text="Bicycle brand")
    show_data(table)

    window.mainloop()