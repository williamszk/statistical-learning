// https://www.youtube.com/watch?v=bWvpNLBSEKk&list=PLCKpcjBB_VlBsxJ9IseNxFllf-UFEXOdg&index=52&ab_channel=AprendaGo

package main

import "fmt"

func main() {

	year := 1993

	for { // infinite loop

		fmt.Println(year)
		year++
		if year == 2021 {
			break
		}

	}
}
