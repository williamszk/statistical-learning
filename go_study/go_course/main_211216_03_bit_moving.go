// https://www.youtube.com/watch?v=USntMXkOihY&list=PLCKpcjBB_VlBsxJ9IseNxFllf-UFEXOdg&index=30&ab_channel=AprendaGo
// we can change the position of bits
// bit wise operation

package main

import "fmt"

func main() {

	myFirstBit := 1
	mySecondBit := myFirstBit << 1
	myThirdBit := mySecondBit << 1
	fmt.Printf("%b, %b, %b\n", myFirstBit, mySecondBit, myThirdBit)

	myNumber := 1
	myAnotherNumber := myNumber << 10

	fmt.Printf("%b, %b\n", myNumber, myAnotherNumber)
	fmt.Printf("%v, %v\n", myNumber, myAnotherNumber)

}

// example of moving bits
// 0110000
// 0011000
// 0001100
// 0000110
// 0000011

// I know that there is a way to print a decimal number as binary
// but is there a way to transform a binary into decimal?
