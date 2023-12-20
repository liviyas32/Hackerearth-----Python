word = input().lower()

zcount = word.count('z')
ocount = word.count('o')
if (ocount == (zcount*2)) & (ocount%2 == 0):
    print('Yes')
else:
    print('No')
