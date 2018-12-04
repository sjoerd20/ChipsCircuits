# Work in progress!

from random import *
from shared_functions import *
from classChip import *

def fitness(chip, netlist, algorithm):
	cost = 0
	for index, net in enumerate(netlist):
		try:
			cost += algorithm(chip, net)
		except KeyError:
			return(index)
	return(cost)

def initial_pop(size, circuit, width, height, algorithm, netlist):
	population = []
	for i in range(size):
		chip = Chip(circuit, width, height)
		chip.load_chip()
		shuffle(netlist)
		population.append((netlist[:], fitness(chip, netlist[:], algorithm)))
	population.sort(key = lambda netlist : netlist[1], reverse = True)
	return population

def selection(population, sample):
	parents = []
	for i in range(sample):
		parents.append(population[i][0])
	shuffle(parents)
	return parents

def create_child(parent_a, parent_b):
	child = []
	for i in range(len(parent_a)):
		if random() < 0.5:
			if parent_a[i] not in child:
				child.append(parent_a[i])
			else:
				child.append(parent_b[i])
		else:
			if parent_b[i] not in child:
				child.append(parent_b[i])
			else:
				child.append(parent_a[i])
	return child

def next_pop(size, circuit, width, height, algorithm, parents):
	population = []
	for i in range(len(parents) // 2):
		for j in range(size):
			chip = Chip(circuit, width, height)
			chip.load_chip()
			child = create_child(parents[i], parents[len(parents) - 1 - i])
			population.append((child, fitness(chip, child, algorithm)))
	population.sort(key = lambda child : child[1], reverse = True)
	return population

def mutate(individual):
	ids = range(len(individual))
	a, b = sample(ids, 2)
	individual[a], individual[b] = individual[b], individual[a]

def mutate_pop(population, mutation_rate):
	for individual in population:
		if random() < mutation_rate:
			mutate(individual[0])
