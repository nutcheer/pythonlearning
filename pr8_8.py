def make_album(singer, album_name, number = '0'):
    album = {"singer": singer, "album's name": album_name, "number of songs": number}
    return album
    
while True:
    singer = input("Please enter the singer  ")
    album_name = input("Please enter the album_name  ")
    number = input("Please enter the number of songs  ")
    if singer == 'q' or album_name == 'q' or number == '0':
        break
    print(make_album(singer, album_name, number))
    
