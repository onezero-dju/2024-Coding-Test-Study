import sys

A = int(input())
B = list(map(int, sys.stdin.readline().strip().split()))

def is_end(B: list[int]):
    if set(B) == {0}:
        return True
    else:
        return False

calc_cnt = 0
def make_all_even(B: list[int]):
    global calc_cnt
    for i in range(A):
        if B[i] % 2 != 0:
            B[i] -= 1
            calc_cnt += 1
            
def devide_by_two(B: list[int]):
    if is_end(B):  #? 꼭 한 번 더 검사해야?
        return
    global calc_cnt
    for i in range(A):
        B[i] //= 2
    calc_cnt += 1
    
def main(arr: list[int]):
    if is_end(arr):
        print(calc_cnt)
        return
    else:
        make_all_even(arr)
        devide_by_two(arr)
        main(arr)  # 재귀
    

if __name__ == "__main__":
    main(B)
