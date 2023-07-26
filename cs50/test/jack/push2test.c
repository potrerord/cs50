#include <stdio.h>
#include <stdbool.h>

const int CAPACITY = 50;

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
    s.size = 0;
    for (int i = 1; i < CAPACITY + 20; i++)
    {
        int butt[CAPACITY];
        for (int j = 0; j < CAPACITY; j++)
        {
            butt[j] = s.numbers[j];
        }
        push(i);
        printf("%i is: %i\n", i, s.numbers[0]);
    }
}


bool push(int n)
{
    // If size is already maxed out, reallocate memory.
    if (s.size >= CAPACITY)
    {
        numbers = realloc(numbers, s.size + 1)

        // If realloc failed, return false.
        if (numbers == NULL)
        {
            return false;
        }
    }

    // Change the value at the next available index to n.
    s->numbers[s.size] = n;

    // Increment the size of the stack.
    s.size += 1;

    return true;
}
