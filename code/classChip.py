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
        self.forbidden = []          # contains coordinates used nodes and gates

        self.init_nodes(0)


    # init nodes
    def init_nodes(self, z):
        L_nodes = []
        for x in range(self.horiz_length):
            for y in range(self.vert_length):
                # TODO make a dict instead of list with tuple? coordinates as keys
                L_nodes.append(Node(id, (x, y, z), True))


    # loads the chip
    def load_chip(self):
        with open(self.file_circuit, 'r') as f_circuit:

            # write code to load the chip from file_chip
            cur_coordinates = []        # temp list for current gate
            new_gate = False     # checks if new gate is reached
            for line in f_circuit:
                for char in line:
                    if char == "(":
                        new_gate = True
                    elif char == ")":
                        new_gate == False
                        # TODO change this node's is_free to False
                        # and add to list with all gates incl. gate number
                    elif new_gate == True and is_number(char):
                        cur_coordinates.append(int(char))
