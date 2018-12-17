import os

from random import choice, shuffle, random, sample
from shared_functions import *
from chip import Chip

parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def initial_pop(size, chip, algorithm, netlist):
	"""Create an initial population of randomly ordered copies of a netlist"""
	population = []
	for i in range(size):
		shuffle(netlist)
		population.append((netlist[:], fitness(chip, netlist[:], algorithm)))
	population.sort(key = lambda netlist : netlist[1], reverse = True)
	return population


def selection(population, sample):
	"""Select the best sample from the population for breeding"""
	parents = []
	for i in range(sample):
		parents.append(population[i][0])
	shuffle(parents)
	return parents


def create_child(parent_a, parent_b, netlist):
	"""Create children who inherit a net if both parents share that net on the same index;
	the remainder is inherited in a random order from the remaining nets"""
	temp_netlist = [netlist[i] for i in range(len(netlist))]
	child = [0 for i in range(len(parent_a))]
	for i in range(len(parent_a)):
		if (parent_a[i] == parent_b[i]):
			child[i] = parent_a[i]
			temp_netlist.remove(parent_a[i])
	for i in range(len(child)):
		if (len(netlist) > 0):
			if child[i] == 0:
				child[i] = choice(temp_netlist)
				temp_netlist.remove(child[i])
	return child


def next_pop(population_size, chip, algorithm, parents, netlist):
	"""Create a new population"""
	population = []
	for i in range(len(parents) // 2):
		for j in range(population_size):
			child = create_child(parents[i], parents[len(parents) - 1 - i], netlist)
			population.append((child, fitness(chip, child, algorithm)))
	population.sort(key = lambda child : child[1], reverse = True)
	return population


def mutate(individual):
	"""Mutate an individual by swapping two nets"""
	ids = range(len(individual))
	a, b = sample(ids, 2)
	individual[a], individual[b] = individual[b], individual[a]


def mutate_pop(population, mutation_rate):
	"""Mutate individuals randomly from a population at a given rate"""
	for individual in population:
		if random() < mutation_rate:
			mutate(individual[0])


def make_netlist(population_size, chip, algorithm, netlist, do_visualization = False):
	"""Do the genetic algorithm until you obtain a netlist reordering that A* can obtain a valid solution from,
	or use the reordering which has placed the most nets using A* after 50 generations have passed"""
	i = 0
	population = initial_pop(population_size, chip, algorithm, netlist)
	while population[0][1] < len(netlist) and i < 50:
		mutate_pop(population, 0.1)
		parents = selection(population, 5)
		population = next_pop(population_size // 5 + 1, chip, algorithm, parents, netlist)
		print("Generation {}: placed nets: {}, score: {}".format(i, population[0][1], upper_bound(chip) - population[0][1]))
		i += 1
	if do_visualization and population[0][1] >= len(netlist):
		visualization.plot_3D(parent_dir + "/results", chip)
		visualization.plot_grid(parent_dir + "/results", chip)
	return population[0][0], population[0][1]
