package FastCampus._2.Array;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class 백준_2751 {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

        // 수의 개수 N 입력
        int N = Integer.parseInt(reader.readLine());

        // 수를 저장할 배열 선언 및 입력
        int[] numbers = new int[N];
        for (int i = 0; i < N; i++) {
            numbers[i] = Integer.parseInt(reader.readLine());
        }

        // 배열 정렬
        Arrays.sort(numbers);

        // 정렬된 결과 출력
        for (int i = 0; i < N; i++) {
            writer.write(Integer.toString(numbers[i]) + "\n");
        }

        // BufferedWriter의 경우, 모든 작업을 마친 후에는 반드시 flush()와 close()를 호출해주어야 합니다.
        writer.flush();
        writer.close();
        reader.close();
    }
}

