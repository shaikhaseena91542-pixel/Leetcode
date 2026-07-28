#include <stdlib.h>
#include <string.h>

void backtrack(char* current, int pos, int open_count, int close_count, int n, char** result, int* returnSize) {
    if (pos == 2 * n) {
        current[pos] = '\0';
        result[*returnSize] = strdup(current);
        (*returnSize)++;
        return;
    }

    if (open_count < n) {
        current[pos] = '(';
        backtrack(current, pos + 1, open_count + 1, close_count, n, result, returnSize);
    }

    if (close_count < open_count) {
        current[pos] = ')';
        backtrack(current, pos + 1, open_count, close_count + 1, n, result, returnSize);
    }
}

char** generateParenthesis(int n, int* returnSize) {
    int maxResults = 1;
    for (int i = 0; i < n; i++) {
        maxResults *= 4;
    }

    char** result = (char**)malloc(sizeof(char*) * maxResults);
    char* current = (char*)malloc(sizeof(char) * (2 * n + 1));
    *returnSize = 0;

    backtrack(current, 0, 0, 0, n, result, returnSize);

    free(current);
    return result;
}