count = int(input())
numArray = [int(input()) for _ in range(count)]

result = sorted(numArray)
for n in result:
    print(n)