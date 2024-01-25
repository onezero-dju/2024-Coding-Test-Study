"""
0으로 채워져 있는 길이가 N인 배열 A

배열에 있는 값 하나를 1 증가시킨다.
배열에 있는 모든 값을 두 배 시킨다.

배열 A를 B로 만들기 위한 연산의 최소 횟수


"""
import sys
N = int(input())
A = [0 for i in range(N)]
B = list(map(int, sys.stdin.readline().strip().split()))

# 연산 횟수
cnt = 0

# 모든 원소가 0일때 stop
while sum(B) != 0:
  # B의 모든 원소에 대해서 탐색
  for i in range(N):
    # 현재 원소 0 일때
    if B[i] == 0:
      continue # 다음 원소 탐색
    # 홀수 일때 -> 1뺴기
    if B[i] % 2 != 0:
      B[i] -= 1
      cnt += 1
  # for문 탈출 시 모든 원소 짝수

  # 아직 모든 원소가 0이 아닐때 전체 2로 나누기
  if sum(B) != 0:
    B = [i//2 for i in B]
    cnt += 1

print(cnt)