int romanToInt(char* s) {
    int total = 0;
    int prev_value = 0;

    for (int i = strlen(s) - 1; i >= 0; i--) {
        int value;

        switch (s[i]) {
            case 'I': value = 1; break;
            case 'V': value = 5; break;
            case 'X': value = 10; break;
            case 'L': value = 50; break;
            case 'C': value = 100; break;
            case 'D': value = 500; break;
            case 'M': value = 1000; break;
            default: value = 0; break;
        }

        if (value < prev_value) {
            total -= value;
        } else {
            total += value;
            prev_value = value;
        }
    }

    return total;
}