"""
Baekjoon Online Judge
Number: 2210
Title: 숫자판 점프

Comment


Improvement


"""

# sys - input() 함수의 단점인 느린 속도를 보완하기 위해 정의
import sys
input = sys.stdin.readline

# input (5x5 matrix)
listB_val = [list(map(int, input().split())) for _ in range(5)]
