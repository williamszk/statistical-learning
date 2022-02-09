import javax.swing.plaf.synth.SynthSeparatorUI;

public class Main {
	public static void main(String[] args) {
		int value = 3;
		if (value == 1) {
			System.out.println("Value was 1");
		} else if (value == 2) {
			System.out.println("Value was 2");
		} else {
			System.out.println("Was not 1 nor 2");
		}

		int switchValue = 1;

		switch (switchValue) {
			case 1:
				System.out.println("Value was 1");
				break;
			case 2:
				System.out.println("Value was 2");
				break;
			case 3:
			case 4:
			case 5:
				System.out.println("Was a 3 or 4 or 5.");
				System.out.println("Actually it was a " + switchValue);
			default:
				System.out.println("Value was not 1 nor 2");
				break;
		}

		/* Switch can be used with byte, short char and int also with String */

		char myValueChar = 'A';

		switch (myValueChar) {
			case 'A':
				System.out.println("The value was A");
				break;
			case 'B':
				System.out.println("The value was B");
				break;
			case 'C':
				System.out.println("The value was C");
				break;
			case 'D':
				System.out.println("The value was D");
				break;
			case 'E':
				System.out.println("The value was E");
				break;
			default:
				System.out.println("It was not found " + myValueChar);
				break;
		}

		String month = "January";

		switch (month.toLowerCase()) {
			case "january":
				System.out.println("Jan");
				break;
			case "february":
				System.out.println("Feb");
				break;
			default:
				System.out.println("Not sure.");
				break;
		}
	}
}
