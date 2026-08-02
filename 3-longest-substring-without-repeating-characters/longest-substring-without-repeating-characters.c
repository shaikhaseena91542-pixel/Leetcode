int lengthOfLongestSubstring(char *s) {
    int lastIndex[128];
    memset(lastIndex, -1, sizeof(lastIndex));

    int left = 0, maxLen = 0;
    int n = strlen(s);

    for (int right = 0; right < n; right++) {
        unsigned char ch = s[right];
        if (lastIndex[ch] >= left) {
            left = lastIndex[ch] + 1;
        }
        lastIndex[ch] = right;
        int windowLen = right - left + 1;
        if (windowLen > maxLen) {
            maxLen = windowLen;
        }
    }

    return maxLen;
}