// https://www.youtube.com/watch?v=w_JW1bWT08s&list=PLCKpcjBB_VlBsxJ9IseNxFllf-UFEXOdg&index=50&ab_channel=AprendaGo

package main

import "fmt"

func main() {

	for i := 65; i <= 91; i++ {
		fmt.Printf("%#U\n", i)
	}

}
