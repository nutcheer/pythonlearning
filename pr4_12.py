my_foods = ['pizza','falafel','carrot cake']
for food in my_foods:
	print(food)
friend_foods = my_foods[:]
my_foods.append('cannoli')
for food in my_foods:
	print(food)
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorte foods are:")
print(friend_foods)

