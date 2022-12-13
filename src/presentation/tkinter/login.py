import tkinter as tk
from src.presentation.tkinter.dashboard import dashboard


# Define a function that creates a Tkinter window and displays the following options
def login():
    # Define a function that saves the entered data
    def get_fields():
        user_saved = user.get()
        password_saved = password.get()
        if user_saved == 'Admin' and password_saved == '1234':
            master.iconify()
            dashboard()
        else:
            master.iconify()
            return 'Viewer'

        return 'Finished'

    # Declare master as the Tkinter window
    # Add the corresponding text next to each field

    master = tk.Tk()
    master.title('Sign up')

    tk.Label(master, text="User name").grid(row=0)
    tk.Label(master, text="Password").grid(row=1)

    # Create variables with the values entry in the master window
    # Place the Entry values in the master window
    # Assign to the buttons the functions to close the window in Cancel and to call the Get_Fields function in Enter.

    user = tk.Entry(master)
    password = tk.Entry(master)

    user.grid(row=0, column=1)
    password.grid(row=1, column=1)

    tk.Button(master,
              text='Cancel',
              command=master.quit).grid(row=3,
                                        column=0,
                                        sticky=tk.W,
                                        pady=4)
    tk.Button(master,
              text='Enter', command=get_fields, ).grid(row=3,
                                                       column=1,
                                                       sticky=tk.W,
                                                       pady=4)

    tk.mainloop()
