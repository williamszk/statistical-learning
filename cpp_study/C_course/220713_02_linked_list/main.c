// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/25398280#overview

#include <stdio.h>
#include <stdlib.h>



typedef struct Node
{
    int data;
    struct Node *next;
    // without including struct Node, this would give an error telling
    // that Node is not defined
} Node;

// Node *createListOfNumbers()
// {
//     Node *head; // keep the head of the liked list
//     Node *holderNode;
//     int num;
//     head = (Node *)malloc(sizeof(Node));
//     holderNode = head;
//     holderNode->data = num;
//     holderNode->next = (Node *)malloc(sizeof(Node));
//     holderNode = holderNode->next;
//     holderNode->data = num;
//     return head;
// }

void appendToNode(Node *ptrNode, int num)
{
    Node *holder = malloc(sizeof(Node));
    holder->data = num;
    holder->next = NULL;

    ptrNode->next = holder;
    // next is a pointer to Node
}


int main()
{
    // Node *ptrHead = malloc(sizeof(Node));
    Node *ptrHead; // this will give an access violation error, if we try to access its content
    // we would need to allocate some memory in the heap, so the pointer has somewhere to point to
    // if (ptrHead == 0) {
    //     printf("ptrHead is a null pointer");
    // }
    // ptrHead->data = 0;
    // ptrHead->next = NULL; 

    // appendToNode(ptrHead, 1);


    return 0;
}
