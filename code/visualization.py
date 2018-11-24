# TODO implement a better visualization
import matplotlib.pyplot as plt
import numpy as np
from termcolor import colored

# print the circuit as a simple grid consisting of seperated layers
def print_simple_grid(chip):
    for z in range(chip.levels):
        print("Layer", z)
        for y in range(chip.height):
            for x in range(chip.width):
                print("|",end="")
                id = str(x) + ", " + str(y) + ", " + str(z)
                if chip.nodes.get(id) is None:
                    print(" ",end="")
                elif chip.nodes.get(id).is_free:
                    print(" ",end="")
                elif chip.nodes.get(id).is_gate:
                    print(colored("o", "red"),end="")
                else:
                    print("-",end="")
            print("|")

# grid representation with matplotlib
def plot_grid(results_directory, chip, width, height):

    # get all gates
    x_gates, y_gates = chip.get_gates_coordinates()
    # L_x_nodes_used, L_y_nodes_used, L_z_nodes_used = chip.get_walls_coordinates()

    all_paths_coordinates = chip.get_all_paths_coordinates()

    # print gates at grid layer 0
    plot_grid_level(results_directory, width, height, x_gates=x_gates, y_gates=y_gates)

    plt.show()
    return

# plot single grid layer
def plot_grid_level(results_directory, width, height, x_nodes_used=None,
                    y_nodes_used=None, x_gates=None, y_gates=None, level=0):
    fig, ax = plt.subplots()
    x_ticks = range(width)      # set ticks to step of 1 for correct grid
    y_ticks = range(height)     # set ticks to step of 1 for correct grid
    ax.set_xticks(x_ticks)
    ax.set_yticks(y_ticks)

    # set all ticks and labels off
    plt.tick_params(
        axis="both",
        which="both",
        bottom=False,
        top=False,
        left=False,
        right=False,
        labelbottom=False,
        labelleft=False)

    if (x_gates and y_gates) != None:
        ax.plot(x_gates, y_gates, 'ro')
    if (x_nodes_used and y_nodes_used) != None:
        ax.plot(x_nodes_used, y_nodes_used, 'bo')

    # set correct limits and initiate grid
    ax.set_xlim(0, width - 1)
    ax.set_ylim(0, height - 1)
    plt.gca().invert_yaxis()        # invert the y-axis to get correct view
    ax.grid(alpha=1)
    plt.savefig(results_directory + "/plot_grid/plot_grid" + str(level) + ".png")

    return
