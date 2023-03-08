import uuid

import typer
import vsketch
from   prettymaps import *
import matplotlib.font_manager as fm
from   matplotlib import pyplot as plt


def draw(location:str='Old Town, Tallinn',
         radius:int=1000,
         width:int=12,
         height:int=12):
    fig, ax = plt.subplots(figsize=(width, height),
                           constrained_layout=True)

    backup = plot(
        location,
        radius=radius,
        ax=ax,
        layers = {
            'perimeter': {},
            'streets': {
                'custom_filter':
                    '["highway"~"motorway|trunk|primary|'
                      'secondary|tertiary|residential|service|'
                      'unclassified|pedestrian|footway"]',
                'width': {
                    'motorway': 5,
                    'trunk': 5,
                    'primary': 4.5,
                    'secondary': 4,
                    'tertiary': 3.5,
                    'residential': 3,
                    'service': 2,
                    'unclassified': 2,
                    'pedestrian': 2,
                    'footway': 1,
                }
            },
            'building': {'tags': {'building': True,
                                  'landuse': 'construction'},
                         'union': False},
            'water': {'tags': {'natural': ['water', 'bay']}},
            'green': {'tags': {'landuse': 'grass',
                               'natural': ['island', 'wood'],
                               'leisure': 'park'}},
            'forest': {'tags': {'landuse': 'forest'}},
            'parking': {'tags': {'amenity': 'parking',
                                 'highway': 'pedestrian',
                                 'man_made': 'pier'}}
        }
    )

    filename = str(uuid.uuid4()).split('-')[0] + '.png'
    plt.savefig(filename)
    print(filename)


if __name__ == "__main__":
    typer.run(draw)