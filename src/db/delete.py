import tkinter as tk
from src.db.delete_one import delete_data

# Defining a function to delete data from a Tkinter window
def delete():
    # We define a function that will save the data entered at the moment of hitting enter
    # and call the function delete_data
    def safe():
        _id_saved = _id.get()
        delete_data(_id_saved)
        ask_for_options.iconify()

    # We define the variable ask_for_options as the Tkinter window. We put a size of 250x200
    ask_for_options = tk.Tk()
    ask_for_options.geometry('250x200')

    # Enter the corresponding entry for id
    _id = tk.Entry(ask_for_options)
    # Name the text that will appear next to the id entry
    tk.Label(ask_for_options, text="_id: ").grid(row=1)
    # Indicates where each text entry will be positioned
    _id.grid(row=1, column=1, pady=6)
    # We program the Cancel and Enter buttons, with their specific functions.
    # Cancel will close the window and Enter will execute the save function.
    tk.Button(ask_for_options, text='Cancel', command=ask_for_options.quit, ).grid(row=8, column=0, pady=4)
    tk.Button(ask_for_options, text='Enter', command=safe).grid(row=8, column=2, pady=4)

    tk.mainloop()
    exit()
