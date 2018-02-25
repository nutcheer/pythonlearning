requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese")
    
print("\nFinished making your pizza!")


requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are not of green peppers right now.")
    else:
        print("Adding "+requested+'.')
print("\nFinished making your pizza!")
