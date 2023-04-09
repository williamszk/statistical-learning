package polygon

import "fmt"

type Polygon interface {
	Get()
}

type BlueTriangle struct{}

func (t BlueTriangle) Get() {
	fmt.Println("Hello from a BlueTriangle")
}

type RedTriangle struct{}

func (t RedTriangle) Get() {
	fmt.Println("Hello from a RedTriangle")
}

type GreenTriangle struct{}

func (t GreenTriangle) Get() {
	fmt.Println("Hello from a GreenTriangle")
}

type BlueRectangle struct{}

func (r BlueRectangle) Get() {
	fmt.Println("Hello from a BlueRectangle")
}

type RedRectangle struct{}

func (r RedRectangle) Get() {
	fmt.Println("Hello from a RedRectangle")
}

type GreenRectangle struct{}

func (r GreenRectangle) Get() {
	fmt.Println("Hello from a GreenRectangle")
}

type BluePentagon struct{}

func (p BluePentagon) Get() {
	fmt.Println("Hello from a BluePentagon")
}

type RedPentagon struct{}

func (p RedPentagon) Get() {
	fmt.Println("Hello from a RedPentagon")
}

type GreenPentagon struct{}

func (p GreenPentagon) Get() {
	fmt.Println("Hello from a GreenPentagon")
}
