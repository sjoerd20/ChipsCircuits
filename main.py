# add directories to path
import sys, os
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))

from classChip import Chip
from load_data import load_data
from algorithm import distance, area, lower_bound, algorithm

def main():

    """
    load net lists
    """
    circuits = load_data(directory + "/data/circuits.txt")
    netlists = load_data(directory + "/data/netlists.txt")

    test(circuits.circuit_0, 18, 13, netlists.netlist_1, algorithm)
    

    return


# to test with certain circuits and netlists
def test(circuit, horz_length, vert_length, netlist, algorithm):
    
    go_up = True
    
    cost = 0
    chip = Chip(circuit, horz_length, vert_length)
    for net in netlist:
      cost += algorithm(chip, circuit, net, go_up)
      go_up = not go_up
    print("Unsorted =", cost)

    cost = 0
    chip = Chip(circuit, horz_length, vert_length)
    netlist.sort(key=lambda net: distance(circuit[net[0]], circuit[net[1]]))
    for net in netlist:
      cost += algorithm(chip, circuit, net, go_up)
      go_up = not go_up
    print("Distance sorted =", cost)

    cost = 0
    chip = Chip(circuit, 18, 13)
    netlist.sort(key=lambda net: area(circuit[net[0]], circuit[net[1]]))
    for net in netlist:
      cost += algorithm(chip, circuit, net, go_up)
      go_up = not go_up
    print("Area sorted =", cost)

    cost = 0
    chip = Chip(circuit, 18, 13)
    netlist.sort(key=lambda net: [distance(circuit[net[0]], circuit[net[1]]), 
    area(circuit[net[0]], circuit[net[1]])])
    for net in netlist:
      cost += algorithm(chip, circuit, net, go_up)
      go_up = not go_up
    print("Distance sorted, then area sorted =", cost)

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