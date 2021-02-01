def make_album(artist_name, album_title,songs=None):
    if songs:
        album = {'name': artist_name, 'title' : album_title,'tracks': songs}
    else:
        album = {'name': artist_name, 'title' : album_title,}
    if songs:
        album['tracks'] = songs    
    return album

while True:
    print("you can quit by pressing 'q'")
    artist_name = input("give me a artist name: ")
    if artist_name == "q":
        break
    album_title = input("give me a album name: ")
    if album_title == 'q':
        break

    result = make_album(artist_name,album_title)
    print(result)
