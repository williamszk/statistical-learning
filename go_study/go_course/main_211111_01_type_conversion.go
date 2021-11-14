// go run main.go
package main

import "fmt"

type hotdog int

var b hotdog = 22

func main() {
	x := 10
	fmt.Printf("%v\n", b)
	fmt.Println(x)
	fmt.Println("Hello, World!")
	// b = x
	x = int(b) // type conversion, type casting, type coercion
	// in go we have just type conversion
	// we need to pass int() here to transform b into an int
	fmt.Printf("%T\n", b)
	fmt.Printf("%T\n", x)
}
