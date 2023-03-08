import matplotlib.cm as cm
import matplotlib.colors as colors
import networkx as nx
from IPython.display import Image
from pprint import pprint
import osmnx as ox
import matplotlib.pyplot as plt

ox.config(log_console=True, use_cache=True)
ox.__version__



center_point = (48.1276189,11.3669227)
G = ox.graph_from_point(center_point, dist=15000, retain_all=True, simplify = True, network_type='all')


###############################################################################
#                               4. Unpack Data                                #
###############################################################################
u = []
v = []
key = []
data = []
for uu, vv, kkey, ddata in G.edges(keys=True, data=True):
    u.append(uu)
    v.append(vv)
    key.append(kkey)
    data.append(ddata)


# Lists to store colors and widths
roadColors = []
roadWidths = []

for item in data:
    if "footway" in item["highway"]:
        color = "#ededed"
        linewidth = 0.25
    else:
        color = "#a6a6a6"
        linewidth = 0.5

    roadWidths.append(linewidth)



#Center of the map
latitude = 48.1276189
longitude = 11.3669227

#Limit borders
north = latitude + 0.15
south = latitude - 0.15
east = longitude + 0.15
west = longitude - 0.15

bgcolor = "#061529"

fig, ax = ox.plot_graph(G, node_size=0, bbox = (north, south, east, west),
                        dpi = 300,bgcolor = bgcolor,
                        save = False, edge_color=roadColors,
                        edge_linewidth=roadWidths, edge_alpha=1)

fig.tight_layout(pad=0)
fig.savefig("madrid.png", dpi=300, bbox_inches='tight', format="png",
            facecolor=fig.get_facecolor(), transparent=False)



#ADD WATER

G1 = ox.graph_from_point(center_point, dist=15000, dist_type='bbox', network_type='all',
                         simplify=True, retain_all=True, truncate_by_edge=False,
                         clean_periphery=False, custom_filter='["natural"~"water"]')

G2 = ox.graph_from_point(center_point, dist=15000, dist_type='bbox', network_type='all',
                         simplify=True, retain_all=True, truncate_by_edge=False,
                         clean_periphery=False, custom_filter='["waterway"~"river"]')

Gwater = nx.compose(G1, G2)


u = []
v = []
key = []
data = []
for uu, vv, kkey, ddata in Gwater.edges(keys=True, data=True):
    u.append(uu)
    v.append(vv)
    key.append(kkey)
    data.append(ddata)


# List to store colors
roadColors = []
roadWidths = []

# #72b1b1
# #5dc1b9
for item in data:
    if "name" in item.keys():
        if item["length"] > 400:
            color = "#72b1b1"
            linewidth = 2
        else:
            color = "#72b1b1"
            linewidth = 0.5
    else:
        color = "#72b1b1"
        linewidth = 0.5

    roadColors.append(color)
    roadWidths.append(linewidth)


    fig, ax = ox.plot_graph(Gwater, node_size=0,figsize=(27, 40),
                        dpi = 300, save = False, edge_color=roadColors,
                        edge_linewidth=roadWidths, edge_alpha=1)

fig.tight_layout(pad=0)
fig.savefig("water.png", dpi=300, format="png", bbox_inches='tight',
            facecolor=fig.get_facecolor(), transparent=True)


            
