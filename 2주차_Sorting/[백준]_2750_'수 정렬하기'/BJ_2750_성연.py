# 백준 2750번
# 결국 풀기는 했지만 시간이 꽤 걸렸다
# 아직 파이썬에 대한 이해(for문 _ 이용)가 부족하다고 느꼈고 현재 수준으로는 백준 2750번 문제 난이도로 연습을 진행해야 할 것 같다

n = int(input())  # 첫 번째 정수 입력받기
nums = [int(input()) for _ in range(n)]  # n번만큼 정수 입력받기, 문제에서 숫자 중복은 안된다고 나온다


def bubbleSort(nums):
    numlen = len(nums) # nums의 길이
    i = 0
    for _ in range(numlen-1):  # for문 수행한 결과를 모든 요소마다 실행해야 하므로 다시 for문 사용
        for i in range(numlen-1): # 아래 과정을 길이만큼 반복
                if nums[i] > nums[i+1]: # nums[i]가 nums[i+1]보다 크다면 서로 위치를 바꾼다
                    nums[i], nums[i+1] = nums[i+1], nums[i]
    return nums

bubbleSort(nums)

for i in nums:
    print(i)
