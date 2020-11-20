def get_file_contents(filepath):
	result = []
	with open(filepath, "r") as f:
		for line in f.readlines():
			result.append(line.strip())
	return result
