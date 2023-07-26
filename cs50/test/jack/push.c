bool push(int n)
{
    if (s.size == s.CAPACITY) {
        return false;
    }

    for (int i = s.size; i > 0; i--) {
        s[i] = s[i - 1];
    }

    s[0] = n;
    s.size += 1;
    return true;
}
