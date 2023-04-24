import tkinter as tk
from tkinter import ttk
from gekko import Gekko
from gekko_adapter import GekkoAdapter
import json


root = tk.Tk()
root.geometry("500x500")
root.title("GEKKO")

title_lable = tk.Label(root, text="PROJECT GEKKO", font=("Arial", 18))
title_lable.pack(padx=20, pady=20)

textbox = tk.Text(root, font=('Arial', 16))
textbox.pack(padx=10, pady=10)

selected_coin = tk.StringVar()
options = ["Option 1", "Option 2", "Option 3"]

label = ttk.Label(root, text="Please select a coin:", font=('Arial', 16))
combo_button = ttk.Combobox(root, values=options, textvariable=selected_coin)

label.pack(fill=tk.X, padx=10, pady=10)
combo_button.pack(padx=10, pady=10)

label = ttk.Label(root, text="Please select a graph:", font=('Arial', 16))
combo_button = ttk.Combobox(root, values=options, textvariable=selected_coin)

label.pack(fill=tk.X, padx=10, pady=10)
combo_button.pack(padx=10, pady=10)

root.mainloop()
