import json

number = input("Enter a number:")
filename = "favorite_number.json"
with open(filename, 'w') as f_obj:
	json.dump(number, f_obj)
	print("I've known your favorite number.")

try:
	with open(filename) as f_obj:
		fav_num = json.load(f_obj)
except FileNotFoundError:
		print("Can not find " + filename)
else:
	print("Your favorite number is " + str(fav_num))