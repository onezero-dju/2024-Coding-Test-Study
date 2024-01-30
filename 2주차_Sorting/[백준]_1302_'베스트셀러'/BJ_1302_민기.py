"""
하루 동안 팔린 책의 개수를 입력 받고
개수에 따라 책 제목을 입력한다. 단, 책 제목은 알파벳 소문자로만 이루어져 있다.

입력 받은 책에 따라 가장 많이 팔린 책의 제목을 출력해라.

#! 중복되는 책을 더하고, 중복되는 책이 여러가지면 abcd 순에서 가장 앞서는 제목을 출력한다.
"""
counter = {} # dictionary 형

x = int(input()) # 몇개의 책을 입력 받을지 선택
y = [str(input()) for i in range(x)] # 입력 받은 수만큼 입력받기
z = [] # 빈 배열

for value in y: # 중복된 제목 개수 확인하기
    try: counter[value] += 1
    except: counter[value] = 1

max_counter = max(list(counter.values()))
for i in list(counter.keys()):
    if counter[i] == max_counter:
        z.append(i)
z.sort()

print(''.join(z)) # 출력

