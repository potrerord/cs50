#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

typedef struct
{
    int *numbers;
    int size;
}
stack;

stack t;

bool push(int n);

int main(void)
{
    t.size = 0;
    for (int i = 1; i < 5042; i++)
    {
        int butt[5042];
        for (int j = 0; j < t.size; j++)
        {
            butt[j] = t.numbers[j];
        }
        push(i);
        printf("%i is: %i\n", i, t.numbers[0]);
    }
}


bool push(int n)
{
    // Reallocate memory for new element.
    t.numbers = realloc(t.numbers, sizeof(int) * (t.size + 1));

    // If realloc failed, return false.
    if (t.numbers == NULL)
    {
        return false;
    }

    // Change the value at the next available index to n.
    t.numbers[t.size] = n;

    // Increment the size of the stack.
    t.size += 1;

    return true;
}
