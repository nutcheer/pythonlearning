active = True
places = []
while active:
    place_info = input("If you could visit one place in the world, where would you go\n")
    if place_info == "quit":
        active = False
        break
    places.append(place_info)

print("\n--- Dreamed Place to Visit ---")
for place in places:
    print(place)
