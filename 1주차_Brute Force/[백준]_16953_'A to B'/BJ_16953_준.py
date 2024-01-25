"""
Baekjoon Online Judge
Number: 16953
Title: A -> B

Comment
A -> B
1. A * 2
2. B * 10 + 1

B -> A
1. B / 2
2. (B - 1) / 10

Improvement
- BFS로 구현

"""

# sys - input() 함수의 단점인 느린 속도를 보완하기 위해 정의
import sys
input = sys.stdin.readline

# input (A, B)
num_A, num_B = map(int, input().split())

# 가능한 연산을 Top-down 방식으로 변경하여 진행
## A * 2 -> B / 2
## B * 10 + 1 -> (B - 1) / 10
def switchNum (num_A, num_B):
    Count_rslt = 0
    while num_B > num_A:
        if num_B % 2 == 0:
            num_B /= 2
        elif num_B % 2 == 0:
            num_B = (num_B - 1) / 10
        else:
            return -1
        Count_rslt += 1

    return Count_rslt + 1 if num_B == num_A else -1


print(switchNum(num_A, num_B))