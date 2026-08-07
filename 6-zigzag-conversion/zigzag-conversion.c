#include <stdlib.h>
#include <string.h>

char* convert(char* s, int numRows) {
    int len = strlen(s);

    if (numRows <= 1 || numRows >= len) {
        char* result = (char*)malloc(len + 1);
        strcpy(result, s);
        return result;
    }

    // One buffer per row, worst case a row can hold the whole string
    char** rows = (char**)malloc(numRows * sizeof(char*));
    int* rowLen = (int*)calloc(numRows, sizeof(int));
    for (int i = 0; i < numRows; i++)
        rows[i] = (char*)malloc(len + 1);

    int curRow = 0;
    int goingDown = 0;

    for (int i = 0; i < len; i++) {
        rows[curRow][rowLen[curRow]++] = s[i];
        if (curRow == 0 || curRow == numRows - 1)
            goingDown = !goingDown;
        curRow += goingDown ? 1 : -1;
    }

    char* result = (char*)malloc(len + 1);
    int pos = 0;
    for (int i = 0; i < numRows; i++) {
        memcpy(result + pos, rows[i], rowLen[i]);
        pos += rowLen[i];
        free(rows[i]);
    }
    result[len] = '\0';

    free(rows);
    free(rowLen);
    return result;
}