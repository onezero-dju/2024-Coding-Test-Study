

a = input() #c or d 입럭받기


if a[0] == 'c':
    num = 26
    if a[1] == 'c':
        num *= 25
    else:
        num *= 10
        if a[1] == 'c' and a[2] == 'c':
            num *= 25
        elif a[1] == 'd' and a[2] == 'c':
            num *= 26
        elif a[1] == 'c' and a[2] == 'd':
            num *= 10
        elif a[1] == 'd' and a[2] == 'd':
            num *= 9
            
            if a[2] == 'c' and a[3] == 'c':
                num *= 25
            elif a[2] == 'd' and a[3] == 'c':
                num *= 26
            elif a[2] == 'c' and a[3] == 'd':
                num *= 10
            elif a[2] == 'd' and a[3] == 'd':
                num *= 9

elif a[0] == 'd':
    num = 10
    if a[1] == 'd':
        num *= 9
    else:
        num *= 26
        if a[1] == 'd' and a[2] == 'd':
            num *= 9
        elif a[1] == 'c' and a[2] == 'd':
            num *= 10
        elif a[1] == 'd' and a[2] == 'c':
            num *= 26
        elif a[1] == 'c' and a[2] == 'c':
            num *= 25


            if a[2] == 'd' and a[3] == 'd':
                num *= 9
            elif a[2] == 'c' and a[3] == 'd':
                num *= 10
            elif a[2] == 'd' and a[3] == 'c':
                num *= 26
            elif a[2] == 'c' and a[3] == 'c':
                num *= 25


print(num)











# x = rancdom.randrange(1,5)
# if x == 1:
#     random_alphabet = [random.choice('cd') for i in range(1)]

# elif x == 2:
#     random_alphabet = [random.choice('cd') for i in range(2)]
# elif x ==3:
#     random_alphabet = [random.choice('cd') for i in range(3)]
# elif x ==4:
#     random_alphabet = [random.choice('cd') for i in range(4)]