cities = {
    'paris': {
        'country': 'france',
        'population': 12345678,
        'fact': 'romance',
    },
    'berlin': {
        'country': 'germen',
        'population': 12332112,
        'fact': 'serious',
    },
    'beijing': {
        'country': 'china',
        'population': 98765432,
        'fact': 'power',
    },
}
for city, city_info in cities.items():
    print(city+":")
    for info, info_ans in city_info.items():
        print(info+":"+str(info_ans))
