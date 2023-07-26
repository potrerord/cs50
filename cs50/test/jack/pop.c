bool pop(int *n)
{
    if (s.size == 0) {
        return false;
    }

    *n = s.numbers[0];

    for (int i = 0, len = s.size; i < len - 1; i++) {
        s.numbers[i] = s.numbers[i + 1];
    }

    s.size--;
    return true;
}
