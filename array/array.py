import random

arr: list[int] = [0] * 5
nums: list[int] = [1, 2, 3, 4, 5]
print(arr)
print(nums)


def random_access(array: list[int]) -> int:
    random_index = random.randint(0, len(array) - 1)
    random_num = array[random_index]
    return random_num


def insert(array: list[int], index: int, num: int):
    for i in range(len(array) - 1, index, - 1):
        array[i] = array[i - 1]
    array[index] = num


def delete(array: list[int], index: int):
    for i in range(index, len(array) - 1, 1):
        array[i] = array[i + 1]
    array[len(array) - 1] = 0


if __name__ == '__main__':
    print(random_access(nums))
    insert(nums, 0, 2)
    print(nums)
    delete(nums, 0)
    print(nums)
