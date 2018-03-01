try:
	num1 = input("Enter a number('q' to quit): ")
	num2 = input("Enter another number('q' to quit): ")
	num = int(num1) + int(num2)
except ValueError:
		print("Please enter a number!")
else:
		print(num)
