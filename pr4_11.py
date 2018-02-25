pizzas = ['pepperoni','beef','fruit']
friend_pizzas = pizzas[:]
pizzas.append('vegetable')
friend_pizzas.append('button')
print("My favorite pizzas are:")
for pizza in pizzas:
	print(pizza)
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
	print(pizza)
