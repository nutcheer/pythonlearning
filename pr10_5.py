filename = "Why_choose_programming.txt"
with open(filename, 'a') as file_object:
	while  True:
		reason = input("Enter the reason(q to quit):")
		if reason == 'q':
			break
		file_object.write(reason + "\n")