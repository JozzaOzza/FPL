# Set Python Interpreter to Anaconda one recommended with ctrl-shift-p

# imports
import requests
import pandas as pd
import numpy as np

# testing requests
url = 'https://fantasy.premierleague.com/api/bootstrap-static/'
r = requests.get(url)
print(r.status_code)
json = r.json()
print(json.keys())
