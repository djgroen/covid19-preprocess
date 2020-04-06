import sys
import xml.etree.ElementTree as ET

def build_node_list(root, verbose=False):
  node_list = {}
  for c1 in root:
    if c1.tag == "node":
      x = float(c1.attrib["lon"])
      y = float(c1.attrib["lat"])
      i = int(c1.attrib["id"])
      node_list[i] = [x,y]

  if verbose:
    for k in node_list:
      print(k,node_list[k])
  return node_list
              

def get_nodes(way):
  for c2 in way:
    if c2.tag == "nd":
      print(c2.attrib["ref"])

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
            #get_nodes(c1)

build_node_list(root)

print(leisure_types)
