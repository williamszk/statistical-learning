public class Main{
    public static void main(String[] args) {

        System.out.println("RedheadDuck duck01 ------");
        RedheadDuck duck01 = new RedheadDuck();
        duck01.fly();
        duck01.quack();

        System.out.println("MallardDuck duck02 ------");
        MallardDuck duck02 = new MallardDuck();
        duck02.fly();
        duck02.quack();

        System.out.println("RubberDuck duck03 ------");
        RubberDuck duck03 = new RubberDuck();
        duck03.fly();
        duck03.quack();
        // The RubberDuck shouldn't be able to fly, and it should squeak instead
        // of quack.

        System.out.println("DecoyDuck duck03 ------");
        DecoyDuck duck04 = new DecoyDuck();
        duck04.fly();
        duck04.quack();
        // The DecoyDuck shouldn't be able to fly nor quack
    }
}

class Duck{

    public Duck(){}

    public static void quack(){
        System.out.println("Quack!");
    }

    public static void fly(){
        System.out.println("Fly!");
    }
}

class RedheadDuck extends Duck {
    public RedheadDuck(){
    }
}

class MallardDuck extends Duck {
    public MallardDuck(){
    }
}

class RubberDuck extends Duck {
    public RubberDuck(){
    }
}

class DecoyDuck extends Duck {
    public DecoyDuck(){
    }
}