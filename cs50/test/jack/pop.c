bool pop(int *n)
{
    // If there is nothing to pop, return false.
    if (s.size == 0) {
        return false;
    }

    // Store the value at the last index in the arg pointer.
    *n = s.numbers[s.size - 1];

    // Decrement the size of the stack.
    s.size--;
    return true;
}
