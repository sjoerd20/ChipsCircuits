import heapq
from random import random

import shared_functions as sfunc
from chip import Chip
from path import Path


def a_star(chip, net):
	"""A* is a best-first search; it tries to find the shortest path between
	two points
	"""
	start, goal = chip.circuit[net[0]] + (0,), chip.circuit[net[1]] + (0,)
	came_from, cost_so_far = {}, {}
	came_from[start], cost_so_far[start] = None, 0

	queue = []
	heapq.heappush(queue, (0, start))
	while len(queue) > 0:
		current = heapq.heappop(queue)[1]
		if current == goal:
			break
		for next in chip.neighbors(current, goal):
			new_cost = cost_so_far[current] + 1
			if next not in cost_so_far or new_cost < cost_so_far[next]:
				cost_so_far[next] = new_cost
				priority = new_cost + sfunc.heuristic(goal, next) \
						+ sfunc.gate_density(chip, next, start, goal)
				heapq.heappush(queue, (priority, next))
				came_from[next] = current

	prev = goal
	shortest_path = [prev]
	while came_from[prev] is not None:
		shortest_path.append(came_from[prev])
		prev = came_from[prev]
	chip.walls += shortest_path
	chip.paths.append(Path(net, shortest_path))

	return cost_so_far[goal]
