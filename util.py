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

def list_append(a_list, something_to_add):
    new_list = list(a_list)
    new_list.append(something_to_add)
    return new_list

def read_file(filename):
    with open(filename, 'r') as myfile:
        return myfile.read()
