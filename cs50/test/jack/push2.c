bool push(int n)
{
    // Reallocate memory for new element.
    t.numbers = realloc(t.numbers, sizeof(int) * (t.size + 1));

    // If realloc failed, return false.
    if (t.numbers == NULL)
    {
        return false;
    }

    // Change the value at the next available index to n.
    t.numbers[t.size] = n;

    // Increment the size of the stack.
    t.size += 1;

    return true;
}
