package main

import (
	"errors"
	"fmt"
	"io"
	"net/http"
	"os"
)

func sayHi(w http.ResponseWriter, r *http.Request) {
	io.WriteString(w, "Hi!\n")
}

//	func getHello(w http.ResponseWriter, r *http.Request) {
//		fmt.Printf("got /hello request\n")
//		io.WriteString(w, "Hello, HTTP!\n")
//	}

func main() {
	http.HandleFunc("/", sayHi)
	// http.HandleFunc("/hello", getHello)
	fmt.Println("Server running on port 5000")
	err := http.ListenAndServe(":5000", nil)
	if errors.Is(err, http.ErrServerClosed) {
		fmt.Printf("server closed\n")
	} else if err != nil {
		fmt.Printf("error starting server: %s\n", err)
		os.Exit(1)
	}
}

// [ ]  I noticed that the Go fiber message is wrong, it should be "Hi!" not "hi"
