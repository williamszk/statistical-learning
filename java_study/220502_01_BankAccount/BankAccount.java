public class BankAccount {
    private long accountNumber;
    // maybe we should use long here, and use the last two digits as cents
    private double balance;
    private String customerName;
    private String email;
    private String phoneNumber;

    // this is a constructor
    public BankAccount() {
        this(11111, 1.00, "Default Client", "default@bank.com", "0000-0000");
        // we use the key word this, because it refers to the class
        // we need to pass the arguments in the correct order for the constructor
        // to know which method we are using.

        // In python we have the concept of instance attributes and 
        // class attributes, in Java do we have the same?

        // When using "this" in the construcutor, we need to pass as 
        // the first line of the constructor.
        
        System.out.println("Empty Constructor called!");
        // we can pass a constructor inside another constructor
        // for example, if we pass the empty constructor
        // we can use the other constructor to build a default client        
    }
    // a constructure is like the __init__ from python
    // we can pass initial arguments that will be fields (attributes)
    // of the instance
    // notice that we do not include the type to be returned
    // a constructor is a method?

    // this is method overloading, we just change the parameters passed
    // and Java will know which method we are calling
    public BankAccount(long accountNumber, double balance, String customerName,
                        String email, String phoneNumber){
        this.accountNumber = accountNumber;
        this.balance = balance;
        this.customerName = customerName;
        this.email = email;
        this.phoneNumber = phoneNumber;
    }

    public long getAccountNumber() {
        return this.accountNumber;
    }

    public double getBalance() {
        return this.balance;
    }

    public String getCustomerName(){
        return this.customerName;
    }

    public String getEmail() {
        return this.email;
    }

    public String getPhoneNumber() {
        return phoneNumber;
    }

    public void setAccountNumber(long accountNumber) {
        this.accountNumber = accountNumber;
    }

    public void setBalance(double balance) {
        this.balance = balance;
    }

    public void setCustomerName(String customerName ){
        this.customerName = customerName;
    }

    public void setEmail(String email){
        this.email = email;
    }

    public void setPhoneNumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }

    public void depositFunds(double depositAmount) {
        this.balance += depositAmount;
    }

    public void withdrawFunds(double withdrawAmount) {
        if (this.balance < withdrawAmount) {
            System.out.println(
                "There is not enough funds to withdraw. Operation cancelled.");
        } else {
            this.balance -= withdrawAmount;
        }
    }
}
