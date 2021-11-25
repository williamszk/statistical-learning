pub fn run(){
  let name = "William";
  let mut age = 40;

  println!("My name is {}! And I am {} years old.", name, age);

  age = 50;

  println!("My name is {}! And I am {} years old.", name, age);

  // Define const
  const ID:i32 = 001;
  println!("ID: {}",ID);

  // Assign mutliple vars
  let ( my_name, my_age ) = ("Brad","37");
  println!("{} is {}", my_name, my_age);

}