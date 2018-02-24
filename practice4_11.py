pizzas = ['1', '2', '3']
for pizza in pizzas:
	print("I like " + pizza + " pizza.\n")

print("I really love pizza!")

friend_pizzas = pizzas[:]
friend_pizzas.append('4')
print("My favorite pizzas are:")
for pizza in pizzas:
	print(pizza)

print("My friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
	print(friend_pizza)