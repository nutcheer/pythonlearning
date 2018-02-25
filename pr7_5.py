active = True
while active:
    sage = int(input("Please enter your age:"))
    
    if sage < 3 and sage >= 0:
        print("You are free to see the movie!")
    elif sage <= 12:
        print("You need to pay 10 dollars for this movies!")
    elif sage < 120:
        print("You need to pay 15 dollars for this movies!")
    else:
        break
