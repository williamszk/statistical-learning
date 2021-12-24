// https://www.youtube.com/watch?v=v6HnDiPyynA&list=PLCKpcjBB_VlBsxJ9IseNxFllf-UFEXOdg&index=47&ab_channel=AprendaGo

package main

import "fmt"

var x interface{} // not type specified

func main() {
	x = true
	// what to do when we don't know the type of the variable?
	switch x.(type) {
	case int:
		fmt.Println("x is int")
	case bool:
		fmt.Println("x is bool")
	case string:
		fmt.Println("x is string")
	case float64:
		fmt.Println("x is float64")
	}
	// this is called type switch
}

//
