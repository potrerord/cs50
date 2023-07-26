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
    for (int i = 0; i < CAPACITY; i++)
    {
        push(1);
    }
}


bool push(int n)
{
    if (s.size >= CAPACITY) {
        return false;
    }

    for (int i = s.size - 1; i > 0; i--) {
        s.numbers[i] = s.numbers[i - 1];
    }

    s.numbers[0] = n;
    s.size += 1;
    return true;
}
