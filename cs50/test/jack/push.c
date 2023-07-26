bool push(int n)
{
    // If size is already maxed out, return false.
    if (s.size >= CAPACITY)
    {
        return false;
    }

    // Change the value at the first index to n.
    s.numbers[s.size] = n;

    // Increment the size of the stack.
    s.size += 1;

    return true;
}
