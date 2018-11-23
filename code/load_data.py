import imp

# loads the netlists and returns a list of tuples
def load_data(data):
	with open(data, 'r') as f:
		return imp.load_source('data', data, f)
