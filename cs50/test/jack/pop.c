bool pop(int *n)
{
    if (s.size == 0) {
        return false;
    }

    n = s[0];

    for (int i = 0, len = s.size; i < len - 1; i++) {
        s[i] = s[i + 1]
    }

    s.size--;
    return true;
}
