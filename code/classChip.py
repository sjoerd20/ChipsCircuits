# class chips & circuits

class Node():
    def __init__(self, id, coordinates, is_free):
        self.id = id                        # id xyz
        self.coordinates = coordinates      # tuple with x, y, z coordinates
        self.is_free = is_free              # free means not used and no gate

class Chip():
    def __init__(self, file_circuit, horiz_length, vert_length):
        self.count_levels = 1
        self.horiz_length = horiz_length
        self.vert_length = vert_length
        self.file_circuit = file_circuit
        self.dict_nodes = {}        # contains all nodes with coord. as keys
        L_gates = []                # contains all gates coord.

        # initiate first level of chip
        self.init_nodes(0)


    # init nodes at level z and store them in dict_nodes
    def init_nodes(self, z):
        for x in range(self.horiz_length):
            for y in range(self.vert_length):

                # TODO make a dict instead of list with tuple? coordinates as keys
                id = str(x) + ", "+ str(y) + ", " + str(z)
                node = Node(id, (x, y, z), True)
                self.dict_nodes[id] = node


    # loads the chip
    def load_chip(self):
        with open(self.file_circuit, 'r') as f_circuit:

            cur_coordinates = []    # temp list for current gate
            new_gate = False        # checks if new gate is reached
            for line in f_circuit:
                for char in line:
                    if char == "(":
                        new_gate = True
                    elif char == ")":
                        new_gate == False
                        id = str(cur_coordinates[0]) + str(cur_coordinates[1])
                                 + "0")
                        self.dict_nodes.get(id).is_free = False
                        L_gates.append(id)
                        cur_coordinates = []

                    elif new_gate == True and is_number(char):
                        cur_coordinates.append(int(char))
