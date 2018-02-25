name1 = {
    'first_name': 'mclean',
    'last_name': 'tiffany',
    'age': '20',
    'city': 'Berlin',
}
name2 = {
    'first_name': 'albert',
    'last_name': 'einstein',
    'age': '60',
    'city': 'Shanghai'
}
name3 = {
    'first_name': 'Jack',
    'last_name': 'Ma',
    'age': '42',
    'city': 'Hangzhou'
}

people = [name1, name2, name3]

for person in people:
    for key, value in person.items():
        print(key+":"+value)
        
