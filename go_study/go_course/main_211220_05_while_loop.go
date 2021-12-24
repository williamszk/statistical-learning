//
// https://www.youtube.com/watch?v=QDaiqhTq3TA&list=PLCKpcjBB_VlBsxJ9IseNxFllf-UFEXOdg&index=41&ab_channel=AprendaGo

package main

import "fmt"

func main() {

	x := 0

	for x < 10 {
		fmt.Println(x)
		x++
	}

	y := 0
	for { // this is a way to set an infinite loop
		fmt.Print("Halo\n")
		if y < 10 {
			y++
		} else {
			break // we need to include a break so that the loop stops
		}
	}

}

// next class
