import tkinter as tk
from tkinter import ttk
from gekko import Gekko
from gekko_adapter import GekkoAdapter
import json


class GekkoApp:
    def __init__(self, master):
        self.master = master
        self.master.geometry("800x800")
        self.master.title("GEKKO")
        self.master.resizable(False, False)

        self.title_label = tk.Label(self.master, text="PROJECT GEKKO", font=("Arial", 18))
        self.title_label.pack(padx=20, pady=20)

        self.canvas = tk.Canvas(self.master, bg='white', width=700, height=450)
        self.canvas.pack(padx=10, pady=10)

        self.selected_coin = tk.StringVar()
        self.selected_graph = tk.StringVar()

        options_0 = ["Option 1", "Option 2", "Option 3"]
        options_1 = ["Option 4", "Option 5", "Option 6"]

        self.coin_label = ttk.Label(self.master, text="Please select a coin:", font=('Arial', 16))
        self.coin_combo = ttk.Combobox(self.master, values=options_0, textvariable=self.selected_coin)

        self.coin_label.pack(fill=tk.X, padx=10, pady=10)
        self.coin_combo.pack(padx=10, pady=10)

        self.graph_label = ttk.Label(self.master, text="Please select a graph:", font=('Arial', 16))
        self.graph_combo = ttk.Combobox(self.master, values=options_1, textvariable=self.selected_graph)

        self.graph_label.pack(fill=tk.X, padx=10, pady=10)
        self.graph_combo.pack(padx=10, pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = GekkoApp(root)
    root.mainloop()
