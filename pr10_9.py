filename1 = "cats.txt"
filename2 = "dogs.txt"

try:
	with open(filename1) as f_obj1:
		content1 = f_obj1.read()
except FileNotFoundError:
	pass
else:
	print(content1.strip())

try:
	with open(filename2) as f_obj2:
		content2 = f_obj2.read()
except FileNotFoundError:
	pass
else:
	print(content2.strip())