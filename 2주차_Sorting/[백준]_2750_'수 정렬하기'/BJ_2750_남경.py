import sys
N = int(sys.stdin.readline())
numList = []
for i in range(N):
  numList.append(int(sys.stdin.readline()))

numList.sort()
for i in numList:
  print(i)