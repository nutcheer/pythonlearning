while True:
	try:
		num1 = input("Enter a number('q' to quit): ")
		num2 = input("Enter another number('q' to quit): ")
		if num1 == 'q' or num2 == 'q':
			print("Ready to quit.")
			break
		num = int(num1) + int(num2)
	except ValueError:
		print("Please enter a number!")
	else:
		print(num)
