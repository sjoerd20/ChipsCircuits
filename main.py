# add directories to path
import sys, os
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code" , "algorithms"))

from classChip import *
from load_data import load_data
from a_star import *
from greedy import *

def main():

	"""
	load net lists
	"""
	circuits = load_data(directory + "/data/circuits.txt")
	netlists = load_data(directory + "/data/netlists.txt")

	circuit = circuits.circuit_0
	netlist = netlists.netlist_1
	algorithm = a_star

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
	print("circuit van lengte", width, "en hoogte", height)
	print()

	cost = 0
	chip = Chip(circuit, width, height)
	chip.load_chip()
	for net in netlist:
		print(chip.circuit[net[0]], chip.circuit[net[1]])
		cost += algorithm(chip, net)
	print("Total cost, " + sort + " =", cost)

	print("Lower bound =", lower_bound(circuit, netlist))
	print()

"""
	for z in range(chip.levels):
		print("Layer", z)
		for y in range(height):
			for x in range(width):
				print("|",end="")
				id = str(x) + ", " + str(y) + ", " + str(z)
				if chip.nodes.get(id) is None:
					print(" ",end="")
				elif chip.nodes.get(id).is_free:
					print(" ",end="")
				elif chip.nodes.get(id).is_gate:
					print("o",end="")
				else:
					print("-",end="")
			print("|")
"""


if __name__ == "__main__":
	main()
