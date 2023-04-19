from gekko import Gekko
from gekko_adapter import GekkoAdapter
import json

g = Gekko
json_df = g.get_categories()
GekkoAdapter.json_to_csv(json_df, "categories.csv")
