// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/25398280?start=1110#overview 

/** Here we want to make the list be presented in 
 * the reverse order, on main.c the liked list is being
 * created with the resersed order compared to the input
 * list.
 * */

#include <stdlib.h>
#include <stdio.h>

typedef struct node {
	int data;
	struct node* next;
} Node;

Node* createNode(int data){

	Node* curNode = malloc(sizeof(Node));
	curNode->data = data;
	return curNode;
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

	Node* head = createNode(dataArr[0]);
	Node* tmp = NULL;
	Node* tmp2 = NULL;

	for (i = 1; i < lenArr; i++) {
		if (i == 1) {

			tmp = createNode(dataArr[i]);
			head->next = tmp; 

		} else {

			tmp2 = createNode(dataArr[i]);	
			tmp->next = tmp2;
			tmp = tmp2;

		}
	}	

	printList(head);


	return 0;
}










