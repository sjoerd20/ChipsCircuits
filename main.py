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
	population_size = 20
	width, height = 18, 17

	print("Upper bound (worst case) = ", upper_bound(Chip(circuit, width, height)))

	# make netlist with genetic algorithm
	netlist, total_cost = make_netlist(population_size, circuit, width, height, algorithm, netlist)
	print("Total cost = ", total_cost)

	print("Lower bound = ", lower_bound(circuit, netlist))

	return

def test_algorithm(circuit, width, height, netlist, algorithm):
	print(algorithm.__name__)
	cost = 0
	while cost == 0:
		chip = Chip(circuit, width, height)
		chip.load_chip()
		for net in netlist:
			try:
				cost += algorithm(chip, net, int(random() * 8))
			except KeyError:
				cost = 0
				break
	print("Total cost", algorithm.__name__, " = ", cost)

	# print grid
	visualization.plot_3D(directory + "/results", chip, width, height)
	# visualization.plot_grid(directory + "/results", chip, width, height)
	# visualization.print_simple_grid(chip)

if __name__ == "__main__":
	main()
