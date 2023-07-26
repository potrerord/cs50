bool push(int n)
{
    // If size is already maxed out, reallocate memory.
    if (s.size >= CAPACITY)
    {
        numbers = realloc(numbers, s.size + 1)
    }

    // Change the value at the next available index to n.
    s->numbers[s.size] = n;

    // Increment the size of the stack.
    s.size += 1;

    return true;
}
