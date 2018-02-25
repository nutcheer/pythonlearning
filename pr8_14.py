def make_car(name, num, **info):
    carfile = {}
    carfile['name'] = name
    carfile['num'] = num
    for key, value in info.items():
        carfile[key] = value
    return carfile
    
car = make_car('subaru', 'outback', color='blue', tow_package=True)

print(car)
