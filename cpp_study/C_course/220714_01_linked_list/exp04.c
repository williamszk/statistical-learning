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


node_t* create_node(int value){
	node_t* result = malloc(sizeof(node_t));

	result->value = value;
	result->next = NULL;

}

int main() {

	// dynamic allocation uses the heap and malloc
	// static allocation uses the stack and does not uses malloc
	
	node_t* head;
	node_t* tmp;

	tmp = create_node(32);
	head = tmp;
	tmp = create_node(8);
	tmp->next = head;	
	head = tmp;
	tmp = create_node(34);
	tmp->next = head;
	head = tmp;

	printLinkedList(head);

	return 0;
}


