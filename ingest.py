import pandas as pd
import requests
import json

response_api = requests.get("https://data.cityofnewyork.us/resource/rbx6-tga4.json?issued_date>=2025-02-01T00:00:00.000")

data = response_api.json()
df = pd.DataFrame(data)

df.head()