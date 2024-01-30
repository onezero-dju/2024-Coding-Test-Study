//package 2주차_Sorting.[백준]_2750_'수 정렬하기';
// 개념을 자바코드로 바로 작성하는데서 시간이 10분넘게 들었다
// 자바언어를 평소 적게 사용해서 자바에 대한 지식과 숙련도가 부족하다고 생각이 된다.
// 다 풀고 다른 사람의 풀이를 보니 자바에 있는 특정 함수를 이용하는 것을 보고 쉽게 풀는 방법을 알게 되었다.

import java.util.*;
public class BJ_2750_성우 {
    public static void main(String[] args) {
		
		Scanner nu = new Scanner(System.in);
		
		int N = nu.nextInt();					
		int[] num = new int[N];
		
		for (int i = 0; i < N; i++) {
			num[i] = nu.nextInt();
		}
		
		for (int i = 0; i < N - 1; i++) {			
			int temp = 0;						
			for (int j = i + 1; j < N; j++) {	 // 정렬 과정	
				if (num[j] > num[i]) {							
					temp = num[j];		// temp(임시) 변수에 num[j]에 미리 값을 넣는다.
					num[j] = num[i];	//  num[i]값을 num[j] 값을 넣는다 
					num[i] = temp;      //  맨처음 담은 temp(임시)변수의 값을 num[i] 넣어서 자리교환이 된다.
				}
			}
		}
		
		for (int i = 0; i < N; i++) {
			System.out.println(num[i]);
		}
	}
}