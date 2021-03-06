from random import randrange
from matplotlib import pyplot as plt

import os

cwd = os.getcwd()
plots_dir = os.path.join(cwd, "plots")

try:
    os.mkdir(plots_dir)
    plot_name = "plot1.png"
except:
    plots = len(os.listdir(plots_dir)) + 1
    plot_name = f"plot{plots}.png"
    plot_path =  os.path.join(plots_dir, plot_name)


origin = [0,0] # point A
base_vertex = [10, 0] # point B
max_x = 10
min_y = 0
top_vertex = [randrange(1,11), randrange(1,11)] # point C

x = [ origin[0] , base_vertex[0] , top_vertex[0] ]
y = [ origin[1] , base_vertex[1] , top_vertex[1] ]

def get_point(die_roll):

    # alloting points to vertex
    a = (1, 2)
    b = (3, 4)
    c = (5, 6)

    if die_roll in a:
        return origin
    elif die_roll in b:
        return base_vertex
    else:
        return top_vertex

starting_point = origin

for _ in range(100000):

    die_roll = randrange(1, 7)
    destination_point = get_point(die_roll)
    mid_x = ( starting_point[0] + destination_point[0] ) / 2
    mid_y = ( starting_point[1] + destination_point[1] ) / 2

    x.append(mid_x)
    y.append(mid_y)

    starting_point = [mid_x, mid_y]

plt.scatter(x, y, s=4)
plt.savefig(plot_path)
plt.show()