import sys
import xml.etree.ElementTree as ET
from parse_osm import *
import numpy as np


Brent_Population = 330795
Avg_HouseHold = 2.6
Total_Num_of_Houses = int(Brent_Population/Avg_HouseHold)

tree = ET.parse('./brent.osm')
root = tree.getroot()

building_types = {}
node_list = build_node_list(root)
poly_list = []
for c1 in root:
  if c1.tag == "way":
    for c2 in c1:
      #<tag k="leisure" v="park"/>
      if c2.tag == "tag":
        if c2.attrib["k"] == "building":
          if c2.attrib["v"] in building_types:
            building_types[c2.attrib["v"]] += 1
          else:
            building_types[c2.attrib["v"]] = 1

          # if c2.attrib["v"] in ["house","apartments","residential"]:
          if c2.attrib["v"] in ["apartments"]:
            p = get_polygon_from_way(c1, node_list)
            if p:
              #print(c2.tag, c2.attrib, p.centroid, calc_geom_area(p))
              # print("house,{},{},{}".format(p.centroid.x, p.centroid.y, int(calc_geom_area(p))))
              poly_list.append((p, p.centroid.x, p.centroid.y, int(calc_geom_area(p))))


Total_Area = 0
for p in poly_list:
  Total_Area += p[3]

for p in poly_list:
  areaPercent = p[3]/Total_Area * 100
  Num_of_Houses = int(Total_Num_of_Houses * areaPercent)
  Houses = random_points_within(p[0], Num_of_Houses)
  for h in Houses:
    print("house,{},{},{}".format(h.x, h.y, p[3]))







# print("Debug: list of leisure types in osm file:", building_types, file=sys.stderr)

