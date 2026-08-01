int reverse(int x) {
    long long result = 0;
    long long temp = x;

    if (temp < 0) {
        temp = -temp;
    }

    while (temp != 0) {
        int digit = temp % 10;
        temp /= 10;
        result = result * 10 + digit;

        if (result > INT_MAX || result < INT_MIN) {
            return 0;
        }
    }

    if (x < 0) {
        result = -result;
    }

    return (int)result;
}