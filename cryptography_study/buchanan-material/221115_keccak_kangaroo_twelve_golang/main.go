package main

import (
	"encoding/hex"
	"fmt"
	"os"

	"github.com/mimoo/GoKangarooTwelve/K12"
)

func main() {

	customStr := ""
	message := ""

	argCount := len(os.Args[1:])

	if argCount > 0 {
		customStr = string(os.Args[1])
	}
	if argCount > 1 {
		message = string(os.Args[2])
	}

	customStrBytes := []byte(customStr)
	messageBytes := []byte(message)
	out := make([]byte, 32)

	K12.K12Sum(customStrBytes, messageBytes, out)
	fmt.Printf("Custom string:\t%s\nMessage:\t%s\n\n", customStr, message)
	fmt.Printf("Hash:\t%s\n", hex.EncodeToString(out))

	// Should be output:
	// Custom string:	Hello
	// Message:	qwerty
	// Hash:	d7aa928c520c8d48a0734ad96c2b43d237197f7bedab6ef014c7ed5f60fc160b

	// Custom string: hello
	// Message:        there
	// Hash:   88f8c758b209b8a6cb36030a3cb9a8d79b8e4325dfdd1563bb8aeafeac9dead4

	// Custom string:  Hello
	// Message:        qwerty
	// Hash:   d7aa928c520c8d48a0734ad96c2b43d237197f7bedab6ef014c7ed5f60fc160b

}
