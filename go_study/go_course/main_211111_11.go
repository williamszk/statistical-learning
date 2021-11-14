// go run main.go

package main

import "fmt"

func main() {
	fmt.Println("Hello World!")

	binaryCodeMap := map[string]string{
		"000": "A",
		"001": "B",
		"010": "C",
		"100": "D",
		"110": "E",
		"101": "F",
		"011": "G",
		"111": "H",
	}

	myMessage := [11]string{
		"010", "111", "110", "011", "000",
		"100", "110", "010", "000", "101", "110"}

	for _, val := range myMessage {
		letter := binaryCodeMap[val]
		fmt.Printf("%v", letter)
	}
}
