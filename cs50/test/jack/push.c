const int CAPACITY = 50;

typedef struct
{
    int numbers[CAPACITY];
    int size;
}
stack;

stack s;

int main(void)
{
    s.size = 0;
    push(4)
}

bool push(int n)
{
    if (s.size == s.CAPACITY) {
        return false;
    }

    for (int i = s.size; i > 0; i--) {
        s[i] = s[i - 1];
    }

    s[0] = n;
    s.size += 1;
    return true;
}
