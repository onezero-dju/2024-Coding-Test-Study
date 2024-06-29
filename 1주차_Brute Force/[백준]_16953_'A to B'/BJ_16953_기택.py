input = [int(i) for i in input().split()]

calc_cnt = 0

def is_end(init:int, result:int):
    global calc_cnt
    # 변환에 성공하거나 실패하는 경우 종료
    return True if (init is result) or (calc_cnt == -2) else False


def is_one_at_right_end(num):
    return True if str(num)[-1] == '1' else False


def temp(num):
    global calc_cnt
    if is_one_at_right_end(num):  # 숫자의 오른쪽 끝이 1로 끝나는지 확인 
        # 1을 빼고 10으로 나눠, 숫자 오른쪽 끝의 1을 제거  #? 문자열로 취급하는 게 낫나?
        # num -= 1
        num //= 10
        calc_cnt += 1
    elif num % 2 == 0:  # 짝수 확인
        num //= 2
        calc_cnt += 1
    else:
        calc_cnt = -2  #* 1로 끝나지도, 짝수도 아닌 경우 진행 불가
    return num
    
    
def main(num_A, num_B):
    global calc_cnt
    if num_A > num_B:
        calc_cnt = -2  #* 계산 결과가 입력값(A)보다 작아진다면 연산 무의미
    if is_end(num_A, num_B):
        print(calc_cnt + 1)  # 결과 출력(최솟값+1)  #? 위 연산 과정에서 calc_cnt가 -2가 아닌 -1로 받아도 되게 하는 방법은?
        return
    else:
        num_B = temp(num_B)
        main(num_A, num_B)  # 재귀
        
    
if __name__ == "__main__":
    main(input[0], input[1])
