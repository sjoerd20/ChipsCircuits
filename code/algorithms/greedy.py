from shared_functions import *

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

def greedy(chip, net, start_layer = 0):
	net_cost = 0
	global x, y, z
	x = chip.circuit[net[0]][0]
	y = chip.circuit[net[0]][1]
	z = start_layer
	end_x = chip.circuit[net[1]][0]
	end_y = chip.circuit[net[1]][1]

	while (x != end_x or y != end_y or z != 0) and z <= chip.levels:
		if x < end_x:
			move((x + 1, y, z), chip)
		elif x > end_x:
			move((x - 1, y, z), chip)
		elif y < end_y:
			move((x, y + 1, z), chip)
		elif y > end_y:
			move((x, y - 1, z), chip)
		else:
			z -= 1
			id = str(x) + ", " + str(y) + ", " + str(z)
			chip.nodes.get(id).is_free = False
		net_cost += 1

	return net_cost