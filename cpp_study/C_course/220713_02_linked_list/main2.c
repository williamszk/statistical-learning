#include <stdio.h>
#include <stdlib.h>


typedef struct Node
{
    int data;
    struct Node *next;
} Node;

int main() {
    int i;

    Node *head = (Node *)malloc(sizeof(Node));
    head->data = 0;
    Node *holder = (Node *)malloc(sizeof(Node));
    head->next = holder;

    // fill the nodes with numbers
    for (i = 1; i <= 10; i++)
    {
        holder->next = (Node *)malloc(sizeof(Node));
        holder = holder->next;
        holder->data = i;
    }

    // get the information back using the head node 

    printf("%d\n", head->data);
    holder = head->next;
    while (1) {

        printf("%d\n", holder->data);
        holder = holder->next;

        if (holder->next == )

        break;
    }


}
