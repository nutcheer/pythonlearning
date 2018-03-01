filename = "alice.txt"
try:
	with open(filename) as f_obj:
		contents = f_obj.read()
except FileNotFoundError:
	print("Can not find " + filename)
else:
	print(contents.lower().count('alice'))