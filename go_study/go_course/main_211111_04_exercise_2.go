// go run main.go
// https://www.youtube.com/watch?v=Q7ZrIDMj9zc&list=PLCKpcjBB_VlBsxJ9IseNxFllf-UFEXOdg&index=17&ab_channel=AprendaGo
// exercice
package main

import "fmt"

// package level scope
var x int
var y string
var z bool

func main() {
	fmt.Println(x, "\n", y, "\n", z)
}

// we can see that the compiler give some default values for the declared variables
