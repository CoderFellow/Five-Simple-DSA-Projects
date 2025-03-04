import random
from SortingAlgorithms import bubbleSort, selectionSort, mergeSort, quickSort

# Generate a random list to test
arr = random.sample(range(1, 100), 10)  # List of 10 random integers

print(f"Original Array: {arr}")

# Using the custom-built Bubble Sort algorithm
arr_bubble = arr.copy()
print(f"\nBubble Sort: {bubbleSort(arr_bubble)}")  # Changed to bubbleSort

# Using the custom-built Selection Sort algorithm
arr_selection = arr.copy()
print(f"\nSelection Sort: {selectionSort(arr_selection)}")

# Using the custom-built Merge Sort algorithm
arr_merge = arr.copy()
print(f"\nMerge Sort: {mergeSort(arr_merge)}")

# Using the custom-build Quick Sort algorithm
arr_quick = arr.copy()
print(f"\nQuick Sort: {quickSort(arr_quick)}")