// https://www.youtube.com/watch?v=Y5HamAGQzUg&list=PLCKpcjBB_VlBsxJ9IseNxFllf-UFEXOdg&index=48&ab_channel=AprendaGo

package main

import "fmt"

func main() {
	x := 2

	if x == 2 || x == 3 {
		fmt.Println("x is 2 or 3")
	}

	if x > 0 && x < 10 {
		fmt.Println("x is between 0 and 10")
	}

	x = 19

	if !(x%2 == 0) && (x > 10) {
		fmt.Println("x is not even and it larger than 10")

	}

}

// next exericise
// https://www.youtube.com/watch?v=xXUTHJzJNgM&list=PLCKpcjBB_VlBsxJ9IseNxFllf-UFEXOdg&index=49&ab_channel=AprendaGo
