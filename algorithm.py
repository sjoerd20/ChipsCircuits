def distance(coords_a, coords_b):
	return abs(coords_a[0] - coords_b[0]) + abs(coords_a[1] - coords_b[1])

def heuristic(coords_a, coords_b):
	return abs(coords_a[0] - coords_b[0]) + abs(coords_a[1] - coords_b[1]) + abs(coords_a[2] - coords_b[2])

# delta x * delta y, POSSIBLY an improvement; does the simplest/most straight paths first
def area(coords_a, coords_b):
	return abs(coords_a[0] - coords_b[0]) * abs(coords_a[1] - coords_b[1])

# largest lower bound
def lower_bound(circuit, netlist):
	lower_bound = 0
	for net in netlist:
		lower_bound += distance(circuit[net[0]], circuit[net[1]])
  	# can still be improved
	return lower_bound

# smallest upper bound
def upper_bound(circuit, netlist):
  	# TODO
	return upper_bound

import heapq

class PriorityQueue():
	def __init__(self):
		self.elements = []

	def empty(self):
		return len(self.elements) == 0

	def put(self, item, priority):
		heapq.heappush(self.elements, (priority, item))

	def get(self):
		return heapq.heappop(self.elements)[1]

def a_star(chip, net):
	start = chip.circuit[net[0]] + (0,)
	goal = chip.circuit[net[1]] + (0,)
	queue = PriorityQueue()
	queue.put(start, 0)
	came_from = {}
	cost_so_far = {}
	came_from[start] = None
	cost_so_far[start] = 0
	shortest_path = []

	while not queue.empty():
		current = queue.get()
		if current == goal:
			break
		for next in chip.neighbors(current, start, goal):
			if current not in shortest_path:
				shortest_path.append(current)
			new_cost = cost_so_far[current] + 1
			if next not in cost_so_far or new_cost < cost_so_far[next]:
				cost_so_far[next] = new_cost
				priority = new_cost + heuristic(goal, next)
				queue.put(next, priority)
				came_from[next] = current
				shortest_path.remove(current)
	chip.walls += shortest_path		
	return cost_so_far[goal]

def greedy(chip, net):
	net_cost = 0
	x = chip.circuit[net[0]][0]
	y = chip.circuit[net[0]][1]
	z = 0
	end_x = chip.circuit[net[1]][0]
	end_y = chip.circuit[net[1]][1]

	while (x != end_x or y != end_y or z != 0):

		if x < end_x:
			id = str(x + 1) + ", " + str(y) + ", " + str(z)
			if chip.nodes.get(id).is_free:
				x += 1
				chip.nodes.get(id).is_free = False
			else:
				z += 1
				id = str(x) + ", " + str(y) + ", " + str(z)
				if chip.nodes.get(id) is None:
					chip.init_nodes(z)
				chip.nodes.get(id).is_free = False

		elif x > end_x:
			id = str(x - 1) + ", " + str(y) + ", " + str(z)
			if chip.nodes.get(id).is_free:
				x -= 1
				chip.nodes.get(id).is_free = False
			else:
				z += 1
				id = str(x) + ", " + str(y) + ", " + str(z)
				if chip.nodes.get(id) is None:
					chip.init_nodes(z)
				chip.nodes.get(id).is_free = False

		elif y < end_y:
			id = str(x) + ", " + str(y + 1) + ", " + str(z)
			if chip.nodes.get(id).is_free:
				y += 1
				chip.nodes.get(id).is_free = False
			else:
				z += 1
				id = str(x) + ", " + str(y) + ", " + str(z)
				if chip.nodes.get(id) is None:
					chip.init_nodes(z)
				chip.nodes.get(id).is_free = False

		elif y > end_y:
			id = str(x) + ", " + str(y - 1) + ", " + str(z)
			if chip.nodes.get(id).is_free:
				y -= 1
				chip.nodes.get(id).is_free = False
			else:
				z += 1
				id = str(x) + ", " + str(y) + ", " + str(z)
				if chip.nodes.get(id) is None:
					chip.init_nodes(z)
				chip.nodes.get(id).is_free = False
		else:
			z -= 1
			id = str(x) + ", " + str(y) + ", " + str(z)
			chip.nodes.get(id).is_free = False

		net_cost += 1

	return net_cost