"""
2를 곱한다.
1을 수의 가장 오른쪽에 추가한다. -> 1의자리가 1이 아니면고 짝수면 2를 나누기
"""
import sys
A, B = map(int,  sys.stdin.readline().rstrip().split())
cnt = 1

def func(A, B):
  global cnt
  if A == B:
    print(cnt)
    return
  elif A > B:
    print(-1)
    return

  if B%2 == 0:
    cnt += 1
    func(A, B//2)
  elif B%10 == 1:
    cnt += 1
    func(A, B//10)
  else :
    print(-1)
    return
  
func(A, B)