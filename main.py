import tkinter as tk
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
from graph import Graph
from datetime import datetime

def create_graph(coin, data, graph_type):
    if graph_type == 'histogram':
        plt.clf()  
        color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        sns.histplot(data, bins=20, color=color)
        sns.set_style('whitegrid')
        sns.despine(left=True)
        plt.title('Daily Closing Prices of ' + coin.capitalize())
        plt.xlabel('Price (USD)')
        plt.ylabel('Frequency')
        if hasattr(app, 'canvas'):
            app.canvas.get_tk_widget().destroy()
        fig = plt.gcf()
        app.canvas = FigureCanvasTkAgg(fig, master=app.page2)
        app.canvas.draw()
        app.canvas.get_tk_widget().pack()

    if graph_type == "lineplot":
        plt.clf()  
        color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        g = sns.lineplot(data=data, x="Date", y = "Price", color=color)
        x_dates = data['Date'].dt.strftime('%Y-%m-%d').sort_values().unique()
        g.set_xticklabels(labels=x_dates, rotation=45, ha='right')
        
        sns.set_style('whitegrid')
        sns.despine(left=True)
        plt.title('Monthly Price of ' + coin.capitalize())
        plt.xlabel('Date')
        plt.ylabel('Price (USD)')
        if hasattr(app, 'canvas'):
            app.canvas.get_tk_widget().destroy()
        fig = plt.gcf()
        app.canvas = FigureCanvasTkAgg(fig, master=app.page2)
        app.canvas.draw()
        app.canvas.get_tk_widget().pack()

    if graph_type == "boxplot":
        plt.clf()  
        plt.boxplot(data)
        plt.title(f'{coin.capitalize()} Historical Prices')
        plt.ylabel('Price (USD)')
        if hasattr(app, 'canvas'):
            app.canvas.get_tk_widget().destroy()
        fig = plt.gcf()
        app.canvas = FigureCanvasTkAgg(fig, master=app.page2)
        app.canvas.draw()
        app.canvas.get_tk_widget().pack()


class MainApplication(tk.Frame):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.graph = Graph()
        self.pack()
        self.create_widgets()
        self.create_graph()
    
    def create_widgets(self):
        self.page1 = tk.Frame(self)
        self.page1.pack()

        self.coin_entry = tk.Entry(self.page1, width=30)
        self.coin_entry.pack(pady=10)
        self.coin_entry.bind('<KeyRelease>', self.update_listbox)

        self.coin_listbox = tk.Listbox(self.page1, width=30, height=10)
        self.coin_listbox.pack(pady=10)

        for coin in self.graph.coins:
            self.coin_listbox.insert(tk.END, coin)

        graph_types = ['histogram', 'lineplot','boxplot']
        self.graph_var = tk.StringVar()
        self.graph_var.set(graph_types[0])
        graph_menu = tk.OptionMenu(self.page1, self.graph_var, *graph_types)
        graph_menu.pack(pady=10)

        submit_button = tk.Button(self.page1, text='Submit', command=self.show_graph)
        submit_button.pack(pady=10)

        quit_button = tk.Button(self.page1, text='Quit', command=self.master.destroy)
        quit_button.pack(pady=10)

        self.page2 = tk.Frame(self)
        self.back_button = tk.Button(self.page2, text='Back', command=self.show_page1)
        self.back_button.pack(pady=10)

    def create_graph(self):
        self.fig, self.ax = plt.subplots(figsize=(10, 8))
        sns.histplot([], bins=20, ax=self.ax)
        sns.set_style('whitegrid')
        sns.despine(left=True)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.page2)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()

    def update_listbox(self, *args):
        current_text = self.coin_entry.get().lower()
        self.coin_listbox.delete(0, tk.END)

        for coin in self.graph.coins:
            if current_text in coin.lower():
                self.coin_listbox.insert(tk.END, coin)

    def show_page1(self):
        self.page2.pack_forget()
        self.page1.pack()

    def show_page2(self):
        self.page1.pack_forget()
        self.page2.pack()

    def show_graph(self):
        selected_coin = self.coin_listbox.get(self.coin_listbox.curselection())
        data = self.graph.get_data(selected_coin)
        if self.graph_var.get() == "lineplot":
            data = self.graph.get_line(selected_coin)
        create_graph(selected_coin, data, self.graph_var.get())
        self.show_page2()


root = tk.Tk()
root.title('Gecko Cryptocurrency Monitoring App')
root.geometry("1400x1200")
app = MainApplication(master=root)
app.mainloop()