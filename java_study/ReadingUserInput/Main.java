import java.util.Scanner;
// https://www.udemy.com/course/java-the-complete-java-developer-course/learn/lecture/10629304#overview
// https://www.udemy.com/course/java-the-complete-java-developer-course/learn/lecture/10629306#overview

public class Main {
	public static void main(String[] args) {
		Scanner scanner = new  Scanner(System.in);
		System.out.println("Enter your year of birth:");
		// We need to check if the input is integer
		boolean hasNextInt = scanner.hasNextInt();
		if (hasNextInt) {
			int yearOfBirth = scanner.nextInt();
			// this next line is needed because the next nextLine will think that enter
			// is the character being entered
			scanner.nextLine();
	
			System.out.println("Enter your name:");
			String name = scanner.nextLine();
			
			int age = 2022 - yearOfBirth;
	
			if (age >= 0 && age <= 100) {
				System.out.println("Hello, " + name + ". You are " + age + " years old.");
			} else {
				System.out.println("Invalid year of birth.");
			}
		} else {
			System.out.println("Unable to parse year of birth.");
		}
		scanner.close();
	}
}
