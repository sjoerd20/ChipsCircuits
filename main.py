# add directories to path
import sys, os
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))

from classChip import Chip
from load_data import load_netlists


def main():

    """
    load net lists
    """

    load_netlists(directory + "/data/netlists.txt")

    """
    instantiate circuit 0 and 1
    """

    chip0 = Chip(directory + "/data/circuit0.txt")
    chip1 = Chip(directory + "/data/circuit1.txt")

    return

if __name__ == "__main__":
    main()
