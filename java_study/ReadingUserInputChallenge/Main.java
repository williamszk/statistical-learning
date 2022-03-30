import java.util.Scanner;

// https://www.udemy.com/course/java-the-complete-java-developer-course/learn/lecture/10641374#overview

public class Main {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		boolean hasNextInt;
		int counter = 1;
		int totalSum = 0;
		while (counter <= 10) {
			System.out.println("Enter number #" + counter);
			hasNextInt = scanner.hasNextInt();
			if (hasNextInt) {
				int inputedNum = scanner.nextInt();
				totalSum += inputedNum;
				counter += 1;
			} else {
				System.out.println("Invalid input. Try again.");
				scanner.nextLine();
			}

		}

		scanner.close();

		System.out.println("The total is " + totalSum);

	}
}
