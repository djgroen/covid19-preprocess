import sys
import xml.etree.ElementTree as ET
import pyproj
from shapely.geometry import Polygon

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
      nodes.append(int(c2.attrib["ref"]))
      if verbose:
        print(c2.attrib["ref"])
  return nodes

def get_polygon_from_way(way, node_list, verbose=False):
  nodes = get_nodes(way, verbose)
  poly_nodes = []
  for i in nodes:
    try:
      poly_nodes.append(node_list[i])
    except KeyError:
      print("Warning: node with key {} is not found, ignoring it...".format(i), file=sys.stderr)
  if len(poly_nodes) > 3:
    return Polygon(poly_nodes)
  else:
    print("Warning: location has fewer than 3 valid nodes. Omitting it.", file=sys.stderr)
    return None
  
  # Credit to https://gis.stackexchange.com/questions/127607/area-in-km-from-polygon-of-coordinates
  # User jczaplew
def calc_geom_area(poly):
  poly = ops.transform(
  partial(
      pyproj.transform,
      pyproj.Proj(init='EPSG:4326'),
      pyproj.Proj(
          proj='aea',
          lat1=poly.bounds[1],
          lat2=poly.bounds[3])),
  geom)
    # Print the area in m^2
    return geom_area.area 
