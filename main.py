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

    test(circuits.circuit_0, netlists.netlist_1, algorithm)
    

    return


# to test with certain circuits and netlists
def test(circuit, netlist, algorithm):
    
    go_up = True
    cost = d_sorted_cost = adj_sorted_cost = 0

    chip = Chip(circuit, 18, 13)
    for net in netlist:
      cost += algorithm(chip, circuit, net, go_up)
      go_up = not go_up
    print("Unsorted =", cost)

    chip = Chip(circuit, 18, 13)
    netlist.sort(key=lambda net: distance(circuit[net[0]], circuit[net[1]]))
    for net in netlist:
      d_sorted_cost += algorithm(chip, circuit, net, go_up)
      go_up = not go_up
    print("Distance sorted =", d_sorted_cost)

    chip = Chip(circuit, 18, 13)
    netlist.sort(key=lambda net: [distance(circuit[net[0]], circuit[net[1]]), 
    adjusted_distance(circuit[net[0]], circuit[net[1]])])
    for net in netlist:
      adj_sorted_cost += algorithm(chip, circuit, net, go_up)
      go_up = not go_up
    print("Adjusted distance sorted =", adj_sorted_cost)

    print("Lower bound =", lower_bound(circuit, netlist))

    chip.load_chip()
    for z in range(-4,5):
      print("Layer", z)
      for y in range(13):
        for x in range(18):
          print("|",end="")
          id = str(x) + ", " + str(y) + ", " + str(z)
          if chip.dict_nodes.get(id) is None:
            print(" ",end="")
          elif chip.dict_nodes.get(id).is_free:
            print(" ",end="")
          elif chip.dict_nodes.get(id).is_gate:
            print("o",end="")
          else:
            print("-",end="")
        print("|")


if __name__ == "__main__":
    main()