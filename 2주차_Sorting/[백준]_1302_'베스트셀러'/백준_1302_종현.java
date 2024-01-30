package FastCampus._2.Array;

import java.io.*;
import java.util.HashMap;
import java.util.Map;

public class 백준_1302 {
    public static void main(String[] args) throws IOException {
        // 1. 값 입력 받기
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(reader.readLine());

        // 각 키워드에 count 매겨야 하니까 Map API 사용
        Map<String, Integer> salesMap = new HashMap<>();

        // 2. 입력 받은 책 이름별로 count : 같은 count -> 사전 순으로 가장 앞 책 제목 선택
        int maxSalesCount = 0;
        String bestSeller = "";

        for (int i = 0; i < N; i++) {
            String title = reader.readLine();

            // key(=title)에 대한 value(=count) 값 증가
            // salesCount = value
            int salesCount = salesMap.getOrDefault(title, 0) + 1;

            salesMap.put(title, salesCount);

            if (salesCount > maxSalesCount || (salesCount == maxSalesCount && title.compareTo(bestSeller) < 0)){
                maxSalesCount = salesCount;
                bestSeller = title;
            }

        }

        // 3. 출력
        writer.write(bestSeller);

        writer.flush();
        writer.close();
        reader.close();
    }
}
