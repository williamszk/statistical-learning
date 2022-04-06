public class Main {
	public static void main(String[] args) {
		System.out.println(sumDigits(3453));
		System.out.println(sumDigits(23));
	}

	public static int sumDigits(int number) {
		if (number >= 10) {
			int totalSumChars = 0;
			String numStr = Integer.toString(number);
			for (int i = 0; i < numStr.length(); i++){
				totalSumChars += Character.getNumericValue(numStr.charAt(i)) ;
			}
			return totalSumChars;
		} else {
			return -1;
		}
	}
}
