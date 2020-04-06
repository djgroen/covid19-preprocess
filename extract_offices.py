import sys
import xml.etree.ElementTree as ET
from parse_osm import *

def extract_offices(tree):
  for c1 in root:
    if c1.tag == "way":
      for c2 in c1:
        #<tag k="shop" v="supermarket"/>
        if get_tag(c2, "building") == "office" or get_tag(c2, "office"):
          p = get_polygon_from_way(c1, node_list)
          if p:
            #print(get_nodes(c1))
            #print(c2.tag, c2.attrib, p.centroid, calc_geom_area(p))
            print("office,{},{},{}".format(p.centroid.x, p.centroid.y, int(calc_geom_area(p))))


if __name__ == "__main__":
  tree = ET.parse(sys.argv[1])
  root = tree.getroot()

  leisure_types = {}
  node_list = build_node_list(root)

  extract_offices(tree)
