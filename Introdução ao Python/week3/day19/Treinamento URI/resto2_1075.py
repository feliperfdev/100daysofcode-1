num = int(input())
assert(num < 10000)

for n in range(1, 10001):
    if n%num==2:
        print(n)