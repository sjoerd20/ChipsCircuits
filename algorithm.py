def distance(coords_a, coords_b):
  return abs(coords_a[0] - coords_b[0]) + abs(coords_a[1] - coords_b[1])

# delta x * delta y, POSSIBLY an improvement; does the simplest/most straight paths first
def area(coords_a, coords_b):
  return abs(coords_a[0] - coords_b[0]) * abs(coords_a[1] - coords_b[1])

# largest lower bound
def lower_bound(circuit, netlist):
  lower_bound = 0
  for net in netlist:
    lower_bound += distance(circuit[net[0]], circuit[net[1]])
  # can still be improved
  return lower_bound

# smallest upper bound
def upper_bound(circuit, netlist):
  # TODO
  return upper_bound

def algorithm(chip, circuit, net, go_up = True):
  net_cost = 0
  z = 0
  current_x = circuit[net[0]][0]
  current_y = circuit[net[0]][1]
  end_x = circuit[net[1]][0]
  end_y = circuit[net[1]][1]
  
  while (current_x != end_x or current_y != end_y or z != 0):

    if current_x < end_x:
      id = str(current_x + 1) + ", " + str(current_y) + ", " + str(z)
      if chip.dict_nodes.get(id).is_free:
        current_x += 1
        chip.dict_nodes.get(id).is_free = False
      else:
        if go_up:
          z += 1
        else:
          z -= 1
        id = str(current_x) + ", " + str(current_y) + ", " + str(z)
        if chip.dict_nodes.get(id) is None:
          chip.init_nodes(z)
        chip.dict_nodes.get(id).is_free = False

    elif current_x > end_x:
      id = str(current_x - 1) + ", " + str(current_y) + ", " + str(z)
      if chip.dict_nodes.get(id).is_free:
        current_x -= 1
        chip.dict_nodes.get(id).is_free = False
      else:
        if go_up:
          z += 1
        else:
          z -= 1
        id = str(current_x) + ", " + str(current_y) + ", " + str(z)
        if chip.dict_nodes.get(id) is None:
          chip.init_nodes(z)
        chip.dict_nodes.get(id).is_free = False

    elif current_y < end_y:
      id = str(current_x) + ", " + str(current_y + 1) + ", " + str(z)
      if chip.dict_nodes.get(id).is_free:
        current_y += 1
        chip.dict_nodes.get(id).is_free = False
      else:
        if go_up:
          z += 1
        else:
          z -= 1
        id = str(current_x) + ", " + str(current_y) + ", " + str(z)
        if chip.dict_nodes.get(id) is None:
          chip.init_nodes(z)
        chip.dict_nodes.get(id).is_free = False

    elif current_y > end_y:
      id = str(current_x) + ", " + str(current_y - 1) + ", " + str(z)
      if chip.dict_nodes.get(id).is_free:
        current_y -= 1
        chip.dict_nodes.get(id).is_free = False
      else:
        if go_up:
          z += 1
        else:
          z -= 1
        id = str(current_x) + ", " + str(current_y) + ", " + str(z)
        if chip.dict_nodes.get(id) is None:
          chip.init_nodes(z)
        chip.dict_nodes.get(id).is_free = False

    elif z > 0:
      z -= 1
      id = str(current_x) + ", " + str(current_y) + ", " + str(z)
      chip.dict_nodes.get(id).is_free = False
      
    elif z < 0:
      z += 1
      id = str(current_x) + ", " + str(current_y) + ", " + str(z)
      chip.dict_nodes.get(id).is_free = False

    net_cost += 1

  return net_cost