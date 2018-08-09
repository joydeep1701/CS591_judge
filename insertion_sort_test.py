from runner import ProgramEvaluator
import exceptions
from pprint import pprint

code = """
void insertion_sort(int* arr, int size) {
  for (int i=0; i < size; i++) {
    // Store the current element
    // Assume that the left side is already sorted
    int temp = *(arr + i);
    int j = i;
    // Check whether the adjacent element in the left side
    // is greater or less than the current element
    while (j > 0 && temp < *(arr + j - 1)) {
      // Move the left side element one side forward
      *(arr + j) = *(arr + j - 1);
      j--;
    }
    *(arr + j) = temp;
  }
}
"""
with ProgramEvaluator('insertion_sort') as foo:
    foo.save_code(code)
    try:
        foo.compile()
    except exceptions.CompilationError as e:
        print(e)
    pprint(foo.evaluate('sort'))
