# 由于8.6.1的例题要求, 将以上代码全部删除
def make_pizza(size, *toppings):
    """概述要制作的披萨"""
    print("\nMaking a " + str(size) + 
            "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
