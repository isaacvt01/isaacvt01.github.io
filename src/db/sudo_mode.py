import tkinter as tk
from src.db.create import create
from src.db.delete import delete
from src.db.update import update
from src.db.read import read


def sudo_mode():
    sudo_window = tk.Tk()
    sudo_window.title('Sudo mode')
    sudo_window.geometry('350x200')
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
