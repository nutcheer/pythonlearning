filename = "learning_python.txt"
# method 1
with open(filename) as file_object:
	contents = file_object.read()
	print(contents)
# method 2
with open(filename) as file_object2:
	for line in file_object2:
		print(line.strip())
# method 3
with open(filename) as file_object3:
	list1 = ''
	for line in file_object3:
		list1 += line.strip()

print(list1)
