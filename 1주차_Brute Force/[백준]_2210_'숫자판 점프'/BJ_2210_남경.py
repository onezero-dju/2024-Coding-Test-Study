import sys
sys.setrecursionlimit(10 ** 6)

ans = set() # 중복이 제거된 6자리 문자열 담을 set
di = [(0,1),(1,0),(0,-1),(-1,0)] # 현 위치 기준 움직일 방향
matrix = [list(map(int, sys.stdin.readline().rstrip().split())) for i in range(5)]

# dfs(x, y, 임시문자열)
def dfs(x:int, y:int, temp:str):
  # 6자리 만들어지면 append
  if len(temp) == 6:
    ans.add(temp);
    return
  
  temp += str(matrix[x][y])
  
  for dx, dy in di:
    nx = x+dx;
    ny = y+dy;
    if 5>nx>=0 and 5>ny>=0: # 범위 내인 경우
      dfs(nx, ny, temp)
    else:
      continue
  
for i in range(5):
  for j in range(5):
    dfs(i, j, "")
print(len(ans))
