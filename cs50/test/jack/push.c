bool push(int n)
{
    if (s.size == CAPACITY) {
        return false;
    }

    for (int i = s.size; i > 0; i--) {
        s.numbers[i] = s.numbers[i - 1];
    }

    free(s.numbers[s.size]);
    s.numbers[0] = n;
    s.size += 1;
    return true;
}
