""" Chips & circuits
Authors: Ivo de Brouwer, Sjoerd Terpstra
Course: Programmeertheorie, UvA

For a full description of this project, see:
https://github.com/sjoerd20/ChipsCircuits/blob/master/README.md

"""

import sys
import os
import argparse

# add directory to path for import of project modules
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "results"))
sys.path.append(os.path.join(directory, "code" , "algorithms"))

import visualization
import genetic
import shared_functions as sfunc
from load_data import load_data
from a_star import a_star
from greedy import greedy
from chip import Chip
from node import Node
from path import Path

POPULATION_SIZE = 20

def main():

	circuits = load_data(directory + "/data/circuits.txt")
	netlists = load_data(directory + "/data/netlists.txt")

	# parse and process command line arguments
	algorithmslist, circuitslist, netlistslist, \
		do_visualization, chip_dimensionsdict \
		= command_parser(circuits, netlists)

	# Calculate state space size and upper/lower bounds for  all
	# given chips, circuits and netlists
	for circuit in circuitslist:
		for netlist in netlistslist:
			if (circuit[1] == "both" or circuit[1] == "small" \
			 		and (netlist[1] == 1 or netlist[1] == 2 \
					or netlist[1] == 3)) or (circuit[1] == "large" \
					and (netlist[1] == 4 or netlist[1] == 5 \
					or netlist[1] == 6)):
				print("Calculating state space for circuit " + circuit[1] +
					  " and netlist " + str(netlist[1]))
				width, height = chip_dimensionsdict[circuit[1]]
				sfunc.state_space(circuit[0], width, height, netlist[0])

	for algorithm in algorithmslist:
		for circuit in circuitslist:
			for netlist in netlistslist:
				if (circuit[1] == "small" and (netlist[1] == 1 or netlist[1] == 2 or netlist[1] == 3)) or (circuit[1] == "large" and (netlist[1] == 4 or netlist[1] == 5 or netlist[1] == 6)):
					width, height = chip_dimensionsdict[circuit[1]]
					chip = Chip(circuit[0], width, height)
					chip.load_chip()
					if algorithm == a_star:
						netlist, cost = genetic.make_netlist(POPULATION_SIZE, chip, algorithm, netlist[0])
						total_cost = sfunc.upper_bound(chip) - sfunc.fitness(chip, netlist, algorithm, width, height, do_visualization)
					else:
						total_cost = sfunc.upper_bound(chip) - sfunc.fitness(chip, netlist[0], algorithm, width, height, do_visualization)
					print("Total cost", algorithm.__name__, " = ", total_cost)
	return


def command_parser(circuits, netlists):
	""" Parse command line arguments and processes them for the main program.
	This function also checks if the given arguments are valid program input.

	Keyword arguments:
	circuits -- all loaded circuits
	netlists -- all loaded netlists

	Returns:
	algorithmslist -- list of selected algorithms
	circuitslist -- list of selected circuits
	netlistslist -- list of selected netlists
	do_visualization -- boolean make visualization
	"""

	# Add parser for command line arguments
	parser = argparse.ArgumentParser(description="Chips & Circuits. If run without positional arguments deafult program is runned.")

	# Add all possible algorithms/circuits/netlists to dicts
	algorithmsdict = {"greedy" : greedy, "a_star" : a_star,
					  "both" : (greedy, a_star)}
	circuitsdict = {"small" : circuits.circuit_0, "large": circuits.circuit_1,
					"both" : (circuits.circuit_0, circuits.circuit_1)}
	netlistsdict = {"1" : netlists.netlist_1, "2" : netlists.netlist_2,
					"3": netlists.netlist_3, "4" : netlists.netlist_4,
					"5": netlists.netlist_5, "6" : netlists.netlist_6,
					"small" : (netlists.netlist_1, netlists.netlist_2,
							 netlists.netlist_3),
					"large" : (netlists.netlist_4, netlists.netlist_5,
							 netlists.netlist_6),
					"all" : (netlists.netlist_1, netlists.netlist_2,
							 netlists.netlist_3, netlists.netlist_4,
							 netlists.netlist_5, netlists.netlist_6)}
	visualization_optionsdict = {"true" : True, "false" : False}

	# Dimensions in (width, height)
	chip_dimensionsdict = {"small" : (18, 13), "large" : (18, 17)}

	# Add parser arguments
	parser.add_argument("algorithm", choices=algorithmsdict.keys(), nargs="?", default="both", help="Choose algorithm: greedy/a_star/both. Default is both")
	parser.add_argument("circuit", choices=circuitsdict.keys(), nargs="?", default="both", help="Choose circuit: small/large/both. Default is both. Choose small netlist with small circuit and large netlist with large circuit")
	parser.add_argument("netlist", choices=netlistsdict.keys(), nargs="?", default="all", help="Choose netlist: 1/2/3/4/5/6/small/large/all. Default is all. Choose small netlist with small circuit and large netlist with large circuit")
	parser.add_argument("-v", "--visualization", choices=visualization_optionsdict.keys(), default="false", help="Show visualization: true/false. Default is false")
	args = parser.parse_args()
	argsdict = vars(args) 		# dict with all args stored by keys

	# Extract selected algorithms
	algorithmslist = []
	if (argsdict["algorithm"]) == "both":
		algorithmslist = [algorithmsdict[args.algorithm][i] for i in range(len(algorithmsdict[args.algorithm]))]
	else:
		algorithmslist.append(algorithmsdict[args.algorithm])

	# Extract selected circuits
	circuitslist = []
	L_chips = ["small", "large"]
	if (argsdict["circuit"] == "both"):
		for i in range(len(circuitsdict[args.circuit])):
			circuitslist.append((circuitsdict[args.circuit][i], L_chips[i]))
	elif (argsdict["circuit"] == "small"):
		circuitslist.append((circuitsdict[args.circuit], "small"))
	elif (argsdict["circuit"] == "large"):
		circuitslist.append((circuitsdict[args.circuit], "large"))

	# Extract selected netlists
	netlistslist = []
	L_netlists = [1, 2, 3, 4, 5, 6]
	if (argsdict["netlist"]) == "all":
		netlistslist = [(netlistsdict[args.netlist][i], L_netlists[i]) for i in range(len(netlistsdict[args.netlist]))]
	elif (argsdict["netlist"]) == "large":
		netlistslist = [(netlistsdict[args.netlist][i], L_netlists[i+3]) for i in range(len(netlistsdict[args.netlist]))]
		print(netlistslist)
	elif (argsdict["netlist"]) == "small":
		netlistslist = [(netlistsdict[args.netlist][i], L_netlists[i]) for i in range(len(netlistsdict[args.netlist]))]
	else:
		netlistslist.append((netlistsdict[args.netlist], int(args.netlist)))

	do_visualization = False
	if argsdict["visualization"] == "true":
		do_visualization = True

	# Check if program input is viable:
	# the right combination of netlists and circuits.
	is_compatible = False
	for circuit in circuitslist:
		for netlist in netlistslist:
			if (circuit[1] == "both" or circuit[1] == "small" \
			 		and (netlist[1] == 1 or netlist[1] == 2 \
					or netlist[1] == 3)) or (circuit[1] == "large" \
					and (netlist[1] == 4 or netlist[1] == 5 \
					or netlist[1] == 6)):
				is_compatible = True
	if is_compatible == False:
		print("No compatible circuits and netlists selected! \
			Run main.py -h for help")
		exit(1)

	return algorithmslist, circuitslist, netlistslist, \
		do_visualization, chip_dimensionsdict


if __name__ == "__main__":
	main()
