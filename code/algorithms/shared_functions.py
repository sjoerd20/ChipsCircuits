# put all functions that is used by multiple algorithms
from classChip import *

# distance between two-dimensional points
def distance(coords_a, coords_b):
	return abs(coords_a[0] - coords_b[0]) + abs(coords_a[1] - coords_b[1])

# area between two-dimensional points
def area(coords_a, coords_b):
	return abs(coords_a[0] - coords_b[0]) * abs(coords_a[1] - coords_b[1])
	
# distance between three-dimensional points
def heuristic(coords_a, coords_b):
	return abs(coords_a[0] - coords_b[0]) + abs(coords_a[1] - coords_b[1]) + abs(coords_a[2] - coords_b[2])

# calculates how many gates are nearby; used to avoid 'blocking' gates
def gate_density(chip, coordinates, goal):
	dist = 0
	for gate in chip.gates:
		if heuristic(gate.coordinates, coordinates) < 4 and gate.coordinates != goal:
			dist += 1
	return dist

# largest lower bound
def lower_bound(circuit, netlist):
	lower_bound = 0
	for net in netlist:
		lower_bound += distance(circuit[net[0]], circuit[net[1]])
	return lower_bound

# smallest upper bound
def upper_bound(chip):
	return chip.width * chip.height * chip.max_levels

def factorial(n):
		if n < 2:
			return 1
		return n * factorial(n - 1)

def scientific_notation(n):
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
	"""
		print the upper bound for the given chip
	"""
	chip = Chip(circuit, width, height)
	print("Upper bound (worst case) = ", upper_bound(chip))

	"""
		print the size of the state space of solutions for a given chip size and netlist size
	"""
	netlist_configurations = factorial(len(netlist))
	print("Number of different netlist configurations = ", scientific_notation(netlist_configurations))
	print("Number of possible walks per netlist = ", scientific_notation(walks(chip)))
	print("Total state space size = ", scientific_notation(netlist_configurations * walks(chip)))

	"""
		print the lower bound for the given circuit and netlist
	"""
	print("Lower bound = ", lower_bound(circuit, netlist))
