A = int(input())
B = [int(i) for i in input().split()]

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
    global calc_cnt
    if all(i % 2 == 0 for i in B):
        for i in range(A):
            B[i] //= 2
        calc_cnt += 1
    
def main(arr: list[int]):
    while not is_end(arr):
        make_all_even(arr)
        devide_by_two(arr)
    print(calc_cnt)

if __name__ == "__main__":
    main(B)
