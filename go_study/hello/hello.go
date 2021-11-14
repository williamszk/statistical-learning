package main

import "fmt"

func main() {
	fmt.Println("Hello, World!")
	fmt.Println("This is another test.")

	foo()

	for i := 0; i < 3; i++ {
		if i%2 == 0 {
			fmt.Println("This is a loop.")
		}
	}

	bar()

	// an example of how to use spread in go
	fmt.Println("This", true, 10, false, 109.99)

	// an example of how to capture the output from a fmt.Println function
	n, err := fmt.Println("A")

	fmt.Println(n) // number of bytes used in the tring
	fmt.Println(err)
}

func foo() {
	fmt.Println("I am a foo.")
}

func bar() {
	fmt.Println("This is a bar.")
}

// control flow
// 1. sequencial
// 2. loop
// 3. conditional
