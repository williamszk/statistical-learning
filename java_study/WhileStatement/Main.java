public class Main {
	public static void main(String[] args) {

		int count = 0;
		while (count != 5) {
			System.out.println("Count value is " + count);
			count++;
		}

		count = 1;
		while (true) {
			if (count == 6) {
				break;
			}
			System.out.println("Coutn value is " + count);
			count++;
		}

		for (int i = 6; i != 6; i++){
			System.out.println(i);
		}

		count = 1;
		do {
			System.out.println(count);
			count++;
		} while(count != 6);


	}
}
