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

// https://www.google.com/search?q=xor+table&rlz=1C1GCEU_pt-BRBR974BR974&tbm=isch&source=iu&ictx=1&fir=Dxmvybd5iC2ehM%252CT_ctfO_9UA3ceM%252C%252Fm%252F09j4m5%253BhD31H64jsFNuUM%252CcbOD3hyd-L8XTM%252C_%253BeWWxa6n9PwRf9M%252CFmgFJdqMo1NrkM%252C_%253BvKfz5Vcu__PmnM%252CqZNsKqkIfvQTRM%252C_%253B1xXPC_hOnLV95M%252CFmgFJdqMo1NrkM%252C_%253BiXtHvZxPHP1PdM%252CWkuTm94sNfojBM%252C_&vet=1&usg=AI4_-kQBrPuQB_JwmBjNCGfQonIUEDBY0g&sa=X&ved=2ahUKEwid-bvpkfP0AhXkm-AKHdm1DYQQ_B16BAg0EAE#imgrc=Dxmvybd5iC2ehM
// next implement an xor gate using just and, or gates
