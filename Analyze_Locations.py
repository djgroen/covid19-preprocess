import plotly.express as px
import plotly.graph_objects as go
import  plotly as py
import pandas as pd
import sys


df = pd.read_csv('./hillingdon-out/hillingdon_buildings.csv', header=None, delimiter=',')
df.columns = ['type', 'x', 'y', 'area']
groups = df.groupby('type').count()

# df = df[df['building']!='yes']
# df.size

# for col in df.columns:
#         print(col)

fig = px.scatter_mapbox(df, lat="y", lon="x",
                        color_discrete_sequence=["crimson"],
                        hover_name="type",
                        zoom=8,  height=800)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
py.offline.plot(fig, filename='name.html')