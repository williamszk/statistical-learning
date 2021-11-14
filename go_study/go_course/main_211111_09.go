// go run main.go

// exercice
package main

import "fmt"

var x bool

func main() {
	fmt.Println("Hello World!")
	x = true
	fmt.Println(x)
	x = (10 < 9)
	fmt.Println(x)
}
