#!pip install lyricsgenius - download and install python and run this code first

import lyricsgenius
import json

# lyricsgenius needs token from genius API(to use, get your token and write it below)

genius = lyricsgenius.Genius("Your Token here",
                             verbose=False,
                             skip_non_songs=False
                             )

#%%

# type the artist name to get the lyrics

artist_name = "Okaber"
artist = genius.search_artist(f"{artist_name}", sort="title")

#%%

# save the lyrics as json

artist.save_lyrics()

#%%

# get the json file to extract lyrics

with open(f"Lyrics_{artist_name}.json", "r") as read_file:  # if this code doesn't work, change it to created json file
    data = json.load(read_file)


#%%

# get the title and lyrics to a lyrics list

lyrics = ''
titles = ''
for songs in data['songs']:
    titles += '\n' + songs['full_title']  # you can delete it if you don't want to get lyrics
    lyrics += '\n' + songs['lyrics']

#%%

# creating a file for artist and dump the lyrics and titles (you can delete the titles part)

# titles
text_file = open(f'{artist_name}_titles.txt', "wt", encoding='utf-8')
text_file.write(titles)

# lyrics
text_file = open(f'{artist_name}_lyrics.txt', "wt", encoding='utf-8')
text_file.write(lyrics)
