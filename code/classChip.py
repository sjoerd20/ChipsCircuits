# class chips & circuits
class Node():
    def __init__(self, id, coordinates, is_free):
        self.id = id                        # id xyz
        self.coordinates = coordinates      # tuple with x, y, z coordinates
        self.is_free = is_free              # free means not used
        self.is_gate = False


class Chip():
    def __init__(self, circuit, horiz_length, vert_length):
        self.lower_levels = 0
        self.higher_levels = 0
        self.horiz_length = horiz_length
        self.vert_length = vert_length
        self.circuit = circuit
        self.dict_nodes = {}                # contains all nodes with coord. as keys
        self.L_gates = []                   # contains all gates coord.

        # initiate first level of chip
        self.init_nodes(0)


    # init nodes at level z and store them in dict_nodes
    def init_nodes(self, z):
        if z < 0:
            self.lower_levels -= 1
        elif z > 0:
            self.higher_levels += 1
        for x in range(self.horiz_length):
            for y in range(self.vert_length):
                # TODO make a dict instead of list with tuple? coordinates as keys
                id = str(x) + ", " + str(y) + ", " + str(z)
                node = Node(id, (x, y, z), True)
                self.dict_nodes[id] = node


    # loads the chip
    def load_chip(self):
        cur_coordinates = []    # temp list for current gate
        for gate in self.circuit:
            for coordinate in gate:
              cur_coordinates.append(coordinate)
            id = str(cur_coordinates[0]) + ", " + str(cur_coordinates[1]) + ", " + "0"
            self.dict_nodes.get(id).is_free = False
            self.dict_nodes.get(id).is_gate = True
            self.L_gates.append(id)
            cur_coordinates = []
