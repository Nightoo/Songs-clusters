from lyricsgenius import Genius
import string
import csv
from collections import Counter


def words(text):
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.lower().split()

    stopwords = ['the', 'and', 'a', 'that', 'i', 'it', 'not', 'he', 'as',
                 'you', 'this', 'but', 'his', 'they', 'her', 'she', 'or',
                 'an', 'will', 'my', 'one', 'all', 'would', 'there', 'their',
                 'to', 'of', 'in', 'for', 'of', 'with', 'at', 'by', 'from',
                 'up', 'about', 'into', 'over', 'after', 'to', 'on',
                 'am', 'is', 'are', 'was', 'were', 'be']

    pronouns = ['i', 'we', 'you', 'thou', 'he', 'she', 'it', 'they',
                'me', 'us', 'thee', 'him', 'her', 'them', 'mine',
                'ours', 'yours', 'thine', 'his', 'hers', 'theirs',
                'my', 'our', 'your', 'thy', 'its', 'their', 'im',
                'ive', 'id', 'hes', 'shes', 'youve', 'youd', 'weve', 'wed',
                'theyve', 'theyd', 'hed', 'shed', 'youre']

    resultwords = [word for word in text if (word not in stopwords) and (word not in pronouns) and
                   ('contributors' not in word) and ('lyrics' not in word) and (word.isalpha())]

    text = ' '.join(resultwords)
    text = text.split()
    data = Counter(text)
    s = ''
    for el in data.most_common(20):
        s += el[0]
        s += ' '
    return s


genius = Genius('token', timeout=15, retries=3)
genius.remove_section_headers = True


artists_name = [
    'The Prodigy',
    'Michael Jackson',
    'Taylor Swift',
    'Cannibal Corpse',
    'Napalm Death',
    'Fiona Apple',
    'Lil Uzi Vert',
    'Johnny Cash',
    'XXXTENTACION',
    'Kanye West'
]


with open('songs_s.csv', 'a', encoding="utf-8") as file:
    writer = csv.writer(file)
    for artist_name in artists_name:
        artist = genius.search_artist(artist_name, max_songs=40)
        print('------------')
        for song in artist.songs:
            text = song.lyrics
            word = [words(text)]
            word.insert(0, song.title)
            word.insert(0, artist_name)
            print(word)
            writer.writerow(word)
