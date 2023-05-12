public class Main {
    public static void main(String[] args) {
       Wall awall = new Wall();

       System.out.println(awall.getHeight());
       System.out.println(awall.getWidth());


       Wall wall01 = new Wall(5,4);
       System.out.println("area = " + wall01.getArea());

       wall01.setHeight(-1);

       System.out.println("width = " + wall01.getWidth());
       System.out.println("height = " + wall01.getHeight());
       System.out.println("Area = " + wall01.getArea());
    }
}