// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/25398280?start=1110#overview 

#include <stdlib.h>
#include <stdio.h>

typedef struct node {
	int data;
	struct node* next;
} Node;

Node* createList(){
}

void printList(Node* head) {
		
	Node* tmp = head;
	while (tmp != NULL) {
		printf("%d - ", tmp->data);
		tmp = tmp->next;
	}
}



int main(){

	int i;
	int num;	
	int dataArr[] = {10, 11, 12, 1,2,3,4,5,6};
	int lenArr = sizeof(dataArr)/sizeof(int);

	Node* head = NULL;
	Node* cur = NULL;

	for (i = 0; i < lenArr; i++) {
		cur = malloc(sizeof(Node));	
		cur->data = dataArr[i];
		cur->next = head;
		head = cur;
	}	

	printList(head);


	return 0;
}
