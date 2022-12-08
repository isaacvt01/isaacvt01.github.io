import tkinter as tk
from src.db.delete_one import delete_data


def delete():
    def safe():
        _id_saved = _id.get()
        delete_data(_id_saved)
        ask_for_options.iconify()

    ask_for_options = tk.Tk()
    ask_for_options.geometry('250x200')
    _id = tk.Entry(ask_for_options)

    tk.Label(ask_for_options, text="_id: ").grid(row=1)

    _id.grid(row=1, column=1, pady=6)

    tk.Button(ask_for_options, text='Cancel', command=ask_for_options.quit, ).grid(row=8, column=0, pady=4)
    tk.Button(ask_for_options, text='Enter', command=safe).grid(row=8, column=2, pady=4)

    tk.mainloop()
    exit()
