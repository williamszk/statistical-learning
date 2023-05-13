// https://www.udemy.com/course/java-the-complete-java-developer-course/learn/lecture/3133200#overview

public class Main {

    public static void main(String[] args) {
        BankAccount timsAccount = new BankAccount("Tim", "tim@email.com", "12345");
        System.out.println(timsAccount.getAccountNumber());
        System.out.println(timsAccount.getCustomerName());


        VipCustomer avipCustomer = new VipCustomer();
        System.out.println(avipCustomer.getCustomerName());
        System.out.println(avipCustomer.getCreditLimit());
    }
}
