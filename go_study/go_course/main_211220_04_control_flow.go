// https://www.youtube.com/watch?v=1G-tbQ6UE_A&list=PLCKpcjBB_VlBsxJ9IseNxFllf-UFEXOdg&index=38&ab_channel=AprendaGo
// https://www.youtube.com/watch?v=g_Qdxi1b2cE&list=PLCKpcjBB_VlBsxJ9IseNxFllf-UFEXOdg&index=39&ab_channel=AprendaGo
// https://www.youtube.com/watch?v=EL9wo6Zrz9o&list=PLCKpcjBB_VlBsxJ9IseNxFllf-UFEXOdg&index=40&ab_channel=AprendaGo

// control flow

package main

import "fmt"

func main() {
	// an example of loop in Go
	// there is while in Go, just for
	for x := 0; x < 10; x++ {
		fmt.Println("The loop: ", x)
	}

	for hour := 0; hour <= 12; hour++ {
		for x := 0; x < 60; x++ {
			fmt.Printf("%vh %vmin\n", hour, x)
		}
	}

}
