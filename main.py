# add directories to path
import sys, os
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))

from classChip import Chip
from load_data import load_data
from algorithm import distance, adjusted_distance, lower_bound, algorithm

def main():

    """
    load net lists
    """
    circuits = load_data(directory + "/data/circuits.txt")
    netlists = load_data(directory + "/data/netlists.txt")

    test(circuits.circuit_0, netlists.netlist_1)

    """
    instantiate circuit 0 and 1
    """

    chip0 = Chip(directory + "/data/circuit0.txt", 18, 13)
    # chip1 = Chip(directory + "/data/circuit1.txt")

    chip0.load_chip()
    

    return

# to test with certain circuits and netlists
def test(circuit, netlist):
    print("Lower bound =", lower_bound(circuit, netlist))

    netlist.sort(key=lambda net: distance(circuit[net[0]], circuit[net[1]]))
    print("Distance sorted =", algorithm(circuit, netlist))

    netlist.sort(key=lambda net: [distance(circuit[net[0]], circuit[net[1]]), 
    adjusted_distance(circuit[net[0]], circuit[net[1]])])
    print("Adjusted distance sorted =", algorithm(circuit, netlist))


if __name__ == "__main__":
    main()