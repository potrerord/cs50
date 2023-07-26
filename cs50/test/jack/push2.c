bool push(int n)
{
    // If size is already maxed out, return false.
    if (s.size >= CAPACITY)
    {
        s.size += 1;
        ptr = realloc(ptr, s.size)
    }

    // Change the value at the next available index to n.
    s->numbers[s.size] = n;

    // Increment the size of the stack.
    s.size += 1;

    return true;
}
