#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

// If we wanted to store anything inside data, we should use malloc
typedef struct Node
{
    int data;
    struct Node *next_node;
} Node;

typedef struct LinkedList
{
    Node *initial_node;
    uint64_t length;
} LinkedList;

// Build a function that:
// Given an index find the value that is stored in there.

LinkedList build_linked_list(int initial_data)
{
    Node initial_node = {
        .data = initial_data,
        .next_node = NULL};

    LinkedList out = {
        .initial_node = &initial_node,
        .length = 1};

    return out;
}

/* The elements of a linked list are nodes.
We know the last element of a linked list because its next_node field is null.
If the value of n is greater than the size of the linked list, then the function
will return an status giving an error.
*/
int get_nth_element_from_linked_list(LinkedList target, int n, Node *nth_node)
{
    Node *current_node = target.initial_node;
    for (int i = 0; i < n; i++)
    {
    }
    return 0;
}

Node *find_last_element_of_linked_list(LinkedList target)
{
    Node *current_node = target.initial_node;
    while (1)
    {
        if (current_node->next_node == NULL)
        {
            return current_node;
        }
        current_node = current_node->next_node;
    }
}

int append_to_linked_list(LinkedList target, int new_valeu)
{
    Node *last_node = find_last_element_of_linked_list(target);
    Node new_node = {
        .data = 10,
        .next_node = NULL};

    last_node->next_node = &new_node;
    target.length += 1;
    return 0;
}

// build function get next node

int print_linked_list(LinkedList target)
{
    uint64_t length = target.length;
    printf("length: %ld\n", length);
    printf("[");
    Node *current_node = target.initial_node;
    for (int i = 0; i < length; i++)
    {
        if (i == length - 1){
            printf("%d]\n", target.initial_node->data);
        }else {
            printf("%d ", target.initial_node->data);
        }
        current_node = current_node->next_node;
    }
}

int main()
{
    // void *ptr = malloc(1000);
    // free(ptr);
    // printf("Hello World!\n");
    // Initialize first node
    // Node a_node = {
    //     .data = 10,
    //     .next_node = NULL};
    // I don't need to initialize the next_node
    //--------------------------------------------------------------------------
    // Initialized a linked list

    LinkedList my_linked_list = build_linked_list(0);
    printf("my_linked_list.initial_node->data = %d\n", my_linked_list.initial_node->data);

    print_linked_list(my_linked_list);

    return 0;
}