package main

import (
	"fmt"
	"os"
	"strconv"

	"golang.org/x/crypto/sha3"
)

func main() {

	message := "hello123"
	length := 8

	argLen := len(os.Args[1:])

	if argLen > 0 {
		message = string(os.Args[1])
	}

	if argLen > 1 {
		length, _ = strconv.Atoi(os.Args[2])
	}

	data := []byte(message)
	hash := make([]byte, length)

	sha3.ShakeSum128(hash, data)
	fmt.Printf("Shake 128: %x\n", hash)

	sha3.ShakeSum256(hash, data)
	fmt.Printf("Shake 256: %x\n", hash)

	// Observed:
	// Shake 128: 1b85861510bc4d8e
	// Shake 256: ade612ba265f92de

	// Test vector:
	// Input word: hello123
	// Length (bytes): 8
	//
	// -----SHAKE-----
	//
	// Shake 128 bit:  1b85861510bc4d8e
	// Shake 256 bit:  ade612ba265f92de
}
