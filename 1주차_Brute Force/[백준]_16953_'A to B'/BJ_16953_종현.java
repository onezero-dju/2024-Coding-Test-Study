package 일영_코테_준비;

import java.util.*;

public class BJ_16953 {
    public static void main(String[] args) {
        // Scanner 객체를 생성하여 사용자의 입력을 받기.
        Scanner sc = new Scanner(System.in);

        // 첫 번째 입력값
        int a = sc.nextInt();
        // 두 번째 입력값
        int b = sc.nextInt();

        // 연산 횟수를 저장할 변수 cnt를 0으로 초기화.
        int cnt = 0;

        // 무한 루프 => 이 루프는 a와 b가 같아지거나, a를 b로 만들 수 없는 경우에만 종료
        while (true) {
            // a == b
            if (a == b) {
                // 현재까지의 연산 횟수(cnt)에 1을 더한 값을 출력하고 루프를 종료합니다.
                System.out.println(cnt + 1);
                break;
            }
            // b가 a보다 작아진 경우, 또는 b가 2로 나누어 떨어지지 않고 b의 가장 오른쪽 숫자가 1이 아닌 경우.
            else if (b < a || b % 2 != 0 && b % 10 != 1) {
                // a를 b로 만들 수 없으므로 -1을 출력하고 루프를 종료.
                System.out.println(-1);
                break;
            }
            // 그 외의 경우 = 문제 조건 만족.
            else {
                // b의 가장 오른쪽 숫자가 1인 경우.
                if (b % 10 == 1) {
                    // b를 10으로 나누어 1을 오른쪽에서 제거.
                    b /= 10;
                }
                // b가 2로 나누어 떨어지는 경우.
                else {
                    b /= 2;
                }
                // 연산 횟수(cnt)를 1 증가.
                cnt++;
            }
        }
        // Scanner 객체를 닫기.
        sc.close();
    }
}
