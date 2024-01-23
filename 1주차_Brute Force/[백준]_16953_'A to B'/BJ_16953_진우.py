a, b = map(int, input().split())

min = 1
while True:
    if a == b:
        break

    elif (b % 2 != 0 and b % 10 != 1) or b < a:
        print(-1)
        exit()

    else:
        if b % 10 == 1:
            b //= 10
            min += 1
        else:
            b //= 2
            min += 1

print(min)