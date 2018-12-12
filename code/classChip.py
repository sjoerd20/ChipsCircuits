"""
By: Ivo de Brouwer & Sjoerd Terpstra

This file contains the datastructure of the project. The class Chip contains
all nodes present in the Chip.

In the Node class all information (id, coordinates, is_fee, is_gate,
list of neighbours) of a single node is stored.

The class Path holds all visited nodes of a single path of a net

"""

class Node():
	def __init__(self, id, coordinates, is_free):
		self.id = id                        # id string xyz
		self.coordinates = coordinates      # tuple with x, y, z coordinates
		self.is_free = is_free              # if node is used
		self.is_gate = False				# true if node is gate, else false
		self.L_neighbours = {}				# contains all neighbours (id, node)


class Path():
	def __init__(self, net, nodes):
		self.net = net						# the net from the path
		self.nodes = nodes 					# holds the nodes of the path

class Chip():
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

	# init nodes at level z and store them in nodes
	def init_nodes(self, z):
		self.levels += 1
		for x in range(self.width):
			for y in range(self.height):
				id = str(x) + ", " + str(y) + ", " + str(z)
				node = Node(id, (x, y, z), True)
				self.nodes[id] = node

	# stores all neighbours of each node
	def find_neighbours(self, id, node):
		x, y, z = node.coordinates
		possible_neighbours = [(x+1, y, z), (x, y-1, z), (x-1, y, z),
								(x, y+1, z), (x, y, z-1), (x, y, z+1)]
		for neighbour in possible_neighbours:

			# check for each neighbour if they exist
			id = str(neighbour[0]) + ", " + str(neighbour[1]) + ", " + str(neighbour[2])
			if id in self.nodes:
				node.L_neighbours[id] = self.nodes[id]

	# loads the chip
	def load_chip(self):
		cur_coordinates = []    # temp list for current gate
		for gate in self.circuit:
			for coordinate in gate:
				cur_coordinates.append(coordinate)
			id = str(cur_coordinates[0]) + ", " + str(cur_coordinates[1]) + ", " + "0"
			self.nodes.get(id).is_free = False
			self.nodes.get(id).is_gate = True
			self.walls.append((cur_coordinates[0], cur_coordinates[1], 0))
			self.gates.append(self.nodes.get(id))
			cur_coordinates = []

	# returns a list of coordinates of all gates
	def get_gates_coordinates(self):
		L_x, L_y = [], []
		for gate in self.gates:
			L_x.append(gate.coordinates[0])
			L_y.append(gate.coordinates[1])
		return L_x, L_y

	# TODO TEMPORARY METHOD. NODES IN WALLS SHOULD BE PUT IN A PATH OBJECT,
	# SO THAT EACH PATH CAN BE CLEARLY DISTINGUISHED IN THE VISUALIZATION PLOTS.
	# ALSO ADD LAYERS
	def get_walls_coordinates(self):
		x, y, z = [], [], []
		for node_id in self.walls:
			id = str(node_id[0]) + ", " + str(node_id[1]) + ", " + str(node_id[2])
			node = self.nodes.get(id)
			if node.is_gate == False:
				x.append(node.coordinates[0])
				y.append(node.coordinates[1])
				z.append(node.coordinates[2])
		return x, y, z

	# returns a list with lists filled with tuples of coordinates of all paths
	def get_all_paths_coordinates(self):
		all_paths_coordinates = []
		for path in self.paths:
			path_coordinates = self.get_path_coordinates(path)
			all_paths_coordinates.append(path_coordinates)
		return all_paths_coordinates

	# returns a list of tuples coordinates of a single path
	def get_path_coordinates(self, path):
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
