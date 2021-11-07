// https://www.udemy.com/course/java-the-complete-java-developer-course/learn/quiz/4426610#overview
public class Main {
    
    public static void main(String[] args) {
        
        testMethodIsLeapYear(1700, false);
        testMethodIsLeapYear(2600, false);
        testMethodIsLeapYear(-1600, false);
        testMethodIsLeapYear(1600, true);
        testMethodIsLeapYear(2017, false);
        testMethodIsLeapYear(2000, true);




    }

    public static void testMethodIsLeapYear(int year, boolean expectedAnswer) {
        // test results with expected value of leap year
        System.out.println(expectedAnswer == isLeapYear(year)); 
    }

    public static boolean isLeapYear(int year) {
        boolean output = false;

        if (year >= 1 && year <= 9999) {
            if (year % 4 == 0) {
                if (year % 100 == 0) {
                    if (year % 400 == 0) {
                        output = true;    
                    }
                } else {
                    output = true;
                }
            }
        }

        return output;
    }
    
}