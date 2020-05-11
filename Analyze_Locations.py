import plotly.express as px
import plotly.graph_objects as go
import  plotly as py
import pandas as pd
import sys

def GetColor(type):
    return "red"

df = pd.read_csv('./brent-out/brent_buildings.csv', header=None, delimiter=',')
df.columns = ['type', 'x', 'y', 'area']
groups = df.groupby('type').count()
type = ['hospital', 'house', 'office', 'park', 'leisure', 'school', 'supermarket', 'shopping']
df['color'] = 0
for index, row in df.iterrows():
    df['color'][index] = type.index(row['type'])
# df = df[df['building']!='yes']
# df.size

# for col in df.columns:
#         print(col)

fig = px.scatter_mapbox(df, lat="y", lon="x",
                        hover_name="type",
                        color = 'color',
                        color_continuous_scale=["darkgreen", "crimson", "orange", "lightgreen", "gold", "purple", "blue", "blue"],
                        zoom=8,  height=800)
fig.update_layout(mapbox_style="open-street-map")
py.offline.plot(fig, filename='name.html')