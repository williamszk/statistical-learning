// go run main.go

// exercice
package main

import "fmt"

type MyPersonalType int

var x MyPersonalType

func main() {
	fmt.Println(x)

	fmt.Printf("%T\n", x)

	x = 42

	fmt.Println(x)

}
