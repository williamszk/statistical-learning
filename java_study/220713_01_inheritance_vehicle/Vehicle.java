public class Vehicle {

    private int speed;
    private int angle;
    private int gear;

    public Vehicle() {
        this(0, 0, 0);
    }

    public Vehicle(int speed, int angle, int gear) {
        this.angle = angle;
        this.gear = gear;
    }

    public void steerWheel(int intensity) {
        if (intensity < 0) {
            System.out.println("Steer wheel to the left");
        } else {
            System.out.println("Steer wheel to the right");
        }
        this.angle += intensity;
    }

    /* The possible values of gear are 0 .. 6, included
     * where 0 means that there is no gear
     */
    public void changeGear(int gear) {
        if (gear < 0 || gear > 6) {
            System.out.println("The vehicle cannot change gear to: " + gear);
        } else {
            System.out.println("Gear changed to: " + gear);
            this.gear = gear;
        }
    }

    public void move(int speed) {
        System.out.println("The vehicle is moving with speed: " + speed);
    }

}
