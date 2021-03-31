from ytmusicapi import YTMusic

ytmusic = YTMusic('headers_auth.json')

import sqlite3
import time
conn = sqlite3.connect('./music.db')
db_cursor = conn.cursor()
db_cursor.execute('select * from playlist')
url_list = db_cursor.fetchall()
playlist_dict = {}
print(ytmusic.get_library_playlists)
#for url in url_list :
#    playlist_dict[url[0]] = ytmusic.create_playlist(str(url[0]), f"{url[0]} 플레이리스트")
#    time.sleep(3)
#    print(url[0])
db_cursor.execute('select * from music')
music_list = db_cursor.fetchall()

for music in music_list[310:]:
    time.sleep(2)
    search_results = ytmusic.search(f"{music[1]} {music[2]}")
    print(music[1])
    try:
        ytmusic.add_playlist_items('PLMpbFDNBjcXT_N0y4x2mGGcaNPi_xb5YI', [search_results[0]['videoId']])
    except:
        continue
    #ytmusic.add_playlist_items(playlist_dict[music[3]], [search_results[0]['videoId']])