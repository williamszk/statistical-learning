public class ByteShortIntLong {
    
    public static void main(String[] args){
        System.out.println("Hello world!");

        int myMinIntValue = Integer.MIN_VALUE;
        int myMaxIntValeu = Integer.MAX_VALUE;

        System.out.println("Integer min value = " + myMinIntValue);
        System.out.println("Integer max value = " + myMaxIntValeu);

        // add +1 to the maximum value of int
        int plusOneIntMaxValue = myMaxIntValeu + 1;
        System.out.println("+1 the max value of int = " + plusOneIntMaxValue);
        // this is called overflow

        // subtract -1 to the minimum value of int
        int minusOneIntMinValue = myMinIntValue - 1;
        System.out.println("-1 the min value of int = " + minusOneIntMinValue);
        // this is called underflow 

        int myMaxInt = 2_147_483_647;
        

        
    }
}
