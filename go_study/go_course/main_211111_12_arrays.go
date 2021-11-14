// go run main.go

package main

import "fmt"

func main() {
	fmt.Println("Hello World!")

	primes := [6]int{2, 3, 5, 7, 11}

	fmt.Println(primes)

	for _, item := range primes {
		fmt.Println(item)
	}

}
