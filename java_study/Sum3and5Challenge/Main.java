public class Main {
    public static void main(String[] args) {
        int sum3and5 = 0;
        int currNum = 0;
        int numChecks = 0;
        for (int i = 1; i <= 1000; i++){
            currNum = i;
            if (currNum % 3 == 0 && currNum % 5 == 0) {
                sum3and5 += currNum;
                System.out.println(currNum);
                ++numChecks;
            }
            
            if (numChecks == 5) {
                break;
            }
        }

        System.out.println("Total sum: " + sum3and5);

    }
}
