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
		load circuits and netlists
	"""
	circuits = load_data(directory + "/data/circuits.txt")
	netlists = load_data(directory + "/data/netlists.txt")

	"""
		choose circuit, netlist, algorithm, and size of the chip
	"""

	circuit = circuits.circuit_1
	netlist = netlists.netlist_6
	algorithm = a_star
	width, height = 18, 17

	"""
		state space size and upper/lower bounds for given chip and netlist
	"""
	state_space(circuit, width, height, netlist)

	"""
		make desirable netlist with genetic algorithm
	"""
	population_size = 20
	netlist, fitness = make_netlist(population_size, circuit, width, height, algorithm, netlist)
	total_cost = upper_bound(Chip(circuit, width, height)) - fitness
	# test algorithm with netlist obtained from genetic algorithm
	print("Total cost", algorithm.__name__, " = ", total_cost)

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
