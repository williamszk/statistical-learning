// https://www.google.com/search?q=xor+table&rlz=1C1GCEU_pt-BRBR974BR974&tbm=isch&source=iu&ictx=1&fir=Dxmvybd5iC2ehM%252CT_ctfO_9UA3ceM%252C%252Fm%252F09j4m5%253BhD31H64jsFNuUM%252CcbOD3hyd-L8XTM%252C_%253BeWWxa6n9PwRf9M%252CFmgFJdqMo1NrkM%252C_%253BvKfz5Vcu__PmnM%252CqZNsKqkIfvQTRM%252C_%253B1xXPC_hOnLV95M%252CFmgFJdqMo1NrkM%252C_%253BiXtHvZxPHP1PdM%252CWkuTm94sNfojBM%252C_&vet=1&usg=AI4_-kQBrPuQB_JwmBjNCGfQonIUEDBY0g&sa=X&ved=2ahUKEwid-bvpkfP0AhXkm-AKHdm1DYQQ_B16BAg0EAE#imgrc=Dxmvybd5iC2ehM
// next implement an xor gate using just and, or gates

package main

import "fmt"

func main() {

	A := 1
	B := 1

	// here we need to use xor already, I don't think that there is a bitwise operator for not
	// but we can use the property that 1^0=1, 1^1=0, that is 1^ is equivalente to a not operator
	and_first_0 := 1 ^ A&B
	or_first_0 := A | B

	and_second_0 := and_first_0 & or_first_0

	fmt.Println(and_second_0)

}
