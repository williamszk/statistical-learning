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
		long extraFuel = 0;
		for (int i = 0; i < N; i++){
			if (arr[i] > K) {
				long diffFuel = arr[i] - K;
				if (diffFuel > extraFuel) {
					extraFuel = diffFuel;
				}
			}
		}

		if (extraFuel == 0){
			return -1;
		} else {
			return extraFuel;
		}
	}
}

// to compile in windows
// javac Main.java
// to run in windows
// java Main