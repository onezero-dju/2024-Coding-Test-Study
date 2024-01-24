package 일영_코테_준비;

import java.util.Scanner;

public class BJ_16968 {
    public static void main(String[] args) {
        Scanner scan=new Scanner(System.in);

        // 형식 입력 받기
        String format = scan.nextLine();

        // 차량 번호판 계산 결과
        int result = countCarNumber(format);

        // 결과 출력
        System.out.println(result);

    }
    public static int countCarNumber(String format){
        int count = 0;
        // 입력된 형식에 대해 'c','d'가 몇 개 들어 있는지 확인
        int numCount = totalOccurrence(format,'c');
        int charCount = totalOccurrence(format,'d');

        // 전체 경우의 수 계산
        for (int c = 1; c <= (int) Math.pow(26,numCount); c++) {
            for (int d = 1; d <= (int) Math.pow(10,charCount); d++) {
                count++;
            }
        }

        // 예외 처리

        return count;
    }

    public static int totalOccurrence(String format, char target){
        int count = 0;
        for (char ch : format.toCharArray()){
            if (ch == target){
                count++;
            }
        }
        return count;
    }
}
