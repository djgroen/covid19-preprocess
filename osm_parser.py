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
              

def get_nodes(way, verbose=False):
  nodes = []
  for c2 in way:
    if c2.tag == "nd":
      nodes.append(c2.attrib["ref"])
      if verbose:
        print(c2.attrib["ref"])
  return nodes

