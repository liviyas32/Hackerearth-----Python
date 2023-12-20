data = input().split()
low = int(data[0])
high = int(data[1])
k = int(data[2])

count = 0
for i in range(low, high+1):
    if i%k == 0:
        count += 1

print(count)
