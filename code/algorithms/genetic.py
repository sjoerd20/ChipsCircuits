# Work in progress!

from random import randint
from shared_functions import *
from classChip import *

def genetic(chip, netlist):

	complete_path = []
	total_cost = 0

	for net in netlist:
		net_cost = 0
		try:
			current = chip.circuit[net[0]] + (0,)
			goal = chip.circuit[net[1]] + (0,)
			path = []
			while current != goal and net_cost < 100:
				rng = randint(0, 5)
				if len([x for x in chip.neighbors(current, goal)]) == 0:
					raise KeyError
				for next in chip.neighbors(current, goal):
					if rng == 0:
						current = next
						chip.walls.append(current)
						path.append(current)
						net_cost += 1
						break
					else:
						rng -= 1
		except KeyError:
			net_cost = 100
		complete_path.append(path)
		total_cost += net_cost

	return (complete_path, total_cost)

def initial_pop(circuit, width, height, size, netlist):
	population = []
	for net in range(size):
		chip = Chip(circuit, width, height)
		population.append(genetic(chip, netlist))
	population.sort(key = lambda path : path[1])
	return population
