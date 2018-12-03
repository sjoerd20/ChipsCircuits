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

	circuit = circuits.circuit_1
	netlist = netlists.netlist_6
	algorithm = a_star
	population_size, width, height = 14, 18, 17

	print("Upper bound (worst case) = ", upper_bound(Chip(circuit, width, height)))

	population = initial_pop(population_size, circuit, width, height, algorithm, netlist)
	while population[0][1] < len(netlist):
		parents = selection(population, 5)
		population = next_pop(7, circuit, width, height, algorithm, parents)
	netlist = population[0][0]

	test(circuit, width, height, netlist, algorithm)
	test(circuit, width, height, netlist, greedy)

	print("Lower bound =", lower_bound(circuit, netlist))

	"""

	netlist.sort(key=lambda net: distance(circuit[net[0]], circuit[net[1]]))
	test(circuit, 18, 13, netlist, algorithm, "sorted by distance")

	netlist.sort(key=lambda net: area(circuit[net[0]], circuit[net[1]]))
	test(circuit, 18, 13, netlist, algorithm, "sorted by area")

	netlist.sort(key=lambda net: [distance(circuit[net[0]], circuit[net[1]]),
	area(circuit[net[0]], circuit[net[1]])])
	test(circuit, 18, 13, netlist, algorithm, "sorted by distance, then by area")

	population = initial_pop(population_size, circuit, width, height, algorithm, netlist)
	while population[0][1] < len(netlist):
		print(population[0][1], population[-1][1])
		parents = selection(population, 5)
		population = next_pop(7, circuit, width, height, algorithm, parents)
	print(population[0])

	"""

	return


# to test with certain circuits and netlists
def test(circuit, width, height, netlist, algorithm):
	print(algorithm.__name__)
	cost = 0
	while cost == 0:
		chip = Chip(circuit, width, height)
		chip.load_chip()
		for net in netlist:
			try:
				cost += algorithm(chip, net)
			except KeyError:
				cost = 0
				break
	print("Total cost =", cost)

	# print grid
	visualization.plot_grid(directory + "/results", chip, width, height)
	# visualization.print_simple_grid(chip)


if __name__ == "__main__":
	main()
