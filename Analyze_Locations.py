import plotly.express as px
import plotly.graph_objects as go
import  plotly as py
import pandas as pd
import sys


df = pd.read_csv('./hillingdon-out/hillingdon_buildings.csv', header=None, delimiter=',')
df.columns = ['type', 'x', 'y', 'area']
groups = df.groupby('type').count()
