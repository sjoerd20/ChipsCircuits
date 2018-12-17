import imp

def load_data(data):
	"""Loads the netlists and returns a list of tuples"""
	with open(data, 'r') as f:
		return imp.load_source('data', data, f)
