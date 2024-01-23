"""
Baekjoon Online Judge
Number: 12931
Title: 두 배 더하기

Comment


Improvement
- Greedy로 구현

"""

# sys - input() 함수의 단점인 느린 속도를 보완하기 위해 정의
import sys
input = sys.stdin.readline

# input (19: 배열 크기 N, 20: 배열 B의 인덱스 값들)
list_size = int(input())
listB_val = [list(map(int, input().split())) for _ in range(list_size)]
