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
