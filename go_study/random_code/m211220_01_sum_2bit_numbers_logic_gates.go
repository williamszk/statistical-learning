// this is an exercise where we want to build a sum function that can consume two binary numbers of 2bits
// then the function will sum the binary numbers using logic expresisions only: and, or, xor
// the output is also in binary
// we can translate them later

package main

import "fmt"

func main() {

	A0 := 0
	A1 := 1

	B0 := 1
	B1 := 0

	answer := bitwiseSum2bits(A1, A0, B1, B0)

	fmt.Printf("%v\n", answer)
}

func bitwiseSum2bits(A1 int, A0 int, B1 int, B0 int) [3]int {
	// go bitwise operators
	xor_first_0 := A0 ^ B0
	and_first_0 := A0 & B0
	xor_first_1 := A1 ^ B1
	and_first_1 := A1 & B1

	// fmt.Printf("xor_first_0: %v\n", xor_first_0)
	// fmt.Printf("and_first_0: %v\n", and_first_0)
	// fmt.Printf("xor_first_1: %v\n", xor_first_1)
	// fmt.Printf("and_first_1: %v\n", and_first_1)

	xor_second_0 := and_first_0 ^ xor_first_1
	and_second_0 := and_first_0 & xor_first_1
	xor_second_1 := and_second_0 ^ and_first_1

	S0 := xor_first_0
	S1 := xor_second_0
	S2 := xor_second_1

	answer := [3]int{S2, S1, S0}

	return answer
}
