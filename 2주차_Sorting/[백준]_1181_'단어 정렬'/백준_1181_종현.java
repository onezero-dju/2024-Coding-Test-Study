package FastCampus.Sort;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class 백준_1181 {
    public static void main(String[] args) {
        // 1. 값 입력 받기
        Scanner scan = new Scanner(System.in);
        int N = scan.nextInt();
        scan.nextLine();
        String[] strCompareArray = new String[N];
        for (int i = 0; i < strCompareArray.length; i++) {
            strCompareArray[i] = scan.nextLine();
        }

        // 2. 중복된 문자열 제거 : Set API 사용
        Set<String> delDupArray = new HashSet<>(Arrays.asList(strCompareArray));

        // 3. 배열 안의 문자열 나열 : 길이가 짧은 순, 길이가 같으면 사전순
        String[] sortedArray = delDupArray.toArray(new String[0]);
        Arrays.sort(sortedArray, (s1, s2) -> {
            int result = Integer.compare(s1.length(), s2.length());
            if (result == 0) {
                return s1.compareTo(s2);
            }
            return result;
        });

        // 4. 출력
        for (String str : sortedArray){
            System.out.println(str);
        }

        // Scanner 닫기
        scan.close();
    }
}
