package main

import "fmt"

func main(){
	// calling phase
	app()
}

// declaration phase
func app(){
	httpclient := HttpClient{}
	httpclient.getUser("bob@clean.com")
	user := User{
		name: "Bob",
		email: "bob@clean.com",
	} 
	httpclient.createUser(user)
}

type HttpClient struct {
}

func (c HttpClient) getUser(email string){
	fmt.Println("Getting user...", email)
}

func (c HttpClient) createUser(user User){
	fmt.Println("Creating user...", user.name)
}

type User struct {
	name string
	email string
}

