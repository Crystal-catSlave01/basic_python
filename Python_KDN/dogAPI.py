import pandas as pd
from urllib.request import urlopen
import json

URL = 'https://api.thedogapi.com/v1/images/search'

response = urlopen(URL)
data = json.load(response)
print(data)
print(type(data))

