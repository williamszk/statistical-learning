// Assume a Java-like style
// 

typedef struct Person {
	char firstName[20];
	char lastName[20];
   	int age;	
} Person;

// a Go style would be:
// SetFirstName(p Person, firstName string)
Person setFirstName(Person person, char *firstName)
{
	person.firstName = firstName;

	return person;
}








void getPerson(Person person)
{
	printf("First Name: %s\n", person.firstName);
	printf("Last Name: %s\n", person.lastName);
	printf("Age: %d\n", person.age);
}


