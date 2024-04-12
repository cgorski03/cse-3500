import random
import time
import sys
from memory_profiler import memory_usage

LIST_SIZES = [100, 500, 1000, 1500, 2000, 10000, 50000]


def pivot_random(arr):
    return random.choice(arr)


def quicksort_non_recursive(arr):
    """Non-recursive quicksort implementation"""
    stack = [(0, len(arr) - 1)]
    while stack:
        low, high = stack.pop()
        if low < high:
            pivot = pivot_random(arr[low : high + 1])
            i = low - 1
            j = high + 1
            while True:
                i += 1
                while arr[i] < pivot:
                    i += 1
                j -= 1
                while arr[j] > pivot:
                    j -= 1
                if i >= j:
                    break
                arr[i], arr[j] = arr[j], arr[i]
            stack.append((low, j))
            stack.append((j + 1, high))


def quicksort(arr):
    # Base case: arrays with 0 or 1 element are already sorted
    if len(arr) <= 1:
        return arr
    pivot = pivot_random(arr)

    # Create three lists to store the elements less than, equal to, and greater than the pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Sort the left and right lists
    return quicksort(left) + middle + quicksort(right)


def time_sort(arr, sorting_algorithm):
    """Quicksort wrapper that times the function and measures memory usage"""
    start = time.time()
    mem_usage = memory_usage((sorting_algorithm, (arr,), {}), interval=0.1)
    end = time.time()
    return end - start, max(mem_usage)


def measure_runtime(n):
    """RETURNS: 2 tuples (quick_time, quick_mem), (radix_time, radix_mem)"""
    input_array = list(range(n))
    # Randomize the array
    random.shuffle(input_array)
    quick_time, quick_mem = time_sort(input_array, quicksort_non_recursive)
    radix_time, radix_mem = time_sort(input_array, radix_sort)
    return (quick_time, quick_mem), (radix_time, radix_mem)


def radix_sort(arr):
    """Radix sort implementation"""
    radix_array = [[], [], [], [], [], [], [], [], [], []]
    max_value = max(arr)
    current_exponent = 1
    # MAIN CONDITION: Loop until the max value divided by the exponent(one, tens place) is less than 0
    # Basically, we will loop as many times as the number of digits in the max value
    while max_value // current_exponent > 0:
        # Loop through the array and append the values to the corresponding bucket
        while len(arr) > 0:
            # Pop the last element from the array
            val = arr.pop()
            # Get the digit at the current exponent place
            digit_bucket = (val // current_exponent) % 10
            # Append the value to the corresponding bucket
            radix_array[digit_bucket].append(val)

        for bucket in radix_array:
            # Extend the array with the values in the bucket
            arr.extend(bucket)
        # Move to the next place
        current_exponent *= 10
    return arr


if __name__ == "__main__":
    sys.setrecursionlimit(3000)
    for size in LIST_SIZES:
        (quicksort_time, quicksort_mem), (radixsort_time, radixsort_mem) = (
            measure_runtime(size)
        )
        print(f"List Size: {size}")
        print(f"Quicksort Time: {quicksort_time} seconds")
        print(f"Quicksort Memory: {quicksort_mem} MiB")
        print(f"Radix Sort Time: {radixsort_time} seconds")
        print(f"Radix Sort Memory: {radixsort_mem} MiB")
        print("------------------------")
