public class BankAccount {
    private String accountNumber;
    private double balance;
    private String customerName;
    private String customerEmailAddress;
    private String customerPhoneNumber;

    public BankAccount() {
        this("56789", 2.50, "Default name", "Default address", "Default phone");
    }

    // this is called the constructor
    public BankAccount(String accountNumber, double balance, String customerName, String customerEmailAddress,
            String customerPhoneNumber) {
        System.out.println("Account constructor with paramters called");
        this.accountNumber = accountNumber;
        this.balance = balance;
        this.customerName = customerName;
        this.customerEmailAddress = customerEmailAddress;
        this.customerPhoneNumber = customerPhoneNumber;
    }

    // implement a constructor where accountNumber and balance are default values,
    // but the rest are given
    // by the user
    public BankAccount(String customerName, String customerEmailAddress, String customerPhoneNumber) {
        this("56789", 2.50, customerName, customerEmailAddress, customerPhoneNumber);
    }
    // we can create many constructors, and method overload will take place
    // Java will call the method that matches the pattern of arguments that are given

    public void setAccountNumber(String accountNumber) {
        this.accountNumber = accountNumber;
    }

    public void setBalance(double balance) {
        this.balance = balance;
    }

    public void setCustomerName(String customerName) {
        this.customerName = customerName;
    }

    public void setCustomerEmailAddress(String customerEmailAddress) {
        this.customerEmailAddress = customerEmailAddress;
    }

    public void setCustomerPhoneNumber(String customerPhoneNumber) {
        this.customerPhoneNumber = customerPhoneNumber;
    }

    public String getAccountNumber() {
        return this.accountNumber;
    }

    public double getBalance() {
        return this.balance;
    }

    public String getCustomerName() {
        return this.customerName;
    }

    public String getCustomerEmailAddress() {
        return this.customerEmailAddress;
    }

    public String getCustomerPhoneNumber() {
        return this.customerPhoneNumber;
    }
}
