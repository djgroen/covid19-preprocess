from urllib.request import urlopen
import geopandas as gpd
import pandas as pd
import numpy as np

# with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
#     counties = json.load(response)
counties = gpd.read_file('./OSM Parser/landuse.geojson')
print(counties.columns)
df = pd.DataFrame(columns=['id', 'value'])
list = []
for index, row in counties.iterrows():
    d = {"id": row['id'], "value": np.random.randint(low = 0, high = 10) }
    list.append(d)

df = df.append(list, ignore_index=True)

import plotly.graph_objects as go

fig = go.Figure(go.Scattergeo())
fig.update_geos(
    visible=True, resolution=1050, scope="europe",
    showcountries=True, countrycolor="Black",
    showsubunits=True, subunitcolor="Blue"
)
fig.update_layout(height=300, margin={"r":0,"t":0,"l":0,"b":0})
fig.show()