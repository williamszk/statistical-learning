// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/25398328#questions/16461164

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>


typedef struct node
{
    int data;
    struct node *next;
} Node;

int countNumInList(Node* head, int num){
    int ctr = 0;
    Node * curr = head;
    while (true) {
        if (curr->data == num)
            ctr++;

        if (curr->next == NULL)
            break;
        
        curr = curr->next;
    }

    return ctr;
}

int main(){

    int i;
    int num;
    int dataArr[] = {10, 11, 12, 6, 6, 3, 1, 2, 3, 4, 5, 6};
    int lenArr = sizeof(dataArr) / sizeof(int);

    Node *head = NULL;
    Node *cur = NULL;

    for (i = 0; i < lenArr; i++)
    {
        cur = malloc(sizeof(Node));
        cur->data = dataArr[i];
        cur->next = head;
        head = cur;
    }

    printf("Count frequency of 6 in linked list: %d\n", countNumInList(head, 6));
    printf("Count frequency of 10 in linked list: %d\n", countNumInList(head, 10));

    return 0;
}
