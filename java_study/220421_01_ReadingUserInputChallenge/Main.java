
// https://www.udemy.com/course/java-the-complete-java-developer-course/learn/lecture/10641374?start=15#overview
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		int totalSum = 0;
		Scanner scanner = new Scanner(System.in);
		int includedNums = 0;
		while (includedNums <= 9) {
			System.out.println("Enter a number #" + (includedNums + 1) + ": ");
			boolean isAnInt = scanner.hasNextInt();
			if (isAnInt) {
				int numberEntered = scanner.nextInt();
				totalSum += numberEntered;
				includedNums++;
			} else {
				System.out.println("Invalid Number.");
			}
			scanner.nextLine(); // handle end of line (enter key)
			// the nextLine() will remove the content of the input
			// without this nextLine the loop will run infinitely
		}
		System.out.println("The total sum is: " + totalSum);

		scanner.close();
	}
}

// to run the .class file
// do not include .class at the end
// just use: java Main
// instead of: java Main.class