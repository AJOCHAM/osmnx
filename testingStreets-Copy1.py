import matplotlib.cm as cm
import matplotlib.colors as colors
import networkx as nx
from IPython.display import Image
from pprint import pprint
import osmnx as ox

ox.config(log_console=True, use_cache=True)
ox.__version__


# Configuration, or what passes as such
font = {'family': 'Titillium'}
tick_font = {'weight': 'bold', 'zorder': 3}
supertitle_font = {'fontsize': 60, 'y': 1.07, **font}
title_font = {'size': 24, 'weight': 'bold', **font}
xtick_font = {'size': 10, 'alpha': 1.0, **font, **tick_font}
ytick_font = {'size': 9, 'alpha': 0.2, **font, **tick_font}

ox.config(log_console=True, use_cache=True)
weight_by_length = False


# create a graph of Piedmont's drivable street network then plot it
G = ox.graph_from_place('Buchloe, Bavaria, Germany', network_type='drive')

#fig, ax = ox.plot_graph(G)
#fig, ax = ox.plot_graph(G, save=True, show=False, edge_color=#ffffff)
#fig, ax = ox.plot_graph(M, ax=None, figsize=(8, 8), bgcolor='#111111', node_color='w', node_size=15, node_alpha=None, node_edgecolor='none', node_zorder=1, edge_color='#999999', edge_linewidth=1, edge_alpha=None, show=True, close=False, save=True, filepath=None, dpi=600, bbox=None)
#ox.plot_graph(M, save=True, show=False)
#ox.plot_graph(D, save=True, show=False)

# calculate node closeness centrality of the line graph
edge_centrality = nx.closeness_centrality(nx.line_graph(G))

# make a list of graph edge centrality values
ev = [edge_centrality[edge + (0,)] for edge in G.edges()]

# create a color scale converted to list of colors for graph edges
norm = colors.Normalize(vmin=min(ev)*0.8, vmax=max(ev))
#cmap = cm.ScalarMappable(norm=norm, cmap=cm.inferno)
cmap = cm.ScalarMappable(norm=norm, cmap=cm.viridis)
ec = [cmap.to_rgba(cl) for cl in ev]

# color the edges in the original graph by closeness centrality in line graph
fig, ax = ox.plot_graph(G, bgcolor='black', node_size=0, edge_color=ec, edge_linewidth=1, edge_alpha=1, show=True, close=True, save=True)