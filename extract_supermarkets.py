import sys
import xml.etree.ElementTree as ET
from parse_osm import *

def extract_supermarkets(tree):
  for c1 in root:
    if c1.tag == "way":
      for c2 in c1:
        #<tag k="shop" v="supermarket"/>
        if get_tag(c2, "shop") == "supermarket" or get_tag(c2, "amenity") == "supermarket" or get_tag(c2, "other_tags") == "supermarket":
          p = get_polygon_from_way(c1, node_list)
          if p:
            #print(get_nodes(c1))
            #print(c2.tag, c2.attrib, p.centroid, calc_geom_area(p))
            print("supermarket,{},{},{}".format(p.centroid.x, p.centroid.y, int(calc_geom_area(p))))

  print("Debug: list of leisure types in osm file:", leisure_types, file=sys.stderr)

if __name__ == "__main__":
  tree = ET.parse(sys.argv[1])
  root = tree.getroot()

  leisure_types = {}
  node_list = build_node_list(root)

  extract_supermarkets(tree)
