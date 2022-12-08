import tkinter as tk
from src.db.update_data import update_data


def update():
    def save():
        _id_saved = _id.get()
        usage_saved = usage.get()
        model_saved = model.get()
        description_saved = description.get()
        shop_name_saved = shop_name.get()
        bicycle_brand_saved = bicycle_brand.get()
        update_data(_id_saved, usage_saved, model_saved, description_saved, shop_name_saved, bicycle_brand_saved)
        ask_for_options.iconify()

    ask_for_options = tk.Tk()
    ask_for_options.geometry('280x240')
    _id = tk.Entry(ask_for_options)
    usage = tk.Entry(ask_for_options)
    model = tk.Entry(ask_for_options)
    description = tk.Entry(ask_for_options)
    shop_name = tk.Entry(ask_for_options)
    bicycle_brand = tk.Entry(ask_for_options)


    tk.Label(ask_for_options, text="_id: ").grid(row=1)
    tk.Label(ask_for_options, text="usage: ").grid(row=2)
    tk.Label(ask_for_options, text="model: ").grid(row=3)
    tk.Label(ask_for_options, text="description: ").grid(row=4)
    tk.Label(ask_for_options, text="shop name: ").grid(row=5)
    tk.Label(ask_for_options, text="bicycle brand: ").grid(row=6)


    _id.grid(row=1, column=1, pady=6)
    usage.grid(row=2, column=1, pady=6)
    model.grid(row=3, column=1, pady=6)
    description.grid(row=4, column=1, pady=6)
    shop_name.grid(row=5, column=1, pady=6)
    bicycle_brand.grid(row=6, column=1, pady=6)

    tk.Button(ask_for_options, text='Cancel', command=ask_for_options.quit,).grid(row=8, column=0, pady=4)
    tk.Button(ask_for_options, text='Enter', command=save ).grid(row=8, column=2, pady=4)


    tk.mainloop()





