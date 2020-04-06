import sys
import xml.etree.ElementTree as ET
from parse_osm import *

tree = ET.parse(sys.argv[1])
root = tree.getroot()

leisure_types = {}

for c1 in root:
  if c1.tag == "way":
    for c2 in c1:
      #<tag k="leisure" v="park"/>
      if c2.tag == "tag":
        if c2.attrib["k"] == "leisure":
          if c2.attrib["v"] in leisure_types:
            leisure_types[c2.attrib["v"]] += 1
          else:
            leisure_types[c2.attrib["v"]] = 1

          if c2.attrib["v"] in ["park","garden","nature_reserve"]:
            print(c2.tag, c2.attrib)
            print(get_nodes(c1))

node_list = build_node_list(root)

print("Debug: list of leisure types in osm file:", leisure_types)
