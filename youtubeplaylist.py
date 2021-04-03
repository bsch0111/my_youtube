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

no_insert_data = []
playlist_id = ''
playlist_no = 1
    
for index, music in enumerate(music_list):
    
    if index == 0:
        playlist_id = ytmusic.create_playlist(str(playlist_no) +"번째 플레이리스트", f"{playlist_no}번째 플레이리스트")
        playlist_no = playlist_no + 1 
    elif index%500 == 0 :
        playlist_id = ytmusic.create_playlist(str(playlist_no) +"번째 플레이리스트", f"{playlist_no}번째 플레이리스트")
        playlist_no = playlist_no + 1

    time.sleep(1)
    search_results = ytmusic.search(f"{music[1]} {music[2]}")
    print('music : '+ music[1])
    print('artist: '+ music[2])
    


    try:
        ytmusic.add_playlist_items(playlist_id, [search_results[0]['videoId']])
    except:
        no_insert_data.append(f"{music[1]} {music[2]}")
        continue
    #ytmusic.add_playlist_items(playlist_dict[music[3]], [search_results[0]['videoId']])

print('--------------------------------------여기서부터는 미입력된 데이터입니다.')
print(no_insert_data)


with open('no_insert_data.txt', 'w') as filehandle:
    filehandle.writelines("%s\n" % m_line for m_line in no_insert_data)
