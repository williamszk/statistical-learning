public class Main {

    public static void main(String[] args) {
        boolean gameOver = true;
        int score = 5000;
        int levelCompleted = 5;
        int bonus = 100;

        if (score > 1000 && score < 5000) {
            System.out.println("Your score was less than 5000 and more than 1000.");
        } else if (score < 1000) {
            System.out.println("Your score was less than 1000.");
        } else {
            System.out.println("Your score was more than or equal to 5000.");
        }

        if (gameOver) {
            int finalScore = score + (levelCompleted * bonus);
            // finalScore is a local variable to this code block
            // this is not seem outside of the code block
            // this variable is deleted after the execution of this code
            System.out.println("Your final score was: " + finalScore);
        }


        // here we are reassign value to variables
        // this wouldn't exist in functional languages
        // in functional style there is no reassignment of variables
        // those are examples of imperative programming, where we are
        // changing the state of the memory
        score = 10000;
        levelCompleted = 8;
        bonus = 200;
        if (gameOver) {
            int finalScore = calculateFinalScore(score, levelCompleted, bonus);
            System.out.println("Your final score was: " + finalScore);
        }

//        if ("true") {
//            System.out.println("Test for truthy values.");
//        }

        int playerScore = 1500;
        int position = calculateHighScorePosition(playerScore);
        displayHighScorePosition("Alice", position);

        playerScore = 900;
        position = calculateHighScorePosition(playerScore);
        displayHighScorePosition("Bob", position);

        playerScore = 400;
        position = calculateHighScorePosition(playerScore);
        displayHighScorePosition("Daniel", position);

        playerScore = 50;
        position = calculateHighScorePosition(playerScore);
        displayHighScorePosition("Rebecca", position);

    }

    public static void displayHighScorePosition(String playerName, int position) {
        System.out.println(playerName + " managed to get into position " +
                position + " on the high score table.");
    }

    public static int calculateHighScorePosition(int playerScore) {
        int position;

        if (playerScore >= 1000) {
            position = 1;
        } else if (playerScore >= 500) {
            position = 2;
        } else if (playerScore >= 100) {
            position = 3;
        } else {
            position = 4;
        }
        return position;
    }

    public static int calculateFinalScore(int score, int levelCompleted, int bonus) {
        int finalScore = score + (levelCompleted * bonus);
        return finalScore;
    }
    // we can't create a method inside another method
    // so we can't create a method inside the main method
    // I think that in Python we can create a function inside another function
    // to create decorators we do this, this is called higher order functions
    public static void myMethod() {
        System.out.println("My method...");
    }

}
