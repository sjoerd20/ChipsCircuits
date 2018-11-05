# load data

class Load_data():
    def __init__(self, file_net_lists, file_chip):
        self.file_net_lists = file_net_lists
        self.file_chip = file_chip

    # loads the netlists
    def load_netlists(self):
        dir_netlists = '../data/' + self.file_net_lists
        with open(v, 'r') as f_netlists:

            # write code to load the net lists from f_netlists
            return True
        return False

    # loads chips
    def load_chip(self):
        dir_chip = '../data/' + self.file_chip
        with open(dir_chip, 'r') as f_chip:

            # write code to load the chip from f_chip
            return True
        return False
