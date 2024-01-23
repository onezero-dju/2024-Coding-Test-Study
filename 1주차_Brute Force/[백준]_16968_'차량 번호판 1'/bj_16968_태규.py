s = input()

# 첫 문자가 c인 경우
if s[0] == 'c': 
    num = 26
else:
    num = 10
    
# 두 번째 문자
for i in range(1, len(s)):
    if s[i] == 'c': # c인경우
        if s[i - 1] == 'c': # c가 연속인 경우
            num *= 25
        else:
            num *= 26
    else:           # d인경우
        if s[i - 1] == 'd': # d가 연속인 경우
            num *= 9
        else:
            num *= 10

print(num)