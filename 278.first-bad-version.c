// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

int firstBadVersion(int n) {
    int l, r, m;
    l = 1;
    r = n;

    while (l < r) {
        m = l + (r-l) / 2;
        if (isBadVersion(m))
            r = m;
        else
            l = m + 1;
    }
    return l;
}
