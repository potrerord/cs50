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
