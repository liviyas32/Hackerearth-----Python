length = int(input())
photos = int(input())

for i in range(photos):
    dimension = input().split()
    width = int(dimension[0])
    height = int(dimension[1])

    if (width == height):
        if (width >= length) & (height >= length):
            print('ACCEPTED')
        if (width < length) | (height < length):
            print('UPLOAD ANOTHER')

    if (width != height):
        if (width >= length) & (height >= length):
            print('CROP IT')

        if (width < length) | (height < length):
            print('UPLOAD ANOTHER')
