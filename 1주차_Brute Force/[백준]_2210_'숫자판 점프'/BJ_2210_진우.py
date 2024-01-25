numBoard = [list(map(int, input().split())) for _ in range(5)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
result = set()
case = list()
def Moving(x, y, n):
    if n == 6:
        if len(case) == 6:
            result.add(''.join(map(str, case)))
        return

    for dir in range(4):
        nx, ny = x + dx[dir], y + dy[dir]
        if 0 <= nx < 5 and 0 <= ny < 5:  # 숫자판 범위
            case.append(numBoard[x][y])
            Moving(nx, ny, n + 1)
            case.pop()

for x in range(5):
    for y in range(5):
        Moving(x, y, 0)

print(len(result))
