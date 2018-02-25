sandwich_orders = ['1', '2', '3']
finished_sandwiches = []
temp = ""
while sandwich_orders:
    temp = sandwich_orders.pop()
    print("I made your " + temp + " sandwich.")
    finished_sandwiches.append(temp)
    
print(finished_sandwiches)
