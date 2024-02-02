import time
from tabulate import tabulate


def bsearch(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]

        if mid_value == target:
            return True
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid - 1
    return False


def brute_force_solution(target_nums: list[int], addition_nums: list[int]) -> float:
    start_time = time.time()
    resultArray = []

    for target_number in target_nums:
        found_pair = False
        for a in addition_nums:
            for b in addition_nums:
                if a + b == target_number:
                    found_pair = True
                    resultArray.append([a, b, target_number])
                    break
            if found_pair:
                break
    return time.time() - start_time


def binary_search_solution(target_nums: list[int], addition_nums: list[int]) -> float:
    start_time = time.time()

    resultArray = []
    addition_nums = sorted(addition_nums)
    for target_number in target_nums:
        for number in addition_nums:
            if (bsearch(addition_nums, (target_number - number))):
                resultArray.append(target_number)
                break
    return time.time() - start_time


if __name__ == '__main__':
    n_numbers = 1
    time_data = [['Brute Force'], ['Binary Search']]
    headers = ['Title']
    for i in range(0, 6):
        n_numbers *= 10

        with open(f'listNumbers-{n_numbers}.txt', 'r') as file:
            usable_nums = [int(line.strip()) for line in file]

        with open(f'listNumbers-{n_numbers}-nsol.txt', 'r') as file:
            numbers = [int(line.strip()) for line in file]

        bsearch_time = binary_search_solution(numbers, usable_nums)
        brute_time = brute_force_solution(numbers, usable_nums)

        time_data[0].append(brute_time)
        time_data[1].append(bsearch_time)

        headers.append(n_numbers)
        print(f'{i}/6 tests complete \r', end='')
    print(tabulate(time_data, headers=headers, tablefmt="pretty"))
