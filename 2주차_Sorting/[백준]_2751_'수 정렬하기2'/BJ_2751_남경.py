"""
1. 내장함수 (merge sort 기반) -> O
"""
import sys
N = int(sys.stdin.readline())
numList = []
for i in range(N):
  numList.append(int(sys.stdin.readline()))

numList.sort()
for i in numList:
  print(i)

"""
2. 퀵 정렬 -> X (시간초과)
"""
# 분할 함수
# numList: 숫자list, l: 가장왼쪽, r:가장오른쪽
def partition(numList, l, r):
  # pivot 설정 (가장 왼쪽 위치)
  pivot = numList[l]
  # 조사위치 l과 r이 서로 교차하기 전까지 반복
  while l<r:
    # l이 r보다 작거나 같고 l위치 아이템이 pivot보다 작은 경우(교체대상X)
    while l<=r and numList[l]<pivot:
      # 이동
      l+=1
    # l이 r보다 작거나 같고 r위치 아이템이 pivot보다 큰 경우(교체대상X)
    while l<=r and numList[r]>pivot:
      # 이동
      r-=1
    
    # 아직 교차되지 않은 상태, l과 r 아이템 위치 변경
    if l<r:
      # swap
      numList[l], numList[r] = numList[r], numList[l]
  
  # 반복문 이후 교차상태, l과 r 아이템 swap
  numList[l], numList[r] = numList[l], numList[r]
  # pivot이 들어갈 위치 반환
  return r

# 퀵 정렬
def quickSort(numList, l, r):
  if l < r:
    p = partition(numList, l, r)
    quickSort(numList, l, p-1)
    quickSort(numList, p+1, r)
quickSort(numList, 0, N-1)

print(numList)

