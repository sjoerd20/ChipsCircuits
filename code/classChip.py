# class chips & circuits

class Chip():
    def __init__(self, file_circuit, length, width):
        self.count_levels = 1
        self.length = length
        self.width = width
        self.file_circuit = file_circuit
        self.forbidden = []          # contains coordinates used nodes and gates

        self.load_chip(self)

    # loads the chip
    def load_chip(self):
        with open(file_circuit, 'r') as f_circuit:

            # write code to load the chip from file_chip
            NotImplementedError()
        NotImplementedError()

class Node():
    def __init__(self, id, coordinates, is_free):
        self.id = id                        # id xyz
        self.coordinates = coordinates      # tuple with x, y, z coordinates
        self.is_free = is_free              # free means not used and no gate
