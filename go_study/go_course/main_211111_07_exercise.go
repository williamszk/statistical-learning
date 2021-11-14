// go run main.go

// exercice
package main

import "fmt"

type MyPersonalType int

var x MyPersonalType

var y int

func main() {
	fmt.Println(x)

	fmt.Printf("%T\n", x)

	x = 42

	fmt.Println(x)
	fmt.Printf("%T\n", x)

	y = int(x)

	fmt.Printf("%v, %T\n", y, y)
}
