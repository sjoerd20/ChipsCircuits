def distance(coords_a, coords_b):
  return abs(coords_a[0] - coords_b[0]) + abs(coords_a[1] - coords_b[1])

# delta x * delta y, POSSIBLY an improvement; does the simplest/most straight paths first
def adjusted_distance(coords_a, coords_b):
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

def algorithm(circuit, netlist):
  total_cost = 0
  for net in netlist:
    total_cost += distance(circuit[net[0]], circuit[net[1]])
  # TODO
  return total_cost