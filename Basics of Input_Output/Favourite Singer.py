
total_songs = int(input())
song_dict = dict()

song = input().split()

for i in range(total_songs):
    if song[i] not in song_dict:
        song_dict[song[i]] = 1
    else:
        song_dict[song[i]] += 1 

fav_singer_list = []
for i,j in song_dict.items():
    if (j == max(song_dict.values())) & (i not in fav_singer_list):
        fav_singer_list.append(i)

print(len(fav_singer_list))


# Otherway
from collections import Counter

total_songs = int(input())
song = input().split()

song_dict = Counter(song)
max_count = max(song_dict.values())

fav_singer_set = set()
for singer,count in song_dict.items():
    if count == max_count:
        fav_singer_set.add(singer)

print(len(fav_singer_set))
