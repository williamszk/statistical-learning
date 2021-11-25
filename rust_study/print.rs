pub fn run(){
  // Print to console
  println!("Hello from the print.rs file.");

  println!("Number: {}",1);

  // Basic formatting
  println!("{} is from {}","Brad","Massachusets");

  // Positional arguments
  println!("{0} is from {1} and {0} likes to {2}.",
      "Brad", "Mass","code"
  );

  // Named arguments
  println!(
      "{name} likes to play {acitivity}.",
      name = "John",
      acitivity = "Baseball"
  );

  // Placeholder traits
  println!("Binary: {:b} Hex: {:x} Octal: {:o}", 10,10,10);

  // Placeholder for debug trait
  println!("{:?}",
      (12, true, "hello")
  );
  
  // Basic Math
  println!("10 + 10 = {}",20);

}