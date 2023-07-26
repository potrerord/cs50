#include <stdio.h>
#include <stdbool.h>

const int CAPACITY = 50;

typedef struct
{
    int numbers[CAPACITY];
    int size;
}
stack;

stack s;

bool push(int n);

int main(void)
{
    s.size = 0;
    for (int i = 0; i < CAPACITY + 20; i++)
    {
        int butt[CAPACITY];
        for (int j = 0; j < CAPACITY; j++)
        {
            butt[j] = s.numbers[j];
        }
        push(i);
        printf("%i is: %i\n", i, s.numbers[i]);
    }
}


bool push(int n)
{
    // If size is already maxed out, return false.
    if (s.size >= CAPACITY)
    {
        return false;
    }

    // Iterate from last index to the second.
    for (int i = s.size; i > 0; i--)
    {
        //
        s.numbers[i] = s.numbers[i - 1];
    }

    // Change the value at the first index to n.
    s.numbers[0] = n;

    // Increment the size of the stack.
    s.size += 1;

    return true;
}
