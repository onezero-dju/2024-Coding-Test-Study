package 일영_코테_준비;

import java.util.Scanner;

public class BJ_12931 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] B = new int[N];

        for(int i=0; i<N; i++){
            B[i] = sc.nextInt(); // 배열 B의 원소를 입력 받기..
        }

        int cnt = calculateMinimumOperations(B); // 배열 A를 B로 변환하는 데 필요한 최소 연산 횟수를 계산.

        System.out.println(cnt); // 계산된 연산 횟수를 출력합니다.
    }

    // 배열 A를 B로 변환하는 데 필요한 최소 연산 횟수를 계산하는 함수.
    private static int calculateMinimumOperations(int[] arr){
        int operations = 0;

        while(sum(arr) != 0){ // 배열의 모든 원소가 0이 될 때까지 반복.
            operations += subtractOneFromOddNumbers(arr); // 배열의 홀수 원소들을 1씩 감소시킵니다.
            if(sum(arr) != 0){ // 배열의 모든 원소가 0이 아니라면
                divideAllNumbersByTwo(arr); // 배열의 모든 원소를 2로 나눕니다.
                operations++; // 연산 횟수를 1 증가시킵니다.
            }
        }

        return operations; // 연산 횟수를 반환합니다.
    }

    // 배열의 홀수 원소들을 1씩 감소시키는 함수입니다. 감소시킨 횟수를 반환합니다.
    private static int subtractOneFromOddNumbers(int[] arr){
        int operations = 0;
        for(int i=0; i<arr.length; i++){
            if(arr[i] % 2 != 0){ // 원소가 홀수라면
                arr[i] -= 1; // 원소를 1 감소시킵니다.
                operations++; // 연산 횟수를 1 증가시킵니다.
            }
        }
        return operations; // 연산 횟수를 반환합니다.
    }

    // 배열의 모든 원소를 2로 나누는 함수입니다.
    private static void divideAllNumbersByTwo(int[] arr){
        for(int i=0; i<arr.length; i++){
            arr[i] /= 2; // 원소를 2로 나눕니다.
        }
    }

    // 배열의 모든 원소를 합산하는 함수입니다.
    private static int sum(int[] arr){
        int sum = 0;
        for(int i: arr){ // 배열의 모든 원소에 대해
            sum += i; // 원소를 합산합니다.
        }
        return sum; // 합산된 결과를 반환합니다.
    }
}

