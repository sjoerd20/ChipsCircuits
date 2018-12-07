# add directories to path
import sys, os
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "results"))
sys.path.append(os.path.join(directory, "code" , "algorithms"))

from classChip import *
from load_data import load_data
from a_star import *
from greedy import *
from genetic import *
import visualization

def main():

	"""
	load net lists
	"""
	circuits = load_data(directory + "/data/circuits.txt")
	netlists = load_data(directory + "/data/netlists.txt")

	circuit = circuits.circuit_0
	netlist = netlists.netlist_1
	algorithm = a_star
	population_size, width, height = 40, 18, 13

	print("Upper bound (worst case) = ", upper_bound(Chip(circuit, width, height)))

	# print("Lower bound =", lower_bound(circuit, netlist))

	"""

	netlist.sort(key=lambda net: distance(circuit[net[0]], circuit[net[1]]))
	test(circuit, 18, 13, netlist, algorithm, "sorted by distance")

	netlist.sort(key=lambda net: area(circuit[net[0]], circuit[net[1]]))
	test(circuit, 18, 13, netlist, algorithm, "sorted by area")

	netlist.sort(key=lambda net: [distance(circuit[net[0]], circuit[net[1]]),
	area(circuit[net[0]], circuit[net[1]])])
	test(circuit, 18, 13, netlist, algorithm, "sorted by distance, then by area")

	"""

	# population = initial_pop(population_size, circuit, width, height, algorithm, netlist)
	# while population[0][1] < len(netlist):
	# 	print(population[0][1], population[-1][1])
	# 	parents = selection(population, 8)
	# 	population = next_pop(7, circuit, width, height, algorithm, parents, netlist)
	# 	mutate_pop(population, 0.1)
	# print(population[0])

	netlist = [(23, 8), (3, 0), (11, 24), (22, 16), (23, 4), (10, 4), (3, 5),
	(3, 15), (9, 13), (3, 4), (1, 0), (3, 23), (7, 13), (5, 7), (15, 21),
	(13, 18), (22, 11), (15, 8), (10, 7), (22, 13), (20, 19), (19, 2), (16, 9),
	(15, 17), (6, 14), (15, 5), (7, 9), (19, 5), (20, 10), (2, 20)]

	test(circuit, width, height, netlist, algorithm)
	# test(circuit, width, height, netlist, greedy)

	return


# to test with certain circuits and netlists
def test(circuit, width, height, netlist, algorithm):
	print(algorithm.__name__)
	cost = 0
	new_index = 0
	max_index = 0
	print("circuit of length", width, "and height", height)
	print("Upper bound (worst case) =", upper_bound(Chip(circuit, width, height)))

	while cost == 0:
		chip = Chip(circuit, width, height)
		chip.load_chip()
		for net in netlist:
			try:
				cost += algorithm(chip, net)
			except KeyError:
				cost = 0
				break
	print("Total cost", algorithm.__name__, " = ", cost)

	print("Lower bound =", lower_bound(circuit, netlist))
	print()

	# print grid
	visualization.plot_3D(directory + "/results", chip, width, height)
	visualization.plot_grid(directory + "/results", chip, width, height)
	# visualization.print_simple_grid(chip)


if __name__ == "__main__":
	main()
