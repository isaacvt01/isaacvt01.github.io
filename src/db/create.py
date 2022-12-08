import tkinter as tk
from src.db.create_data import create_data


def create():
    def save():
        usage_saved = usage.get()
        model_saved = model.get()
        description_saved = description.get()
        shop_name_saved = shop_name.get()
        bicycle_brand_saved = bicycle_brand.get()
        create_data(usage_saved, model_saved, description_saved, shop_name_saved, bicycle_brand_saved)
        ask_for_options.quit()

    ask_for_options = tk.Tk()
    ask_for_options.geometry('250x200')
    usage = tk.Entry(ask_for_options)
    model = tk.Entry(ask_for_options)
    description = tk.Entry(ask_for_options)
    shop_name = tk.Entry(ask_for_options)
    bicycle_brand = tk.Entry(ask_for_options)

    tk.Label(ask_for_options, text="usage: ").grid(row=1)
    tk.Label(ask_for_options, text="model: ").grid(row=2)
    tk.Label(ask_for_options, text="description: ").grid(row=3)
    tk.Label(ask_for_options, text="shop name: ").grid(row=4)
    tk.Label(ask_for_options, text="bicycle brand: ").grid(row=5)


    usage.grid(row=1, column=1, pady=6)
    model.grid(row=2, column=1, pady=6)
    description.grid(row=3, column=1, pady=6)
    shop_name.grid(row=4, column=1, pady=6)
    bicycle_brand.grid(row=5, column=1, pady=6)

    tk.Button(ask_for_options, text='Cancel', command=ask_for_options.quit(),).grid(row=8, column=0, pady=4)
    tk.Button(ask_for_options, text='Enter', command=save ).grid(row=8, column=2, pady=4)


    tk.mainloop()
    exit()



