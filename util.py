def string_to_number(x):
	if '.' in x:
		return float(x)
	else:
		return int(x)

def is_number(string):
    try:
        float(string)
        return True
    except:
        return False

def read_file(filename):
    with open(filename, 'r') as myfile:
        return myfile.read()