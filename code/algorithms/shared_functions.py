import os

import visualization
from chip import Chip

parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def distance(coords_a, coords_b):
	"""Returns distance between two-dimensional points"""
	return abs(coords_a[0] - coords_b[0]) + abs(coords_a[1] - coords_b[1])


def area(coords_a, coords_b):
	"""Returns area between two-dimensional points"""
	return abs(coords_a[0] - coords_b[0]) * abs(coords_a[1] - coords_b[1])


def heuristic(coords_a, coords_b):
	"""Returns distance between three-dimensional points"""
	return abs(coords_a[0] - coords_b[0]) + abs(coords_a[1] - coords_b[1]) \
			+ abs(coords_a[2] - coords_b[2])


def gate_density(chip, coordinates, start, goal):
	"""Calculates how many gates are nearby; used to avoid 'blocking' gates"""
	dist = 0
	for gate in chip.gates:
		if heuristic(gate.coordinates, coordinates) == 1 \
					and gate.coordinates != start and gate.coordinates != goal:
			dist += 10
	return dist


def fitness(chip, netlist, algorithm, do_visualization = False):
	"""Fitness function working on an algorithm"""
	chip.empty()
	cost = 0
	for index, net in enumerate(netlist):
		try:
			cost += algorithm(chip, net)
		except KeyError:
			return index
	if do_visualization == True:
		visualization.plot_3D(parent_dir + "/results", chip)
		visualization.plot_grid(parent_dir + "/results", chip)
	return upper_bound(chip) - cost


def lower_bound(circuit, netlist):
	"""Returns the lower bound of the costs"""
	lower_bound = 0
	for net in netlist:
		lower_bound += distance(circuit[net[0]], circuit[net[1]])
	return lower_bound


def upper_bound(chip):
	"""Returns the upper bound of the costs"""
	return chip.width * chip.height * chip.max_levels


def factorial(n):
	"""Returns the factorial of a whole number n"""
	if n < 2:
		return 1
	return n * factorial(n - 1)


def scientific_notation(n):
	"""Returns the scientific notation of a number n with one decimal"""
	s = str(n)
	return s[0] + '.' + s[1] + ' * 10 ^ ' + str(len(s))


def walks(chip):
	# can only go in two directions from the corners on the outer layers (lowest and highest)
	walks =  2 ** (2 * 4)
	# can only go in three directions from all other corners, and on the outer circle on the outer layers
	walks *= 3 ** (2 * (2 * chip.width + 2 * chip.height - 8) + (chip.max_levels - 2) * 4)
	# can only go in four directions on the outer circle on other layers, and on all other spaces on the outer layers
	walks *= 4 ** ((chip.max_levels - 2) * (2 * chip.width + 2 * chip.height - 8) + 2 * (chip.width - 2)*(chip.height - 2))
	# on all other spaces, we can go in AT MOST 5 directions
	walks *= 5 ** ((chip.max_levels - 2) * (chip.width - 2) * (chip.height - 2))
	return walks


def state_space(circuit, width, height, netlist):
	"""Calculates the statespace of the chip and netlists"""
	chip = Chip(circuit, width, height)
	print("Upper bound (worst case) = ", upper_bound(chip))

	netlist_configurations = factorial(len(netlist))
	print("Number of different netlist configurations = ", scientific_notation(netlist_configurations))
	print("Number of possible walks per netlist = ", scientific_notation(walks(chip)))
	print("Maximum state space size = ", scientific_notation(netlist_configurations * walks(chip)))
	print("Lower bound = ", lower_bound(circuit, netlist))
	print()
