#include <stdio.h>
#include <stdlib.h>
#include "module.h"

/**
 * @brief Input format:
 * [Size]
 * [... Array]
 * 
 * @param argc 
 * @param argv 
 * @return int 
 */

int main(int argc, char const *argv[])
{
    int size;
    int* arr;

    int correctness = 1;

    scanf("%d", &size);
    arr = malloc(sizeof(int) * size);
    for (int i = 0; i < size; i++) {
        scanf("%d", (arr + i));
    }
    for (int i = 0; i < size; i++) {
        // Call Binary search for every element
        if (arr[binarySearch(arr, 0, size, arr[i])] == arr[i]) {
            correctness *= 1;
        } else {
            correctness *= 0;
        }

    }
    printf("Correct: %s", correctness ? "True" : "False");

    return 0;
}
