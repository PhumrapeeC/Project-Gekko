import requests
import pandas as pd
import json
import time


class Gekko():
    def __init__(self) -> None:
        pass

    def get_categories():
        url = "https://api.coingecko.com/api/v3/coins/categories"
        response = requests.get(url)
        categoires = response.json()
        return categoires
    
    def get_trending():
        url = "https://api.coingecko.com/api/v3/search/trending"
        response = requests.get(url)
        trending = response.json()
        return trending
    
    def get_exchange_rate():
        url = "https://api.coingecko.com/api/v3/exchange_rates"
        response = requests.get(url)
        exchange_rate = response.json()
        return exchange_rate
    
    
    


