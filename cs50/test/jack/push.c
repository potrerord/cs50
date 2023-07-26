bool push(int n)
{
    // If size is already maxed out, return false.
    if (s.size >= CAPACITY)
    {
        return false;
    }

    // Start at last available
    for (int i = s.size - 1; i > -1; i--)
    {
        s.numbers[i] = s.numbers[i - 1];
    }

    s.numbers[0] = n;
    s.size += 1;
    return true;
}
