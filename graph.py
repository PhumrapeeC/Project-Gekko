import tkinter as tk
import requests
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
import threading
from datetime import datetime

class Graph:
    def __init__(self) -> None:
        self.url = 'https://api.coingecko.com/api/v3/coins/'
        self.coins = []
        response = requests.get('https://api.coingecko.com/api/v3/coins/list')
        self.data = response.json()
        for coin in self.data:
            self.coins.append(coin['id'])

    def get_data(self,coin):
        params = {
            'vs_currency': 'usd',
            'days': '30'
        }
        response = requests.get(self.url + coin + '/market_chart', params=params)
        data = response.json()
        prices = []
        for point in data['prices']:
            prices.append(point[1])
        return prices

    def get_line(self,coin):
        params = {
            'vs_currency': 'usd',
            'days': '30'
        }
        response = requests.get(self.url + coin + '/market_chart', params=params)
        data = response.json()
        date = []
        prices = []
        for point in data['prices']:
            unix = datetime.fromtimestamp(point[0]/1000)
            date.append(unix)
            prices.append(point[1])
        data_plot = pd.DataFrame({"Date":date, "Price":prices})
        return data_plot