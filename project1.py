import lyricsgenius

genius = lyricsgenius.Genius("UN6D3t7AFvOogZ48g_ZglSiSB-MENGaBTfbiFC8eHDskCM5rf8Hqg7newjpF9T7D")
artist = genius.search_artist("Eminem", max_songs=3, sort="title")
song = genius.search_song("Mockingbird", artist.name)
print(song.lyrics)
artist.save_lyrics()
with open('lyrics_json' + '.json', 'w') as outfile:
    json.dump(all_lyrics, outfile)

