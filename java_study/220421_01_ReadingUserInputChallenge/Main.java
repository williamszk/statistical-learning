import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		int totalSum = 0;
		Scanner scanner = new Scanner(System.in);
		for (int i = 0; i < 10; i++) {
			System.out.println("Enter a number: ");
			int numberEntened = scanner.nextInt();
			System.out.println("The value entered is: " + numberEntened);
		}

		scanner.close();
	}
}
