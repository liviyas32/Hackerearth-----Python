N = int(input())
A = input().split()

product = 1
for i in A:
    product = (product*int(i))%(10**9+7)

print(product)
