package main

import (
	"github.com/gofiber/fiber/v2"
)

func main() {
	app := fiber.New()

	// fmt.Println("Starting server in port 5000")

	app.Get("/", func(c *fiber.Ctx) error {
		return c.SendString("hi")
	})

	app.Listen(":5000")
}
