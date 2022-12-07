import tkinter as tk
from src.db.sudo_mode import sudo_mode


def request_access():
    def get_fields():
        user_saved = user.get()
        password_saved = password.get()
        if user_saved == 'Admin' and password_saved == '1234':
            master.iconify()
            sudo_mode()
        else:
            master.iconify()
            return 'Viewer'

        return 'Finished'

    master = tk.Tk()

    master.title('Sign up')
    tk.Label(master,
             text="User name").grid(row=0)
    tk.Label(master,
             text="Password").grid(row=1)

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
