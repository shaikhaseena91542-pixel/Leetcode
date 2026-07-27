char* addBinary(char* a, char* b) {
    int i = strlen(a) - 1;
    int j = strlen(b) - 1;
    int carry = 0;

    // Result can be at most 1 char longer than the longer input, plus null terminator
    int maxLen = (i > j ? i : j) + 3;
    char* result = (char*)malloc(maxLen * sizeof(char));
    int k = 0;

    while (i >= 0 || j >= 0 || carry) {
        int total = carry;
        if (i >= 0) total += a[i--] - '0';
        if (j >= 0) total += b[j--] - '0';
        result[k++] = (total % 2) + '0';
        carry = total / 2;
    }

    result[k] = '\0';

    // Reverse the result in place
    for (int start = 0, end = k - 1; start < end; start++, end--) {
        char temp = result[start];
        result[start] = result[end];
        result[end] = temp;
    }

    return result;
}