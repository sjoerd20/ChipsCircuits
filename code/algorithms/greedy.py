from shared_functions import *
from chip import Chip
from path import Path

x, y, z = 0, 0, 0 		# global variables

def move(coordinates, chip):
	"""Move to an adjacent point in the chip"""
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
	"""Greedy algorithm tries to move from gate to gate as directly as possible"""
	start, goal = chip.circuit[net[0]] + (0,), chip.circuit[net[1]] + (0,)
	shortest_path = [start]
	node = None
	net_cost = 0
	global x, y, z
	x = start[0]
	y = start[1]
	z = 0
	goal_x = goal[0]
	goal_y = goal[1]

	while (x != goal_x or y != goal_y or z != 0) and z <= chip.levels:
		if x < goal_x:
			node = move((x + 1, y, z), chip)
		elif x > goal_x:
			node = move((x - 1, y, z), chip)
		elif y < goal_y:
			node = move((x, y + 1, z), chip)
		elif y > goal_y:
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
	chip.paths.append(Path(net, shortest_path))

	return net_cost
