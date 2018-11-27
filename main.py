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
	netlist = netlists.netlist_1[:20]
	algorithm = a_star


	test(circuit, 18, 13, netlist, algorithm)



	"""
	test(circuit, 18, 13, netlist, algorithm)

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
def test(circuit, width, height, netlist, algorithm):
	new_index = 0
	print("circuit of length", width, "and height", height)
	print("Upper bound (worst case) =", upper_bound(Chip(circuit, width, height), circuit, netlist))

	cost = 0
	while cost == 0:
		chip = Chip(circuit, width, height)
		chip.load_chip()
		for index, net in enumerate(netlist):
			try:
				cost += algorithm(chip, net)
			except TypeError:
				cost = 0
				print(index)
				netlist.insert(new_index % len(netlist), netlist.pop(index))
				new_index += 1
				break
	print("Total cost", algorithm.__name__, " = ", cost)

	print("Lower bound =", lower_bound(circuit, netlist))
	print()

	# print grid
	visualization.plot_grid(directory + "/results", chip, width, height)
	# visualization.print_simple_grid(chip)


if __name__ == "__main__":
	main()
