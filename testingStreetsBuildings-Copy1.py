import matplotlib.cm as cm
import matplotlib.colors as colors
import networkx as nx
from IPython.display import Image
from pprint import pprint
import osmnx as ox
import matplotlib.pyplot as plt

ox.config(log_console=True, use_cache=True)
ox.__version__

# add more items here to get all the landforms you want
places = ['Munich, Bavaria, Germany'] # 'Brooklyn, NY, USA', 'Queens, NY, USA', 'Bronx, NY, USA'
land = ox.geocode_to_gdf(places)

# Configuration, or what passes as such
font = {'family': 'Titillium'}
tick_font = {'weight': 'bold', 'zorder': 3}
supertitle_font = {'fontsize': 60, 'y': 1.07, **font}
title_font = {'size': 24, 'weight': 'bold', **font}
xtick_font = {'size': 10, 'alpha': 1.0, **font, **tick_font}
ytick_font = {'size': 9, 'alpha': 0.2, **font, **tick_font}
water_color = 'blue'
land_color = '#3a3a3a'
bg_color = '#ffffff'
edge_color = "#aaaaaa"

# configure the inline image display
img_folder = "images"
extension = "png"
size = 240

fp = f"./{img_folder}/Munich_bldgs.{extension}"
fp2 = f"./{img_folder}/Munich_water.{extension}"
fp3 = f"./{img_folder}/Munich_foot.{extension}"





def make_plot(
    place,
    point,
    network_type="drive",
    dpi=400,
    dist=1000,
    default_width=4,
    street_widths=None,
):
    fp = f"./{img_folder}/{place}.{extension}"
    gdf = ox.geometries_from_point(point, tags, dist=dist)
    fig, ax = ox.plot_figure_ground(
        point=point,
        dist=dist,
        network_type=network_type,
        default_width=default_width,
        street_widths=street_widths,
        save=False,
        show=False,
        close=True,
    )
    fig, ax = ox.plot_footprints(
        gdf, ax=ax, filepath=fp, dpi=dpi, save=True, show=False, close=True
    )




# get the water bodies
left, bottom, right, top = land.total_bounds
bbox = top, bottom, right, left
poly = ox.utils_geo.bbox_to_poly(*bbox)
water = ox.geometries_from_polygon(poly, tags={'natural': 'water'})



# specify that we're retrieving building footprint geometries
tags = {"building": True, "amenity":True, "highway": True}



gdf = ox.geometries_from_place("Germering, Bavaria, Germany", tags)
gdf_proj = ox.project_gdf(gdf)
fig, ax = ox.plot_footprints(gdf_proj, filepath=fp, dpi=400, save=True, show=False, close=True, color=land_color, bgcolor=bg_color)
Image(fp, height=size, width=size)

# constrain the plotting window as desired
c = land.unary_union.centroid
bbox = ox.utils_geo.bbox_from_point((c.y, c.x), dist=2000)


fig, ax = ox.plot_footprints(water, bbox=bbox, filepath=fp2,  dpi=400, color=water_color, bgcolor=bg_color,show=False, close=True, save=True)
ax = land.plot(ax=ax, zorder=0, fc=land_color)
Image(fp2, height=size, width=size)

point = (40.7154,-73.9853)
dist = 3000

bbox = ox.utils_geo.bbox_from_point(point, dist=dist)
fp = ox.geometries_from_point(point, tags={'building':True}, dist=dist)
G = ox.graph_from_point(point, network_type='drive', dist=dist, truncate_by_edge=True, retain_all=True)

fig, ax = ox.plot_graph(G, bgcolor=bg_color, node_size=0, edge_color=edge_color, show=False)
#fig, ax = ox.plot_footprints(fp3, ax=ax, filepath=fp3, bbox=bbox, color=bg_color, save=True)


#place = "portland_buildings"
#point = (45.517309, -122.682138)
#make_plot(place, point)

#place = "port_au_prince_buildings"
#point = (18.522240, -72.347607)
#make_plot(place, point, network_type="all", default_width=1, street_widths={"secondary": 3})

#place = "monrovia_liberia_buildings"
#point = (6.340236, -10.747255)
#make_plot(place, point, network_type="all", default_width=2, street_widths={"primary": 6})


place = "GermeringBuildings"
point = (48.1276189,11.3669227)
make_plot(place, point, network_type="all", default_width=2, street_widths={"primary": 6})