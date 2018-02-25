favorite_places = {
    'tiffany': ['1', '2', '3'],
    'einstein': ['4', '5'],
    'nutcheer': ['6', '7', '8'],
}
for name, places in favorite_places.items():
    print(name+":")
    for place in places:
        print("\t"+place)
