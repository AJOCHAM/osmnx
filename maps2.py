import matplotlib.pyplot as plt
import networkx as nx
import osmnx as ox

utw = ox.settings.useful_tags_way + ['railway']
ox.config(use_cache=True, log_console=True, useful_tags_way=utw)
dpi=400
dist=3000


# get graphs of different infrastructure types, then combine
place = 'Germering, Bavaria, Germany'
point = (48.1276189,11.3669227)
G1 = ox.graph_from_point(point, dist=dist, custom_filter='["highway"~"residential"]')
G2 = ox.graph_from_point(point, dist=dist, custom_filter='["railway"~"tram|rail"]')
G3 = ox.graph_from_point(point, dist=dist, custom_filter='["building"]')


#G1 = ox.graph_from_place(place, custom_filter='["highway"~"residential"]')
#G2 = ox.graph_from_place(place, custom_filter='["railway"~"tram|rail"]')

Gtemp = nx.compose(G1, G2)
G = nx.compose(Gtemp, G3)


# get building footprints
#fp = ox.footprints_from_place(place)

# plot highway edges in yellow, railway edges in red
ec = ['y' if 'highway' in d else 'r' for _, _, _, d in G.edges(keys=True, data=True)]
fp_buildig = f"./image/Germering_maps2.png"
fig, ax = ox.plot_graph(G, bgcolor='k', edge_color=ec,
                        node_size=0, edge_linewidth=0.5,
                        filepath=fp_buildig,dpi=dpi,
                        show=False, close=False, save=True)

# add building footprints in 50% opacity white
#fp.plot(ax=ax, color='w', alpha=0.5)
#plt.show()
