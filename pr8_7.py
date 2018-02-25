def make_album(singer, album_name, number = '0'):
    album = {"singer": singer, "album's name": album_name, "number of songs": number}
    return album
    
album1 = make_album("1", "11", '1')
album2 = make_album("2", "22")
album3 = make_album("3", "33")

print(album1)
print(album2)
print(album3)
