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


node_t* createNode(int value){
	node_t* result = malloc(sizeof(node_t));

	result->value = value;
	result->next = NULL;

}

node_t* insertAtHead(node_t* head, node_t* nodeToInsert) {
	nodeToInsert->next = head;
	return nodeToInsert;
}

int main() {
	int i;
	// dynamic allocation uses the heap and malloc
	// static allocation uses the stack and does not uses malloc
	
	node_t* head = NULL;
	node_t* tmp;

	for (i = 0; i<25; i++){
		tmp = createNode(i);
		head = insertAtHead(head, tmp);
	}


	printLinkedList(head);

	return 0;
}


