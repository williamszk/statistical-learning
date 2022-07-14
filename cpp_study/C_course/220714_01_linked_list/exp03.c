#include <stdio.h>
#include <stdlib.h>

struct node {
	int value;
	struct node* next;
};

typedef struct node node_t;


void printLinkedList(node_t *head){
	node_t *temp = head;

	while (temp != NULL) {
		printf("%d - ", temp->value);
		temp = temp->next;
	}
	printf("\n");
}



int main() {

	// here we declare the nodes
	node_t n1, n2, n3;
	node_t n4;

	// note that head is a pointer to a node_t
	node_t *head;

	n1.value = 45;
	n2.value = 8;	
	n3.value = 32;

	head = &n1;
	n3.next = NULL;
	n2.next = &n4;
	n1.next = &n2;


	// add new node and insert in the middle of the list
	n4.value = 13;
	n4.next = &n3; 

	printLinkedList(head);


	return 0;
}

