"""
Baekjoon Online Judge
Number: 16953
Title: A -> B

Comment
1. A * 2
2. B * 10 + 1

"""

import sys

num_A, num_B = map(int, sys.stdin.readline().split())

def switchNum (num_A, num_B):
    Count_rslt = 0
    while num_B > num_A:
        if num_B % 2 != 0:
            num_B = (num_B - 1) / 10
        elif num_B % 2 == 0:
            num_B /= 2
        else:
            return -1
        Count_rslt += 1

    return Count_rslt+1 if num_B == num_A else -1


print(switchNum(num_A, num_B))