"""
사용가능 숫자 : 0 ~ 9 (10개)
사용가능 문자 : a, b, c, d, ..., y, z (26개)

번호판 최대 4글자
c : 문자 / d : 숫자
같은 문자 or 숫자 반복X

dict는 내부적으로 해시 테이블을 이용하므로 데이터의 '조회 및 수정이 O(1)'의 시간복잡도를 가진다!
"""

dict = {'c':26, 'd':10}
board = input()

sol = dict[board[0]]

for i in range(1,len(board)):
  tVal = dict[board[i]]
  if board[i] == board[i-1]:
    tVal -= 1
  sol *= tVal
print(sol)