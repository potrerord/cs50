bool push(int n)
{
    // If size is already maxed out, reallocate memory.
    if (t.size >= CAPACITY)
    {
        numbers = realloc(numbers, t.size + 1)

        // If realloc failed, return false.
        if (numbers == NULL)
        {
            return false;
        }
    }

    // Change the value at the next available index to n.
    t->numbers[t.size] = n;

    // Increment the size of the stack.
    t.size += 1;

    return true;
}
