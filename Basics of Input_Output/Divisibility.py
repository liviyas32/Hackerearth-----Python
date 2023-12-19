N = int(input())
data = [int(x) for x in input().split()]


# Write your code here
rev = 0
for i in data:
    dig = i%10
    rev = (rev*10)+dig

if rev%10 == 0:
    print('Yes')
else:
    print('No')
