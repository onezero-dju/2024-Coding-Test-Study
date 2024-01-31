import sys
N = int(sys.stdin.readline().rstrip())
valDict = set()
for i in range(N):
  val = sys.stdin.readline().rstrip()
  valDict.add(val)

for i in sorted(valDict, key=lambda x : (len(x),x) ):
  print(i)