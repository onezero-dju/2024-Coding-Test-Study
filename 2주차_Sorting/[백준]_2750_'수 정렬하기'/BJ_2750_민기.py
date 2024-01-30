"""
오름차순으로 정렬
첫째 줄에 수의 개수는 1~1000
둘째 줄부터는 N개의 줄에는 수가 주어진다.
수는 중복 X

# 혼자서 30분을 풀다 결국 답지를 보았음

#! 밑에는 답지를 본 코드
# x = int(input())
# list = []
# for i in range(x):
#     list.append(int(input()))
#     list1 = sorted(list)
# for i in range(len(list1)):
#     print(list1[i])

답지를 본 후 배열의 원소를 출력해야 한다는 것을 깨닫고
for문을 활용해 배열을 하나 씩 출력 했음
그리고, 더 빠른 시간을 위해 코드 압축을 진행하였고
필요 없다고 느낀 코드는 주석처리를 진행하였음

#? 아래는 혼자 고민한 코드의 내용
"""

x = int(input()) # 몇개의 수를 입력 받을지 선택
y = [int(input()) for i in range(x)] # 입력 받은 수만큼 입력받기
result = [] # 결과 값을 받기위한 새로운 빈 배열 생성

for value in y: # 중복을 제거하는 for문
    if value not in result:
        result.append(value)

result.sort()

for i in range(len(result)):
    print(result[i])

# for i in range(len(result)):
#     min_i = i # 가장 작은 원소의 인덱스
#     for j in range(i+1, len(result)):
#         if(result[min_i] > result[j]):
#             min_i = j
#     result[i], result[min_i] = result[min_i], result[i] # 스왑
#     print(result[i])

# for i in range(len(result)):
#     print(result[i]) # 결과값 출력

