"""
Baekjoon Online Judge
Number: 16968
Title: 차량 번호판 1

Comment
1. c -> c : 26 * 25
2. c -> d -> : 26 * 10 * 26
3. d -> d : 10 * 9
4. d -> c -> d : 10 * 26 * 10

Imporvment
- DFS로 구현

"""

# input (번호판 형식)
car_num = input()

# 고려해야 하는 경우의 수는 4가지
## c로 시작 -> c or d
## d로 시작 -> d or c
def typeCD(car_num):
    output_num = 1
    for count in range(len(car_num)):
        if car_num[count] == 'c':
            if count > 0 and car_num[count] == car_num[count-1]:
                output_num *= 25
            else:
                output_num *= 26
        elif car_num[count] == 'd':
            if count > 0 and car_num[count] == car_num[count-1]:
                output_num *= 9
            else:
                output_num *= 10
    return output_num

print(typeCD(car_num))