def make_album(artist_name, album_title,songs=None):
    if songs:
        album = {'name': artist_name, 'title' : album_title,'tracks': songs}
    else:
        album = {'name': artist_name, 'title' : album_title,}
    if songs:
        album['tracks'] = songs    
    return album


result = make_album('Ricky','Maria',songs=10)
print(result)
result = make_album('Michel Jackson','Thriller')
print(result)
result = make_album('Ar rahman','uyire')
print(result)