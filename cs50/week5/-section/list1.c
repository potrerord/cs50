#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int number;
    struct node *next;
}
node;

// Defines the max number of nodes
int MAXNODES = 7;

int main(void)
{
    // create a pointer to our future list
    node *list = NULL;

    // Track the number of nodes
    int totalNodes = 0;

    // Get our nodes until we hit the max number
    while (totalNodes < MAXNODES)
    {
        // Get the number from the user for this node
        int x = get_int("Number: ");

        // Verify that this number being provided is valid.
        if (x == INT_MAX)
        {
            printf("\n");
            break;
        }

        // Allocate a new node.
        node *n = malloc(sizeof(node));
        n->number = x;
        n->next = NULL;

		// TODO: Add new node to head (front) of linked list.
        n->next = list;
        list->next = n;

        // Update the total number of nodes
        totalNodes++;

    }

	// TODO: Print all nodes.

    node *temp = list;

    while (temp != NULL)
    {
        printf("%i", temp->number);
        temp = temp->next;
    }

	// TODO: Free all nodes.

    free(n);

    node *temp2 = ptr->next;

    while (temp != NULL)
    {
        temp2 = temp->next;
        free(temp);
        temp = temp2;
    }
}