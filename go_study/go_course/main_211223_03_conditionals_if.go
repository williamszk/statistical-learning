// https://www.youtube.com/watch?v=LBlrrV0iRKg&list=PLCKpcjBB_VlBsxJ9IseNxFllf-UFEXOdg&index=44&ab_channel=AprendaGo

package main

import "fmt"

func main() {

	x := 10

	if x < 100 {
		fmt.Println("Hello World!")
	}

	if !(x < 100) {
		fmt.Println("Hello World! with parenthesis and negation example")
	}

	// test truthy and falsy values
	// if 1 {
	// 	fmt.Println("Testing truthy values...")
	// }
	// doesn't work

	if x := 100; x < 110 {
		fmt.Println("Another thing that we can do in if is to include an initialization")
	}

	// https://www.youtube.com/watch?v=ZfCgoVaxMGE&list=PLCKpcjBB_VlBsxJ9IseNxFllf-UFEXOdg&index=45&ab_channel=AprendaGo
	// else if and else

	if x := 1000; x > 100 {
		fmt.Println("x is bigger than 100")
	} else {
		fmt.Println("x is not bigger than 100")
	}

}
