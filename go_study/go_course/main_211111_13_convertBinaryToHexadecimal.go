// go run main.go

// exercice
package main

import (
	"errors"
	"fmt"
	"strings"
)

func main() {
	binaryCode := "0000 1011 1100"

	hexadecimalTranslantion, error := convertBinaryToHexadecimal(binaryCode)
	fmt.Println(error)
	fmt.Println(hexadecimalTranslantion)
}

// digital systems

// ideas about converting binary to hexadecimal

// build a function that receives an input as binary
// then converts the value into hexadecimal

func convertBinaryToHexadecimal(binaryCode string) (string, error) {

	numberBitsInByte := 4

	binaryToHexadecimal := map[string]string{
		"0000": "0",
		"0001": "1",
		"0010": "2",
		"0011": "3",
		"0100": "4",
		"0101": "5",
		"0110": "6",
		"0111": "7",
		"1000": "8",
		"1001": "9",
		"1010": "A",
		"1011": "B",
		"1100": "C",
		"1101": "D",
		"1110": "E",
		"1111": "F",
	}

	binaryCodeNoSpace := strings.Replace(binaryCode, " ", "", -1)

	lengthArray := len(binaryCodeNoSpace)
	// e.g. 01000, astrayLength is 1, there are 6 digits but we need
	// multiples of 4
	astrayLength := lengthArray % numberBitsInByte

	// fillerZeros := strings.Repeat("0", (numberBitsInByte - astrayLength))

	if astrayLength != 0 {
		return "", errors.New("You've inputed the wrong number of numbers.")
	} else {
		numSteps := lengthArray / numberBitsInByte
		hexadecimalArray := make([]string, numSteps)
		for i := 0; i < numSteps; i++ {
			byteCode := binaryCodeNoSpace[i*numberBitsInByte : (i+1)*numberBitsInByte]
			hexadecimalCode := binaryToHexadecimal[byteCode]
			hexadecimalArray = append(hexadecimalArray, hexadecimalCode)
		}
		hexadecimalTranslantion := strings.Join(hexadecimalArray, "")
		return hexadecimalTranslantion, nil
	}
}
