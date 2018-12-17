import os

from random import choice, shuffle, random, sample
from shared_functions import *
from chip import Chip

parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def initial_pop(size, chip, algorithm, netlist):
	population = []
	for i in range(size):
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


def create_child(parent_a, parent_b, netlist):
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
	population = []
	for i in range(len(parents) // 2):
		for j in range(population_size):
			child = create_child(parents[i], parents[len(parents) - 1 - i], netlist)
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


def make_netlist(population_size, chip, algorithm, netlist, do_visualization = False):
	i = 0
	L_i = []
	L_costs = []
	L_number_placed = []
	population = initial_pop(population_size, chip, algorithm, netlist)
	while population[0][1] < len(netlist) and i < 50:
		mutate_pop(population, 0.1)
		parents = selection(population, 5)
		population = next_pop(population_size // 5 + 1, chip, algorithm, parents, netlist)
		print("Generation {}: placed nets: {}, score: {}".format(i, population[0][1], upper_bound(chip) - population[0][1]))
		L_i.append(i)
		L_costs.append(upper_bound(chip) - population[0][1])
		L_number_placed.append(population[0][1])
		i += 1
	if do_visualization and population[0][1] >= len(netlist):
		visualization.plot_3D(parent_dir + "/results", chip)
		visualization.plot_grid(parent_dir + "/results", chip)
	print(L_i, L_costs, L_number_placed)
	return population[0][0], population[0][1]
