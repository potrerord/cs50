bool push(int n)
{
    if (s.size == s.CAPACITY) {
        return false;
    }

    int temp, temp2;
    
    for (int i = 0, size = s.size; i < size; i++) {
        temp = s[i];
        temp2 = s[i + 1]
        s[i] = n;
        s[i + 1] = s[i]
    }
}
