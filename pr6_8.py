cat = {
    'name': 'cat',
    'master': 'master1',
}
dog = {
    'name': 'dog',
    'master': 'master2',
}

pets = [cat, dog]
for pet in pets:
    for key, value in pet.items():
        print(key+":"+value)
    print("\n")
