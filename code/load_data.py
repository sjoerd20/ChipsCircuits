# loads the netlists and returns a list of tuples
def load_data(data):
	with open(data, 'r') as f:
		import imp
		return imp.load_source('data', '', f)