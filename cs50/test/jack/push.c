bool push(int n)
{
    // If size is already maxed out, return false.
    if (s.size >= CAPACITY)
    {
        return false;
    }

    // Iterate from the index after the last one in s to its second.
    for (int i = s.size; i > 0; i--)
    {
        // From right to left, move all values to their right.
        s.numbers[i] = s.numbers[i - 1];
    }

    // Change the value at the first index to n.
    s.numbers[0] = n;

    // Increment the size of the stack.
    s.size += 1;

    sys.exit(0);
}
