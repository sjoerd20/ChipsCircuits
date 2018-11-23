from shared_functions import *

def greedy(chip, net):
	net_cost = 0
	x = chip.circuit[net[0]][0]
	y = chip.circuit[net[0]][1]
	z = 0
	end_x = chip.circuit[net[1]][0]
	end_y = chip.circuit[net[1]][1]

	while (x != end_x or y != end_y or z != 0) and z <= chip.levels:

		if x < end_x:
			id = str(x + 1) + ", " + str(y) + ", " + str(z)
			if chip.nodes.get(id).is_free:
				x += 1
				chip.nodes.get(id).is_free = False
			else:
				z += 1
				id = str(x) + ", " + str(y) + ", " + str(z)
				if chip.nodes.get(id) is None:
					chip.init_nodes(z)
				chip.nodes.get(id).is_free = False

		elif x > end_x:
			id = str(x - 1) + ", " + str(y) + ", " + str(z)
			if chip.nodes.get(id).is_free:
				x -= 1
				chip.nodes.get(id).is_free = False
			else:
				z += 1
				id = str(x) + ", " + str(y) + ", " + str(z)
				if chip.nodes.get(id) is None:
					chip.init_nodes(z)
				chip.nodes.get(id).is_free = False

		elif y < end_y:
			id = str(x) + ", " + str(y + 1) + ", " + str(z)
			if chip.nodes.get(id).is_free:
				y += 1
				chip.nodes.get(id).is_free = False
			else:
				z += 1
				id = str(x) + ", " + str(y) + ", " + str(z)
				if chip.nodes.get(id) is None:
					chip.init_nodes(z)
				chip.nodes.get(id).is_free = False

		elif y > end_y:
			id = str(x) + ", " + str(y - 1) + ", " + str(z)
			if chip.nodes.get(id).is_free:
				y -= 1
				chip.nodes.get(id).is_free = False
			else:
				z += 1
				id = str(x) + ", " + str(y) + ", " + str(z)
				if chip.nodes.get(id) is None:
					chip.init_nodes(z)
				chip.nodes.get(id).is_free = False
		else:
			z -= 1
			id = str(x) + ", " + str(y) + ", " + str(z)
			chip.nodes.get(id).is_free = False

		net_cost += 1

	return net_cost
