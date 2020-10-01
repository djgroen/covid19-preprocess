from pyrosm import OSM
from pyrosm import get_data
import geopandas
import numpy as np
import os
import matplotlib.pyplot as plt
from pyrosm.data import sources
import pyrosm
from shapely import geometry
from shapely.geometry import Polygon
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import plotly.express as px
import  plotly as py
from urllib.request import urlopen
import json
import pandas as pd
import plotly.graph_objects as go
import folium
import sys
import xml.etree.ElementTree as ET
import pyproj
from shapely import ops
from functools import partial
from shapely.geometry import Polygon, Point
import random
import csv

def get_area(poly):
    geom_area = ops.transform(
        partial(
            pyproj.transform,
            pyproj.Proj('EPSG:4326'),
            pyproj.Proj(
                proj='aea',
                lat_1=poly.bounds[1],
                lat_2=poly.bounds[3])),
        poly)
    # Print the area in m^2
    return geom_area.area

def Parse(loc_type, loc_attributes, nodes, ways, rel):
    global list
    locations = osm.get_data_by_custom_criteria(custom_filter={loc_type : loc_attributes},
                                                filter_type="keep",
                                                keep_nodes= nodes,
                                                keep_ways= ways,
                                                keep_relations= rel)

    for index, row in locations.iterrows():
        p = row['geometry'].centroid
        if (row['osm_type'] == 'node'):
            area = 100
        else:
            area = int(get_area(row['geometry']))

        out = {'type': row[loc_type], 'name' : row['name'], 'x': p.x, 'y': p.y, 'area': area}
        list.append(out)


brunel_points = pd.read_csv('./OSM Parser/Brunel.csv')
points = []
for index, row in brunel_points.iterrows():
    p = Point(row['lat'], row['lon'])
    points.append(p)

poly = Polygon(points)

osm = pyrosm.OSM('./OSM Parser/Brunel.osm.pbf')
building_types = ['park','hospital', 'office', 'school', 'leisure', 'shopping', 'academic', 'lecturehall', 'residential', 'recreational', 'library', 'sports']
leisure_types = ['recreational', 'park', 'sports']
amenity_types = ['supermarket', 'shop', 'cafe', 'bar', 'parking', 'hospital', 'pharmacy']
list = []

Parse('building', building_types, True, True, True)
Parse('leisure', leisure_types, True, True, True)
Parse('amenity', amenity_types, True, True, True)

df = pd.DataFrame(list)
df.to_csv('./OSM Parser/brunel_buildings.csv', index=False)