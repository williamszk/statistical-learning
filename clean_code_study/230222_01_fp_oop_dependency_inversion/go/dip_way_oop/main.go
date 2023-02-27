package main

import "fmt"

func main(){
	// calling phase
	client := HttpClient{}
	app(client)
}

// declaration phase
func app(client ClientInterface){
	client.getUser("bob@clean.com")
	user := User{
		name: "Bob",
		email: "bob@clean.com",
	} 
	client.createUser(user)
}

type ClientInterface interface {
	getUser(email string) 
	createUser(user User)
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