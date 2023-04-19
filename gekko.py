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
        data = response.json()
        return data

