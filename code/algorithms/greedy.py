from shared_functions import *
import classChip

x, y, z = 0, 0, 0 		# global variables

def move(coordinates, chip):
	id = str(coordinates[0]) + ", " + str(coordinates[1]) + ", " + str(coordinates[2])
	global x, y, z
	if chip.nodes.get(id).is_free:
		x = coordinates[0]
		y = coordinates[1]
		z = coordinates[2]
		chip.nodes.get(id).is_free = False
	else:
		z += 1
		id = str(x) + ", " + str(y) + ", " + str(z)
		if chip.nodes.get(id) is None:
			chip.init_nodes(z)
		chip.nodes.get(id).is_free = False
	return(chip.nodes.get(id))

def greedy(chip, net):
	start, goal = chip.circuit[net[0]] + (0,), chip.circuit[net[1]] + (0,)
	shortest_path = [start]
	node = None
	net_cost = 0
	global x, y, z
	x = chip.circuit[net[0]][0]
	y = chip.circuit[net[0]][1]
	z = 0
	end_x = chip.circuit[net[1]][0]
	end_y = chip.circuit[net[1]][1]

	while (x != end_x or y != end_y or z != 0) and z <= chip.levels:
		if x < end_x:
			node = move((x + 1, y, z), chip)
		elif x > end_x:
			node = move((x - 1, y, z), chip)
		elif y < end_y:
			node = move((x, y + 1, z), chip)
		elif y > end_y:
			node = move((x, y - 1, z), chip)
		else:
			z -= 1
			id = str(x) + ", " + str(y) + ", " + str(z)
			node = chip.nodes.get(id)
			node.is_free = False
		shortest_path.append(node.coordinates)
		net_cost += 1

	# append shortest_path to chip.paths
	shortest_path.append(goal)
	chip.paths.append(classChip.Path(net, shortest_path))

	return net_cost
