// https://practice.geeksforgeeks.org/comments/drive-the-car2541/1/?rel=https://practice.geeksforgeeks.org/problems/drive-the-car2541/1/
public class Main {
	public static void main(String[] args) {

		
		long N;
		long K;
		long [] arr;
		long outExp;

		N = 5;
		K = 7;
		arr = new long[] {2, 5, 4, 5, 2};
		outExp = -1;

		System.out.println(required(arr, N, K) == outExp);

		N = 5;
		K = 4;
		arr = new long[] {1, 6, 3, 5, 2};
		outExp = 2;

		System.out.println(required(arr, N, K) == outExp);

	}

	public static long required(long arr[], long N, long K){
		long max = 0;
		for (int i = 0; i < N; i++){
			if (arr[i] > max) {
				max = arr[i];
			}
		}
		return K >= max ? -1 : max - K;
	}

}
