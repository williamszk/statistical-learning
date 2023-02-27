package main

import "fmt"

func main(){
	// calling phase
	app(getUser, createUser)
}

// https://stackoverflow.com/a/12655719/15875971

// declaration phase
func app(getUser GetUserFunc, createUser CreateUserFunc){
	getUser("bob@clean.com")
	user := User{
		name: "Bob",
		email: "bob@clean.com",
	} 
	createUser(user)
}

type GetUserFunc func(email string)

func getUser(email string){
	fmt.Println("Getting user...", email)
}

type CreateUserFunc func(user User)

func createUser(user User){
	fmt.Println("Creating user...", user.name)
}

type User struct {
	name string
	email string
}