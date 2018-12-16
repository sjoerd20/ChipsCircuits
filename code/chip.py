from node import Node
from path import Path


class Chip():
	""" This class contains the chip and the nodes within
	"""
	def __init__(self, circuit, width, height):
		self.levels = 0					# amount of layers of chip
		self.max_levels = 8				# maximum amount of layers
		self.width = width				# width of chip
		self.height = height			# height of chip
		self.circuit = circuit			# list of all gates
		self.nodes = {}                	# contains all nodes with coord. as keys
		self.walls = []                 # contains all used nodes
		self.paths = []					# list of all Path objects
		self.gates = []					# list of all gate id's

		# initiate all levels of the chip
		for z in range(self.max_levels):
			self.init_nodes(z)

		# store all neighbours of each nodes
		for id, node in self.nodes.items():
			self.find_neighbours(id, node)

	def empty(self):
		"""This empties all walls and paths"""
		self.walls = [gate.coordinates for gate in self.gates]
		self.paths = []

	def init_nodes(self, z):
		"""Initiate nodes at level z"""
		self.levels += 1
		for x in range(self.width):
			for y in range(self.height):
				id = str(x) + ", " + str(y) + ", " + str(z)
				node = Node(id, (x, y, z), True)
				self.nodes[id] = node

	def find_neighbours(self, id, node):
		"""Stores all neighbours of each node"""
		x, y, z = node.coordinates
		possible_neighbours = [(x+1, y, z), (x, y-1, z), (x-1, y, z),
								(x, y+1, z), (x, y, z-1), (x, y, z+1)]
		for neighbour in possible_neighbours:

			# check for each neighbour if they exist
			id = str(neighbour[0]) + ", " + str(neighbour[1]) + ", " + str(neighbour[2])
			if id in self.nodes:
				node.L_neighbours[id] = self.nodes[id]

	def load_chip(self):
		"""Load all gates in this class instance"""
		cur_coordinates = []    # temp list for current gate
		for gate in self.circuit:
			for coordinate in gate:
				cur_coordinates.append(coordinate)
			id = str(cur_coordinates[0]) + ", " + str(cur_coordinates[1]) \
				+ ", " + "0"
			self.nodes.get(id).is_free = False
			self.nodes.get(id).is_gate = True
			self.walls.append((cur_coordinates[0], cur_coordinates[1], 0))
			self.gates.append(self.nodes.get(id))
			cur_coordinates = []

	# returns a list of coordinates of all gates
	def get_gates_coordinates(self):
		"""Returns 2 lists with x- and y-coordinates of all gates"""
		L_x, L_y = [], []
		for gate in self.gates:
			L_x.append(gate.coordinates[0])
			L_y.append(gate.coordinates[1])
		return L_x, L_y

	def get_walls_coordinates(self):
		"""Returns 3 lists with x-, y-, z-coordinates of all occupied nodes"""
		x, y, z = [], [], []
		for node_id in self.walls:
			id = str(node_id[0]) + ", " + str(node_id[1]) + ", " + str(node_id[2])
			node = self.nodes.get(id)
			if node.is_gate == False:
				x.append(node.coordinates[0])
				y.append(node.coordinates[1])
				z.append(node.coordinates[2])
		return x, y, z

	def get_all_paths_coordinates(self):
		"""Returns a list with lists filled with tuples of coordinates of all
		paths.
		"""
		all_paths_coordinates = []
		for path in self.paths:
			path_coordinates = self.get_path_coordinates(path)
			all_paths_coordinates.append(path_coordinates)
		return all_paths_coordinates

	def get_path_coordinates(self, path):
		"""Returns a list of tuples coordinates of a single path. """

		path_coordinates = []
		for node_id in path.nodes:
			id = str(node_id[0]) + ", " + str(node_id[1]) + ", " + str(node_id[2])
			node = self.nodes.get(id)
			path_coordinates.append(node.coordinates)
		return path_coordinates

	def in_bounds(self, id):
		(x, y, z) = id
		return 0 <= x < self.width and 0 <= y < self.height and 0 <= z < self.levels

	def passable(self, id):
		return id not in self.walls

	def neighbors(self, id, goal = None):
		(x, y, z) = id
		results = [(x+1, y, z), (x, y-1, z), (x-1, y, z), (x, y+1, z), (x, y, z-1), (x, y, z+1)]
		if goal not in results:
			results = filter(self.in_bounds, results)
			results = filter(self.passable, results)
		return results

	def possible_neighbors(self, id):
		(x, y, z) = id
		results = [(x+1, y, z), (x, y-1, z), (x-1, y, z), (x, y+1, z), (x, y, z-1), (x, y, z+1)]
		return results
