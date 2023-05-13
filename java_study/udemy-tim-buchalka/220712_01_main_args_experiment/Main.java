/**
 * This is a simple program to experiment with arguments that we pass to the java class 
 * artifact.
*/
class Main {
    public static void main(String[] args) {
        int i;
        for (i = 0; i < args.length; i++) {
            System.out.println(args[i]);
        }
    }
}

// This is the output
// C:\Users\william.suzuki\Documents\statistical-learning\java_study\220712_01_main_args_experiment>java Main 1 2 3 f d g 
// 1
// 2
// 3
// f
// d
// g