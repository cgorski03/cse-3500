import random
import time
import sys

LIST_SIZES = [100, 500, 1000, 1500, 2000]


def pivot_last(arr):
    return arr[-1]


def pivot_random(arr):
    return random.choice(arr)


def quicksort(arr, pivot_algoithm):
    # Base case: arrays with 0 or 1 element are already sorted
    if len(arr) <= 1:
        return arr
    pivot = pivot_algoithm(arr)

    # Create three lists to store the elements less than, equal to, and greater than the pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Sort the left and right lists
    return quicksort(left, pivot_algoithm) + middle + quicksort(right, pivot_algoithm)


def time_quicksort(arr, pivot_algorithm):
    """Quicksort wrapper that times the function"""
    start = time.time()
    quicksort(arr, pivot_algorithm)
    end = time.time()
    return end - start


def time_radixsort(arr):
    """Radix sort wrapper that times the function"""
    start = time.time()
    radix_sort(arr)
    end = time.time()
    return end - start


def measure_runtime(n):
    """RETURNS: 3 time tuples (pivot_last, pivot_random) where array is in order of Sorted list, reverse sorted list, random list"""
    input_array = [x for x in range(n)]
    # Calculate the sorted times
    sorted_times = (
        time_quicksort(input_array, pivot_last),
        time_quicksort(input_array, pivot_random),
    )

    # Calculate the reverse sorted times
    input_array.reverse()
    reverse_times = (
        time_quicksort(input_array, pivot_last),
        time_quicksort(input_array, pivot_random),
    )

    # Calculate the randomized array times
    random.shuffle(input_array)
    random_times = (
        time_quicksort(input_array, pivot_last),
        time_quicksort(input_array, pivot_random),
        time_radixsort(input_array),
    )

    return sorted_times, reverse_times, random_times


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
        sorted_times, reverse_times, random_times = measure_runtime(size)
        print(f"Size: {size}")
        print("Sorted Array:")
        print(
            f"Pivot Last/ Random: {sorted_times[0]} seconds / {sorted_times[1]} seconds"
        )
        print("Reverse Sorted Array:")
        print(
            f"Pivot Last/ Random: {reverse_times[0]} seconds / {reverse_times[1]} seconds"
        )
        print("Randomly Sorted Array:")
        print(
            f"Pivot Last/ Random: {random_times[0]} seconds / {random_times[1]} seconds\n",
            f"Radix Sort: {random_times[2]} seconds\n",
        )
