# Project-Gekko

Gekko crypto monitorring app is a Python program that creates a simple GUI that allows the user to select a cryptocurrency and plot its historical price data in various graph types such as line plot, histogram, and box plot. The program uses the tkinter library for creating the GUI and the requests, seaborn, pandas, and matplotlib libraries for retrieving, cleaning, and plotting data.

The program retrieves a list of cryptocurrency names from the CoinGecko API and populates a list box in the GUI with these names. When the user selects a cryptocurrency and a graph type, the program retrieves the historical price data for the selected cryptocurrency using the CoinGecko API and plots the data in the selected graph type.
