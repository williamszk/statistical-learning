public class Main {
    public static void main(String[] args) {
        Player player = new Player();

        player.name = "Tim";
        player.health = 20;
        player.weapon = "Sword";

        int damage = 10;
        player.loseHealth(damage);
        System.out.println("Remaining health = " + player.healthRemaining());

        damage = 11;
        player.loseHealth(damage);
        System.out.println("Remaining health = " + player.healthRemaining());


        EnhancedPlayer player2 = new EnhancedPlayer("Tim", "Sword", 50);
        System.out.println("Initial health is: "+player2.getHealth());
    }
}

// Take a look at:
// https://youtu.be/Qgl81fPcLc8?t=641
