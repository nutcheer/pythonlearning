favorite_numbers = {
    'Albert': [1,6],
    'Tiffany': [2,7,8],
    'Jerry': [3],
    'Caroline':[4],
    'Sheldon':[5,9],
}
for name, numbers in favorite_numbers.items():
    print(name.title()+"'s favorite number are ")
    for number in numbers:
        print("\t"+str(number))
