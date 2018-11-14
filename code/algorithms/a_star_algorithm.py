import shared_functions as sf

# entry point of a_star algorithm
def a_star(chip, netlist):

    # perform algorithm for each net in netlists
    for net in netlist:

        curr_x = circuit[net[0]][0]
    	curr_y = circuit[net[0]][1]
        curr_z = 0

        end_x = circuit[net[1]][0]
    	end_y = circuit[net[1]][1]

    """
    for each net in netlist

    start at current_node and go to end_node

    at current node go to all posible directions and check if is_free

    check minimum_distance for each direction to end_node

    keep all in memory, but advance with the one(s) with the shortest minimum_distance

    if older node shorter minimum_distance advance with that nodes

    repeat until reached end_node

    remember this path

    """
    return

# A* star algorithm for finding shortest path between two points
def a_star_algorithm(curr_x, curr_y, curr_z, end_x, end_y):
    return
