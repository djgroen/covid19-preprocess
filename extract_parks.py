import sys
import xml.etree.ElementTree as ET


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
            get_nodes(c1)


print(leisure_types)
