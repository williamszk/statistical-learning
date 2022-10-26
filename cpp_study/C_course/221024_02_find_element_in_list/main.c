#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct node
{
    int data;
    struct node *next;
} Node;

bool isNumInList(Node *head, int num)
{
    Node *current = head;

    while (current->next != NULL)
    {
        if (current->data == num)
        {
            return true;
        }
        current = current->next;
    }

    if (current->data == num)
        return true;

    return false;
}

int main()
{

    int i;
    int num;
    int dataArr[] = {10, 11, 12, 1, 2, 3, 4, 5, 6};
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

    printf("Is 0 inside the list? %d\n", isNumInList(head, 0));
    printf("Is 10 inside the list? %d\n", isNumInList(head, 10));

    return 0;
}