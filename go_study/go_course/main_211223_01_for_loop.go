// https://www.youtube.com/watch?v=eGdB8FMCZ0s&list=PLCKpcjBB_VlBsxJ9IseNxFllf-UFEXOdg&index=42&ab_channel=AprendaGo

package main

import "fmt"

func main() {

	// for i := 0; i < 20; i++ {
	// 	// print if even
	// 	if i%2 == 0 {
	// 		fmt.Println(i)
	// 	}
	// }

	for i := 0; i < 20; i++ {
		if i%2 != 0 { // this is odd number
			continue // go back to the start of the loop
		}
		fmt.Println(i)

	}

}
