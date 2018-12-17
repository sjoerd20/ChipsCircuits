"""Visualization

This file contains the code for a 2D and a 3D visualization
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def plot_grid(results_directory, chip):
    """2D grid representation using matplotlib"""

    # Retrieve coordinates of all gates
    x_gates, y_gates = chip.get_gates_coordinates()
    all_paths_coordinates = chip.get_all_paths_coordinates()

    for level in range(chip.levels):
        if level == 0:
            plot_grid_level(results_directory, chip,
                            all_paths_coordinates=all_paths_coordinates,
                            x_gates=x_gates, y_gates=y_gates)
        else:
            plot_grid_level(results_directory, chip,
                            all_paths_coordinates=all_paths_coordinates,
                            level=level)

    return plt.show()


def plot_3D(results_directory, chip):
    """3D plot of the chip"""
    
    # get all gates
    x_gates, y_gates = chip.get_gates_coordinates()
    all_paths_coordinates = chip.get_all_paths_coordinates()

    colors = ["b", "g", "c", "m", "y"]
    #colors = ["k"]
    markers = [".", "^", ",", "v", "<", ">"]
    markers = [""]
    color_index = 0
    marker_index = 0

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # set ticks to step of 1 for correct grid
    x_ticks = range(chip.width)
    y_ticks = range(chip.height)
    z_ticks = range(chip.levels)
    ax.set_xticks(x_ticks)
    ax.set_yticks(y_ticks)
    ax.set_zticks(z_ticks)

    # set all ticks and labels off
    plt.tick_params(
        axis="both",
        which="both",
        bottom=True,
        top=False,
        left=False,
        right=False,
        labelbottom=False,
        labelleft=False)

    if all_paths_coordinates != None:
        for path_coordinates in all_paths_coordinates:
            prev_path_node_coordinate = path_coordinates[0]
            for path_node_coordinate in path_coordinates:
                ax.plot([path_node_coordinate[0],
                        prev_path_node_coordinate[0]],
                        [path_node_coordinate[1],
                        prev_path_node_coordinate[1]],
                        [path_node_coordinate[2],
                        prev_path_node_coordinate[2]],
                        color=colors[color_index],
                        marker=markers[marker_index],
                        markersize=5)
                prev_path_node_coordinate = path_node_coordinate
            color_index = (color_index + 1) % len(colors)
            marker_index = (marker_index + 1) % len(markers)

    # plot gates if provided
    if (x_gates and y_gates) != None:
        ax.plot(x_gates, y_gates, [0 for i in range(len(x_gates))], 'ro', markersize=10)

    # ax.scatter(xs, ys, zs)
    # set correct limits and initiate grid
    plt.title("3D representation of the chip (25 gates) filled with " +
                str(len(all_paths_coordinates)) + " nets")
    ax.set_xlim(0, chip.width)
    ax.set_ylim(0, chip.height)
    ax.set_zlim(0, chip.levels)
    # plt.gca().invert_xaxis()
    plt.gca().invert_yaxis()        # invert the y-axis to get correct view
    # ax.set_axis_off()

    # make the x and y panes transparant
    ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    ax.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    ax.xaxis._axinfo["grid"]['color'] =  (1,1,1,0)
    ax.yaxis._axinfo["grid"]['color'] =  (1,1,1,0)

    plt.savefig(results_directory + "/plot_grid/plot_3D.png")
    return plt.show()


def plot_grid_level(results_directory, chip, all_paths_coordinates=None,
                    x_gates=None, y_gates=None, level=0):
    """Plot a single level of a chip"""

    colors = ["b", "g", "c", "m", "y"]
    markers = [".", "^", ",", "v", "<", ">"]
    color_index = 0
    marker_index = 0

    fig, ax = plt.subplots()
    x_ticks = range(chip.width)      # set ticks to step of 1 for correct grid
    y_ticks = range(chip.height)     # set ticks to step of 1 for correct grid
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

    # plot all paths at current level if provided
    if all_paths_coordinates != None:
        for path_coordinates in all_paths_coordinates:
            prev_path_node_coordinate = path_coordinates[0]
            for path_node_coordinate in path_coordinates:
                if path_node_coordinate[2] == level:
                    ax.plot([path_node_coordinate[0],
                            prev_path_node_coordinate[0]],
                            [path_node_coordinate[1],
                            prev_path_node_coordinate[1]],
                            color=colors[color_index],
                            marker=markers[marker_index])
                prev_path_node_coordinate = path_node_coordinate
            color_index = (color_index + 1) % len(colors)
            marker_index = (marker_index + 1) % len(markers)

    # plot gates if provided
    if (x_gates and y_gates) != None:
        ax.plot(x_gates, y_gates, 'ro')

    # set correct limits and initiate grid
    plt.title("Chip level " + str(level))
    ax.set_xlim(-0.2, chip.width - 0.8)
    ax.set_ylim(-0.2, chip.height - 0.8)
    plt.gca().invert_yaxis()        # invert the y-axis to get correct view
    ax.grid(alpha=1)
    plt.savefig(results_directory + "/plot_grid/plot_grid" + str(level) + ".png")


def plot_bounds(results_directory):
    """Plots the upper and lower bound of the costs in a histogram"""
    lower_bounds_small = [291, 341, 475]
    lower_bounds_small_x = [30, 40, 50]
    lower_bounds_large = [600, 578, 761]
    lower_bounds_large_x = [50, 60, 70]

    fig, ax = plt.subplots(nrows=1, ncols=2)
    bounds_small = ax[0].bar(lower_bounds_small_x, lower_bounds_small, align='center', width=10, edgecolor='k')
    bounds_large = ax[1].bar(lower_bounds_large_x, lower_bounds_large, align='center', width=10, edgecolor='k')

    # n_groups = 3
    # index = np.arange(n_groups)
    # bar_chip.width = 1

    for axes in ax:
        axes.set_xlabel('lengte netlists')
        axes.set_ylabel('kosten')
        axes.set_ylim(0,800)
    ax[0].set_title("Lower bounds for chip with 25 gates")
    ax[1].set_title("Lower bounds for chip with 50 gates")
    # ax[0].set_xticklabels((30, 40, 50))
    # ax[1].set_xticklabels((50, 60, 70))

    fig.tight_layout()
    plt.savefig(results_directory + "lowerbounds.png")
    return plt.show()
