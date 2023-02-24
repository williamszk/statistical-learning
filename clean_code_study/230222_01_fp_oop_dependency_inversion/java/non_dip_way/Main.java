class Main {
    public static void main(String[] args) {
        App.start();
    }
}

class App {
    public static void start(){
        HttpClient.getUser("bob@clean.com");
        User user = new User("Bob", "bob@clean.com");
        HttpClient.createUser(user);
    }
}

class HttpClient {
    public static void getUser(String email){
        System.out.println("Getting user... " + email);
    };

    public static void createUser(User user){
        System.out.println("Creating user... " + user.name);
    };
}

class User{
    public String name;
    public String email;

    public User(String name, String email){
        this.name = name;
        this.email = email;
    }
}


