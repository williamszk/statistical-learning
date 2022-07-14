
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

	// note that head is a pointer to a node_t
	node_t *head;

	n1.value = 45;
	n2.value = 8;	
	n3.value = 32;

	// link the nodes
	head = &n3;
	// the head starts at n3
	n3.next = &n2;
	n2.next = &n1;
	
	// to know when the linked list stops
	n1.next = NULL;

	printLinkedList(head);


	return 0;
}

