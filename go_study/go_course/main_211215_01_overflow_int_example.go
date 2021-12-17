// https://www.youtube.com/watch?v=g0j0XaVk2EI&list=PLCKpcjBB_VlBsxJ9IseNxFllf-UFEXOdg&index=25&ab_channel=AprendaGo

package main

import "fmt"

func main() {
	fmt.Println("Hello World!")
	var x uint16 = 65535
	// the max value for an uint16 is 65535
	// when we sum 2 the limit is overflow and the number goes back and start from 0
	// an example of overflow...
	fmt.Println(x)
	x += 2
	fmt.Println(x)
}
