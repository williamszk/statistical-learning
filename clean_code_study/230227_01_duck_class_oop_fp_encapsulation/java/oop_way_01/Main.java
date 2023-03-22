public class Main{
    public static void main(String[] args) {

        System.out.println("RedheadDuck duck01 ------");
        RedheadDuck duck01 = new RedheadDuck();
        duck01.fly();
        duck01.quack();

        // System.out.println("MallardDuck duck02 ------");
        // MallardDuck duck02 = new MallardDuck();
        // duck02.fly();
        // duck02.quack();

        // System.out.println("RubberDuck duck03 ------");
        // RubberDuck duck03 = new RubberDuck();
        // duck03.fly();
        // duck03.quack();
        // // The RubberDuck shouldn't be able to fly, and it should squeak instead
        // // of quack.

        System.out.println("DecoyDuck duck04 ------");
        DecoyDuck duck04 = new DecoyDuck();
        duck04.fly();
        duck04.quack();
        // The DecoyDuck shouldn't be able to fly nor quack
    }
}

// Implement the Interfaces (abstract classes)
interface FlyBehavior {
    public void fly();
}

interface QuackBehavior {
    public void quack();
}

// Implement the concrete classes
class Fly implements FlyBehavior {
    public void fly(){
        System.out.println("Fly!");
    }
}

class NoFly implements FlyBehavior {
    public void fly(){
        System.out.println("No fly!");
    }
}

class Quack implements QuackBehavior {
    public void quack(){
        System.out.println("Quack!");
    }
}

class NoQuack implements QuackBehavior {
    public void quack(){
        System.out.println("No quack!");
    }
}


class Squeak implements QuackBehavior {
    public void quack(){
        System.out.println("Squeak!");
    }
}


class Duck{
    private FlyBehavior flyBehavior;
    private QuackBehavior quackBehavior;
    // FlyBehavior flyBehavior, QuackBehavior quackBehavior
    public Duck(){
    }

    public void setFlyBehavior(FlyBehavior flyBehavior){
        this.flyBehavior = flyBehavior;
    }

    public void setQuackBehavior(QuackBehavior quackBehavior){
        this.quackBehavior = quackBehavior;
    }

    public void fly(){
        this.flyBehavior.fly();
    }

    public void quack(){
        this.quackBehavior.quack();
    }
}

class RedheadDuck extends Duck {
    public RedheadDuck(){
        super();
        this.setFlyBehavior(new Fly());
        this.setQuackBehavior(new Quack());
    }
}

// class MallardDuck extends Duck {
//     public MallardDuck(){
//     }
// }

// class RubberDuck extends Duck {
//     public RubberDuck(){
//     }
// }

class DecoyDuck extends Duck {
    public DecoyDuck(){
        super();
        this.setFlyBehavior(new NoFly());
        this.setQuackBehavior(new NoQuack());
    }
}