# TODO implement a better visualization

# print the circuit as a simple grid consisting of seperated layers
def print_simple_grid(chip):
    for z in range(chip.levels):
        print("Layer", z)
        for y in range(chip.height):
            for x in range(chip.width):
                print("|",end="")
                id = str(x) + ", " + str(y) + ", " + str(z)
                if chip.nodes.get(id) is None:
                    print(" ",end="")
                elif chip.nodes.get(id).is_free:
                    print(" ",end="")
                elif chip.nodes.get(id).is_gate:
                    print("o",end="")
                else:
                    print("-",end="")
            print("|")
