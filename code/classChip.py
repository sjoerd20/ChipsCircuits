# class chips & circuits

class Chip(self):
    def __init__(self, file_chip, length, width):
        self.count_levels = 1
        self.length = length
        self.width = width
        self.file_chip = file_chip

        self.load_chip(self)

    # loads all chips
    def load_chip(self):
        dir_chip = '../data/' + self.file_chip
        with open(dir_chip, 'r') as f_chip:

            # write code to load the chip from file_chip
            return True
        return False

class Node(self):
    def __init__(self, id, is_gate=False):
        self.id = id
        self.is_gate = is_gate
        self.used = False
        self.id_previous_node = None
