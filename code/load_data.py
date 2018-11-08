# loads the netlists and returns a list of tuples
def load_data(file_net_lists):
    with open(file_net_lists, 'r') as f_netlists:
      import imp
      return imp.load_source('data', '', f_netlists)