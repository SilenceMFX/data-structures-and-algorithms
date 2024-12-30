def binary_search(array, target):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        elif array[mid] > target:
            high = mid
    return -1


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(binary_search(array, 7))
