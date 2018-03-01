filename = "learning_python.txt"

with open(filename) as file_object:
	lines = file_object.readlines()
	list1 = ''

	for line in lines:
		list1 += line.strip()

print(list1.replace('python'.title(), 'c'.title()))
