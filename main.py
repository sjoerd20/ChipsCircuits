# add directories to path
import sys, os
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code" , "algorithms"))

from classChip import *
from load_data import load_data
from a_star import *
from greedy import *
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

	netlist.sort(key=lambda net: area(circuit[net[0]], circuit[net[1]]))
	test(circuit, 18, 13, netlist, algorithm, "unsorted")

	"""

	netlist.sort(key=lambda net: distance(circuit[net[0]], circuit[net[1]]))
	test(circuit, 18, 13, netlist, algorithm, "sorted by distance")

	netlist.sort(key=lambda net: area(circuit[net[0]], circuit[net[1]]))
	test(circuit, 18, 13, netlist, algorithm, "sorted by area")

	netlist.sort(key=lambda net: [distance(circuit[net[0]], circuit[net[1]]),
	area(circuit[net[0]], circuit[net[1]])])
	test(circuit, 18, 13, netlist, algorithm, "sorted by distance, then by area")

	"""

	return


# to test with certain circuits and netlists
def test(circuit, width, height, netlist, algorithm, sort):
	print(algorithm.__name__)
	print("circuit of length", width, "and height", height)
	print(netlist)

	cost = 0
	chip = Chip(circuit, width, height)
	chip.load_chip()
	for net in netlist:
		print((net[0], net[1]))
		cost += algorithm(chip, net)
	print("Total cost, " + sort + " =", cost)

	print("Lower bound =", lower_bound(circuit, netlist))
	print()

	# print grid
	visualization.print_simple_grid(chip)


if __name__ == "__main__":
	main()
