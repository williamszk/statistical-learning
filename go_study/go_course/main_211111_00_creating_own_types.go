// go run main.go
package main

import "fmt"

// in go variable types are immutable

type hotdog int

var b hotdog

func main() {
	fmt.Printf("%T", b)
}
