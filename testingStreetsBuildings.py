import matplotlib.cm as cm
import matplotlib.colors as colors
import networkx as nx
from IPython.display import Image
from pprint import pprint
import osmnx as ox
import matplotlib.pyplot as plt

ox.config(log_console=True, use_cache=True)
ox.__version__

# configure the inline image display
img_folder = "images"
extension = "svg"
size = 500
tags = {"building": True, "amenity":True, "highway": True, "railway": True}
water_color = 'blue'
land_color = '#ffffff'
bg_color = '#ffffff'
edge_color = "#aaaaaa"

# helper funcion to get one-square-mile street networks, building footprints, and plot them
def make_plot(
    place,
    point,
    network_type="all",
    dpi=1200,
    dist=2000,
    default_width=1,
    street_widths=1,
):
    fp_buildig = f"./{img_folder}/{place}_buildings.{extension}"
    gdf = ox.geometries_from_point(point, tags, dist=dist)
    fig, ax = ox.plot_figure_ground(
        point=point,
        dist=dist,
        filepath=f"./{img_folder}/{place}_buildings.{extension}",
        network_type=network_type,
        default_width=default_width,
        street_widths=street_widths,
        save=True,
        show=False,
        close=True,
    )

    fp_foot = f"./{img_folder}/{place}_streets.{extension}"
    gdf_proj = ox.project_gdf(gdf)
    bbox = ox.utils_geo.bbox_from_point(point=point, dist=dist, project_utm=True)
    fig, ax = ox.plot_footprints(
        gdf_proj,
        bbox=bbox,
        color='#ffffff',
        ax=ax, filepath=f"./{img_folder}/{place}_streets.{extension}",
        dpi=dpi,
        save=True,
        show=False,
        close=True
    )


    fp_all = f"./{img_folder}/{place}_all.{extension}"
    fig, ax = ox.plot_footprints(
        gdf,
        ax=ax, filepath=fp_all, dpi=dpi, save=True, show=False, close=True
    )


place = "Germering"
point = (48.1276189,11.3669227)
#make_plot(place, point)
#make_plot(place, point, network_type="all", default_width=1, street_widths={"primary": 4})
make_plot(place, point, network_type="drive", default_width=1, street_widths={"primary": 4})


#place = "Buchloe"
#point = (48.03589979572741, 10.719189469252361)
#make_plot(place, point)
#make_plot(place, point, network_type="drive", default_width=2, street_widths={"primary": 8})

#place = "Kaufbeuren"
#point = (47.88432038196188, 10.60559658539269)
#make_plot(place, point)
#make_plot(place, point, network_type="all", default_width=2, street_widths={"primary": 6})


#place = "Kaufbeuren2"
#point = (47.88432038196188, 10.60559658539269)
#make_plot(place, point)
#make_plot(place, point, network_type="all", default_width=2, street_widths={"primary": 6})







# get the water bodies
#left, bottom, right, top = land.total_bounds
#bbox = top, bottom, right, left
#poly = ox.utils_geo.bbox_to_poly(*bbox)
#water = ox.geometries_from_polygon(poly, tags={'natural': 'water'})



# specify that we're retrieving building footprint geometries
#tags = {"building": True, "amenity":True, "highway": True}



#gdf = ox.geometries_from_place("Germering, Bavaria, Germany", tags)
#gdf_proj = ox.project_gdf(gdf)
#fig, ax = ox.plot_footprints(gdf_proj, filepath=fp, dpi=400, save=True, show=False, #close=True, color=land_color, bgcolor=bg_color)
#Image(fp, height=size, width=size)

# constrain the plotting window as desired
#c = land.unary_union.centroid
#bbox = ox.utils_geo.bbox_from_point((c.y, c.x), dist=12000)


#fig, ax = ox.plot_footprints(water, bbox=bbox, filepath=fp2,  dpi=400, color=water_color, bgcolor=bg_color,show=False, close=True, save=True)
#ax = land.plot(ax=ax, zorder=0, fc=land_color)
#Image(fp2, height=size, width=size)

#point = (40.7154,-73.9853)
#dist = 3000

#bbox = ox.utils_geo.bbox_from_point(point, dist=dist)
#fp = ox.geometries_from_point(point, tags={'building':True}, dist=dist)
#G = ox.graph_from_point(point, network_type='drive', dist=dist, truncate_by_edge=True, retain_all=True)

#fig, ax = ox.plot_graph(G, bgcolor=bg_color, node_size=0, edge_color=edge_color, show=False)
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
