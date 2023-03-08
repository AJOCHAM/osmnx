import prettymaps

from matplotlib.font_manager import FontProperties

plot = prettymaps.plot(
    (41.39491,2.17557),
    preset = 'barcelona',
)

# Change background color
plot.fig.patch.set_facecolor('#F2F4CB')
# Add title
plot.ax.set_title(
    'Barcelona',
    fontproperties = FontProperties(
        fname = '../assets/PermanentMarker-Regular.ttf',
        size = 50
    )
)

plot.show()