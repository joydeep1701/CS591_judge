#include <stdio.h>
#include <stdlib.h>
#include "module.h"

int main(int argc, char const *argv[]) {
  int size;
  int* arr;
  int correctness = 1;
  scanf("%d", &size);
  arr = malloc(sizeof(int) * size);
  for (int i = 0; i < size; i++) {
    scanf("%d", (arr + i));
  }
  insertion_sort(arr, size);
  for (int i = 1; i < size; i++) {
    correctness = correctness && *(arr + i) >= *(arr + i - 1);
  }
  printf("Correct: %s", correctness ? "True" : "False");
  return 0;
}
