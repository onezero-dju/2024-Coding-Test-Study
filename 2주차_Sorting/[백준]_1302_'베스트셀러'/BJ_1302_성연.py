# Counter 이용해서 어떤 값이 제일 많은지 찾아낼 수 있다
# 동일 개수라면 알파벳순으로 앞에 나오는 문자를 출력해야 하는데 여기서 막혔다

from collections import Counter
n = int(input())  # 첫 번째 정수 입력받기
nums = [(input()) for _ in range(n)]

word_counts = Counter(nums) 
most = word_counts.most_common(1)
mostValue = most[0][0]
print(mostValue)