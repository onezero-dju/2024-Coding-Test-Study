type = input()
case = 0
prev = 0

for i, letter in enumerate(type):
    if letter == 'c':
        if i == 0:
            case += 26
        elif i != 0 and prev != 'c':
            case *= 26
        else:
            case *= 25
        prev = 'c'
    elif letter == 'd':
        if i == 0:
            case += 10
        elif i != 0 and prev != 'd':
            case *= 10
        else:
            case *= 9
        prev = 'd'

print(case)
