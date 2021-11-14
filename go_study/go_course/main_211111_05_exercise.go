// go run main.go

// exercice
package main

import "fmt"

// package level scope
var x int = 42
var y string = "James Bond"
var z bool = true

func main() {

	s := fmt.Sprintf("%v %v %v\n", x, y, z)

	fmt.Println(s)

}
